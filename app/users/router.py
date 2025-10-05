from fastapi import APIRouter, Request, Response

from app.exceptions import (
    ExceptionLogg,
    IncorrectEmailOrPasswordException,
    IncorrectEmailOrPasswordHandlerException,
    ServerFailedException,
    TokenExpiredException,
    UserAlreadyExistsExceptions,
    UserAlreadyExistsHandlerExceptions,
)
from app.logger import log
from app.users.auth import (
    auth_user,
    create_access_token,
    create_refresh_token,
    get_password_hash,
)
from app.users.auth_google import oauth
from app.users.dependencies import current_user
from app.users.models import ModelUser, UsersDao
from app.users.schemas import UserCreate, UserLogin

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register_user(user_data: UserCreate):
    try:
        existing_user = await UsersDao.find_one_or_none(
            {"phone_number": user_data.phone_number}
        )

        if existing_user:
            raise UserAlreadyExistsHandlerExceptions()

        hashed_password = get_password_hash(user_data.password)
        await UsersDao.add(
            ModelUser(
                name=user_data.name,
                phone_number=user_data.phone_number,
                password=hashed_password,
            )
        )
    except UserAlreadyExistsHandlerExceptions:
        log.info("User already exists")
        raise UserAlreadyExistsExceptions

    except Exception:
        await ExceptionLogg("User registration failed")


@router.post("/login")
async def login_user(request: Request, response: Response, user_data: UserLogin):
    try:
        user = await auth_user(user_data.phone_number, user_data.password)
        if not user:
            raise IncorrectEmailOrPasswordHandlerException()
        refresh_token = create_refresh_token({"sub": str(user.id)})
        response.set_cookie(
            "token", value=refresh_token, httponly=True, secure=True, samesite="strict"
        )

        access_token = create_access_token({"sub": str(user.id)})
        return access_token
    except IncorrectEmailOrPasswordHandlerException:
        log.warning(
            "Login failed: incorrect credentials", clien_host=request.client.host
        )
        raise IncorrectEmailOrPasswordException
    except Exception:
        await ExceptionLogg("Login Failed")


@router.get("/refresh")
async def refresh_access_token(request: Request):
    try:

        token = request.cookies.get("token")
        if not token:
            raise TokenExpiredException

        user = await current_user(token)
        if not user:
            raise ServerFailedException

        access_token = create_access_token({"sub": str(user.id)})
        return access_token

    except Exception as e:
        log.warning(e, exc_info=True)


@router.get("/login/google")
async def login_via_google(request: Request):
    try:
        redirect_uri = request.url_for("auth_via_google")
        return await oauth.google.authorize_redirect(request, redirect_uri)
    except Exception:
        await ExceptionLogg("Login Failed")


@router.get("/auth/google")
async def auth_via_google(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
        user = token["userinfo"]
        return user
    except Exception:
        await ExceptionLogg("Login Failed")
