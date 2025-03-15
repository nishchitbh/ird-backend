from fastapi import Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from src.auth.application.auth_use_cases import AuthUseCases
from src.auth.presentation.config import auth_router, user_router, get_current_user, get_auth_use_cases
from src.auth.domain.entities.users_entity import UserOut, UserRegister, UserUpdate, ChangePassword, UserUpdateAdmin
from src.shared.domain.exceptions import AppException


@auth_router.post("/login", status_code=status.HTTP_200_OK)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    auth_use_cases: AuthUseCases = Depends(get_auth_use_cases)
):
    """
    Authenticates a user given their username and password.
    """
    try:
        return auth_use_cases.login(user_credentials.username, user_credentials.password)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@auth_router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def signup(
    user: UserRegister,
    auth_use_cases: AuthUseCases = Depends(get_auth_use_cases)
):
    """
    Creates a new user.
    """
    try:
        return auth_use_cases.signup(user)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@user_router.get("/me", response_model=UserOut, status_code=status.HTTP_200_OK)
def me(
    current_user: UserOut = Depends(get_current_user)
):
    """
    Returns the current user's information.
    """
    try:
        return current_user
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@user_router.patch("/me", response_model=UserOut, status_code=status.HTTP_200_OK)
def update_me(
    update_data: UserUpdate,
    current_user: UserOut = Depends(get_current_user),
    auth_use_cases: AuthUseCases = Depends(get_auth_use_cases)
):
    """
    Updates the current user's information.
    """
    try:
        return auth_use_cases.update_user(current_user, update_data)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@user_router.patch("/me/password", response_model=UserOut, status_code=status.HTTP_200_OK)
def change_password(
    password_data: ChangePassword,
    current_user: UserOut = Depends(get_current_user),
    auth_use_cases: AuthUseCases = Depends(get_auth_use_cases)
):
    """
    Changes the current user's password.
    """
    try:
        password = password_data.password
        new_password = password_data.new_password
        return auth_use_cases.change_password(current_user, password, new_password)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@user_router.delete("/", status_code=status.HTTP_200_OK)
def delete_user(
    username: str,
    current_user: UserOut = Depends(get_current_user),
    auth_use_cases: AuthUseCases = Depends(get_auth_use_cases)
):
    """
    Deletes a user.
    """
    try:
        return auth_use_cases.delete_user(username, current_user)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@user_router.post("/reset-password/", status_code=status.HTTP_200_OK)
def reset_password(
    username: str,
    current_user: UserOut = Depends(get_current_user),
    auth_use_cases: AuthUseCases = Depends(get_auth_use_cases)
):
    """
    Resets a user's password.
    """
    try:
        return auth_use_cases.reset_password(username, current_user)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@user_router.patch("/update-user/", status_code=status.HTTP_200_OK)
def update_other_user(
    username: str,
    update_data: UserUpdateAdmin,
    current_user: UserOut = Depends(get_current_user),
    auth_use_cases: AuthUseCases = Depends(get_auth_use_cases)
):
    """
    Updates a user.
    """
    try:
        return auth_use_cases.update_other_user(current_user, username, update_data)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
