from app.dao.base import BaseDao
from odmantic import Model
from pydantic import EmailStr


class MUser(Model):
    name: str
    email: EmailStr
    password_hash: str


class UsersDao(BaseDao):
    model = MUser
