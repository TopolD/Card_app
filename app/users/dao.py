from app.dao.base import BaseDao
from beanie import Document
from pydantic import EmailStr


class ModelUser(Document):
    name: str
    email: EmailStr
    password: str


    class Settings:
        name = "Users"

class UsersDao(BaseDao):
    model = ModelUser
