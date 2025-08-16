from fastapi import HTTPException, status
from pydantic import ValidationError
from pymongo.errors import PyMongoError

from app.logger import log

UserAlreadyExistsExceptions = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Пользователь уже существует"
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверная почта или пароль"
)
TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен истек"
)

TokeAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен отсутствует"
)


IncorrectTokenFormaException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверный формат токена "
)

UserIsNotPresentHTTPException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


InactiveUserException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
)

FailedToCreateMapException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="Не удалось создать карту"
)

FailedToCreatePiggyException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="Не удалось создать копилку"
)


CardAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Карта уже существует"
)

PiggyCardAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Копилка уже существует"
)


async def ExceptionDatabase(e, name):
    if isinstance(e, ValidationError):
        msg = f"Validation Error for Database {name}"
    elif isinstance(e, PyMongoError):
        msg = f"Mongo Error for Database in {name}"
    else:
        msg = f"Exception for Database in {name}"
    log.error(msg, exc_info=True)
