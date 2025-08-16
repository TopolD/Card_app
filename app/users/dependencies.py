from datetime import datetime, timezone
from typing import Annotated

from fastapi import Depends, Request
from jose import JWTError, jwt

from app.config import settings
from app.exceptions import (
    IncorrectTokenFormaException,
    TokeAbsentException,
    TokenExpiredException,
    UserIsNotPresentHTTPException,
)
from app.users.models import ModelUser, UsersDao


def get_token(request: Request) -> str:
    token = request.cookies.get("token")

    if not token:
        raise TokeAbsentException
    return token


async def current_user(token):

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY_REFRESH, algorithms=settings.ALGORITHM
        )
    except JWTError :
        raise IncorrectTokenFormaException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.now(timezone.utc).timestamp()):
        raise TokenExpiredException
    user_id: str | None = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentHTTPException
    user = await UsersDao.find_by_id(user_id)
    if not user:
        raise UserIsNotPresentHTTPException
    return user


async def get_current_user(token: Annotated[str, Depends(get_token)]) -> ModelUser:
    return await current_user(token)
