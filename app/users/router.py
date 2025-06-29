from fastapi import APIRouter


from app.exceptions import UserAlreadyExistsExceptions

from app.users.dao import UsersDao,MUser
from app.users.schemas import User,SUserAuth
from app.users.auth import get_password_hash
router = APIRouter(
    prefix="/auth",
    tags=["Auth "]
)


# @router.post("/register", response_model=User)
# async def register_user(user_data: SUserAuth):
#     existing_user = await UsersDao.find_one_or_none({'email': user_data.email})
#     if existing_user:
#         raise UserAlreadyExistsExceptions
#
#     hashed_password = get_password_hash(user_data.password)
#     await UsersDao.add_item(SUser(
#         name = user_data.name,
#         email=user_data.email,
#         password_hash=hashed_password,
#     ))
