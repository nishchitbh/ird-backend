from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    username: EmailStr


class UserLogin(UserBase):
    password: str


class UserRegister(UserLogin):
    name: str
    position: Optional[str]
    education: Optional[str]


class UserStore(UserLogin):
    name: str
    position: Optional[str]
    education: Optional[str]
    approved: bool = False
    admin: bool = False
    created_at: datetime


class UserOut(UserBase):
    _id: str
    name: str
    position: Optional[str]
    education: Optional[str]
    approved: bool
    admin: bool
