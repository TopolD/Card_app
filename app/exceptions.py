
from fastapi import HTTPException,status

UserAlreadyExistsExceptions = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует",
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail= 'Неверная почта или пароль',
)
TokenExpiredException = HTTPException(
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail='Токен истек',
)

TokeAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен отсутствует",
)


IncorrectTokenFormaException  = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат токена",
)

UserIsNotPresentHTTPException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
)


InactiveUserException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail = 'Inactive user',
)

FailedToCreateMapException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail = 'Не удалось создать карту'
)

FailedToCreatePiggyException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail = 'Не удалось создать копилку'
)



CardAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail= "Карта уже существует"
)

PiggyCardAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail= "Копилка уже существует"
)
