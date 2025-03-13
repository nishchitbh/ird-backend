from src.auth.application.auth_use_cases import AuthUseCases
from src.auth.presentation.config import auth_router, user_router, get_current_user, get_auth_use_cases
from src.auth.domain.entities.users_entity import UserOut, UserRegister
from fastapi import Depends, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


@auth_router.post("/login", response_model=UserOut, status_code=status.HTTP_200_OK)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), auth_use_cases: AuthUseCases = Depends(get_auth_use_cases)):
    """
    Authenticates a user given their username and password.

    Args:
        user_credentials: the user's credentials, passed in the request body
        auth_use_cases: the auth use cases, injected by FastAPI

    Returns:
        the authenticated user
    """
    return auth_use_cases.login(user_credentials.username, user_credentials.password)


@auth_router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def signup(user: UserRegister, auth_use_cases: AuthUseCases = Depends(get_auth_use_cases)):
    """
    Creates a new user.

    Args:
        user: the user to create, passed in the request body
        auth_use_cases: the auth use cases, injected by FastAPI

    Returns:
        the created user
    """
    return auth_use_cases.signup(user)
