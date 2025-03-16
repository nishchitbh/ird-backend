from src.auth.domain.entities.users_entity import UserOut
from src.auth.domain.services.auth_services import AuthService, UserService
from src.auth.infrastructure.user_repo_impl import UserRepo
from src.shared.infrastructure.data_repo_impl import MongoRepo
from src.auth.application.auth_use_cases import AuthUseCases
from src.shared.infrastructure.db_config import get_db
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer

auth_router = APIRouter(prefix="/auth", tags=["Auth"])
user_router = APIRouter(prefix="/user", tags=["User"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

def get_auth_use_cases():
    db = get_db()
    repo = MongoRepo(db=db, collection="users")
    user_repo = UserRepo(repo=repo)
    auth_services = AuthService(user_repo=user_repo)
    user_services = UserService(user_repo=user_repo)

    return AuthUseCases(user_repo=user_repo, auth_services=auth_services, user_services=user_services)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    auth_use_cases: AuthUseCases = Depends(get_auth_use_cases),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_payload = auth_use_cases.auth_services.verify_token(
        token, credentials_exception)
    user = auth_use_cases.user_repo.read(token_payload["username"])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserOut(**user)
