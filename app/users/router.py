

from fastapi import APIRouter, Response,  Request


from app.exceptions import UserAlreadyExistsExceptions, IncorrectEmailOrPasswordException
from app.users.aouth_google import oauth

from app.users.models import UsersDao,ModelUser
# from app.users.dependencies import get_current_active_user
from app.users.schemas import UserBase, UserCreate, UserRead, UserLogin
from app.users.auth import get_password_hash, auth_user, create_refresh_token, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
async def register_user(user_data: UserCreate):
    existing_user = await UsersDao.find_one_or_none({'phone_number': user_data.phone_number})

    if existing_user:
        raise UserAlreadyExistsExceptions

    hashed_password = get_password_hash(user_data.password)
    await UsersDao.add(ModelUser(
        name = user_data.name,
        phone_number=user_data.phone_number,
        password=hashed_password,
    ))


@router.post("/login")
async def login_user(response: Response, user_data: UserLogin):
    user = await auth_user(user_data.phone_number, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    refresh_token = create_refresh_token({"sub":str(user.id)})
    response.set_cookie("token", value=refresh_token, httponly=True,secure=True, samesite="strict")

    access_token = create_access_token({"sub":str(user.id)})
    return access_token

@router.get("/login/google")
async def login_via_google(request: Request):
    redirect_uri = request.url_for('auth_via_google')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/auth/google")
async def auth_via_google(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = token['userinfo']
    return user


# @router.post("/token")
# async def login_for_access_token(
#     form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
# )-> Token:
#
#     user = await auth_user(form_data.username, form_data.password)
#
#     if not user:
#         raise IncorrectEmailOrPasswordException
#     access_token = create_access_token({"sub":str(user.id)})
#
#
#     return Token(access_token=access_token, token_type="bearer")
#
# @router.get("/users/me/")
# async def read_users_me(
#     current_user: Annotated[UserRead, Depends(get_current_active_user)],
# ):
#
#     return current_user
