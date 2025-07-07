from pydantic import BaseModel, EmailStr, ConfigDict

class Token(BaseModel):
    access_token: str
    token_type: str


class UserBase(BaseModel):
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class UserRead(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str



class UserInDB(UserBase):
    hashed_password: str