from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime
import re
from src.shared.domain.exceptions import PasswordValidationException


class UserBase(BaseModel):
    username: EmailStr


class UserLogin(UserBase):
    password: str

    @field_validator('password')
    def validate_new_password(cls, value):
        if not re.search(r'[A-Z]', value):
            raise PasswordValidationException(
                'New password must contain at least one uppercase letter')
        if not re.search(r'[0-9]', value):
            raise PasswordValidationException(
                'New password must contain at least one number')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise PasswordValidationException(
                'New password must contain at least one special character')
        if len(value) < 8:
            raise PasswordValidationException(
                'New password must be at least 8 characters long')
        return value


class UserRegister(UserLogin):
    name: str
    position: Optional[str]
    education: Optional[str]


class UserStore(UserRegister):
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


class UserUpdate(BaseModel):
    name: Optional[str] = None
    position: Optional[str] = None
    education: Optional[str] = None


class ChangePassword(BaseModel):
    password: str
    new_password: str

    @field_validator('new_password')
    def validate_new_password(cls, value):
        if not re.search(r'[A-Z]', value):  # At least one uppercase letter
            raise ValueError(
                'New password must contain at least one uppercase letter')
        if not re.search(r'[0-9]', value):  # At least one number
            raise ValueError('New password must contain at least one number')
        # At least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValueError(
                'New password must contain at least one special character')
        if len(value) < 8:  # Password length must be at least 8 characters
            raise ValueError('New password must be at least 8 characters long')
        return value
