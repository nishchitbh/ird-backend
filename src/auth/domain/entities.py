from pydantic import BaseModel, EmailStr, Field, field_validator
from src.shared.domain.exceptions import PasswordValidationException
from typing import Annotated, TypeAlias
from src.shared.config import setting
from typing import Optional, List
from datetime import datetime
from enum import Enum
import re


class Role(str, Enum):
    SUPER = "super"
    ADMIN = "admin"
    MAKER = "maker"
    CHECKER = "checker"
    VIEWER = "viewer"
    USER = "user"


DOMAIN = re.escape(setting.company_domain)

CompanyEmail: TypeAlias = Annotated[
    EmailStr,
    Field(
        pattern=rf"^[A-Za-z0-9._%+-]+@{DOMAIN}$",
        description="must be company domain",
    ),
]


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    must_change_password: bool


class UserBase(BaseModel):
    full_name: str
    email: CompanyEmail
    education: str
    roles: List[Role]


class UserCreate(UserBase): ...


class UserOut(UserBase):
    created_at: datetime
    updated_at: Optional[datetime] = None
    last_login_at: Optional[datetime] = None


class Pagination(BaseModel):
    page: int
    items: int


class UsersOut(BaseModel):
    users: List[UserOut]
    pagination: Pagination


class UserLogin(BaseModel):
    email: CompanyEmail
    password: str


class AddPassword(BaseModel):
    current_password: str
    new_password: str = Field(
        ...,
        min_length=8,
        description=(
            "New password must be at least 8 characters long and contain at least one "
            "uppercase letter, one lowercase letter, one digit, and one special character"
        ),
    )
    confirm_new_password: str

    @field_validator("new_password")
    @classmethod
    def validate_password(cls, pw: str) -> str:
        errors = []
        if not re.search(r"[a-z]", pw):
            errors.append("one lowercase letter")
        if not re.search(r"[A-Z]", pw):
            errors.append("one uppercase letter")
        if not re.search(r"\d", pw):
            errors.append("one digit")
        if not re.search(r"[\W_]", pw):
            errors.append("one special character")
        if errors:
            raise PasswordValidationException(
                f"Password must contain at least {', '.join(errors)}"
            )
        return pw


class UserStore(UserBase):
    password: str
    roles: List[str]
    generated_password: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    last_login_at: Optional[datetime] = None
    soft_deleted: Optional[bool] = None


class UserUpdateBase(BaseModel):
    full_name: Optional[str] = None
    email: Optional[CompanyEmail] = None
    education: Optional[str] = None
    roles: Optional[List[str]] = None


class UserUpdate(UserUpdateBase): ...


class LastLoginUpdate(BaseModel):
    last_login_at: datetime


class FullUpdate(UserUpdateBase):
    password: Optional[str] = None
    generated_password: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    last_login_at: Optional[datetime] = None
    soft_deleted: Optional[bool] = None
