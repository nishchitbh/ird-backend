from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    username: EmailStr


class UserCreate(UserBase):
    password: str


class UserStore(UserCreate):
    name: str
    position: Optional[str]


class UserOut(UserBase):
    name: str
