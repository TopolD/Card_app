from beanie import Document
from pydantic import EmailStr

from app.dao.base import BaseDao


class ModelUser(Document):
    name: str
    phone_number: str
    password: str

    class Settings:
        name = "Users"


class UsersDao(BaseDao):
    model = ModelUser
