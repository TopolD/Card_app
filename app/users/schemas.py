from pydantic import BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserBase(BaseModel):
    name: str
    phone_number: PhoneNumber

    model_config = ConfigDict(from_attributes=True)


class UserRead(BaseModel):
    name: str
    phone_number: PhoneNumber


class UserCreate(UserBase):
    password: str


class UserInDB(UserBase):
    password: str


class UserLogin(BaseModel):
    phone_number: PhoneNumber
    password: str
