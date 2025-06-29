
from fastapi import HTTPException,status

UserAlreadyExistsExceptions = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует",
)

