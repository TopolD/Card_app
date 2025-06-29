from pydantic import BaseModel, EmailStr, ConfigDict

class User(BaseModel):
    name: str
    email: EmailStr


class SUserAuth(BaseModel):
    name: str
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True)