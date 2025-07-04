from typing import List

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.auth.domain.entities import UserOut

from src.shared.infrastructure.db_config import get_db
from src.shared.domain.services import SharedServices
from src.auth.application.auth_flow import AuthUseCases
from src.auth.domain.repositories import IUserRepository
from src.auth.infrastructure.auth_repo import UserRepository
from src.auth.domain.services import AuthService, UserService
from src.shared.infrastructure.data_repo_impl import MongoRepo
from src.auth.application.abstract_auth_flow import IAuthUseCases
from src.shared.domain.exceptions import (
    AuthenticationFailedException,
    ForbiddenException,
)


bearer_scheme = HTTPBearer()

auth_router = APIRouter(prefix="/auth", tags=["Auth"])
user_router = APIRouter(prefix="/user", tags=["User"])


def get_auth_use_cases() -> IAuthUseCases:
    db = get_db()
    repo = MongoRepo(db=db, collection="users")
    user_repo: IUserRepository = UserRepository(repo=repo)
    auth_service = AuthService(user_repo=user_repo)
    user_service = UserService(user_repo=user_repo)
    return AuthUseCases(
        auth_service=auth_service,
        user_repo=user_repo,
        user_service=user_service,
        shared_service=SharedServices
    )


async def get_user_from_token(token: str, auth_use_cases: IAuthUseCases) -> UserOut:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = auth_use_cases.auth_service.verify_token(token, credentials_exception)
    user = auth_use_cases.user_repo.get_user_by_email(payload["sub"])
    if not user or user.soft_deleted:
        raise AuthenticationFailedException("Invalid email or password!")
    return UserOut(**user.model_dump())


def get_current_user(*required_role: List[str]):
    async def _get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
        auth_use_cases: IAuthUseCases = Depends(get_auth_use_cases),
    ) -> UserOut:
        user = await get_user_from_token(credentials.credentials, auth_use_cases)
        user_roles = [role for role in user.roles]
        if not set(required_role) & set(user_roles):
            raise ForbiddenException("Access denied!")
        return user

    return Depends(_get_current_user)
