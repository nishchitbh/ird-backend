from datetime import datetime
from src.auth.domain.services.auth_services import AuthService, UserService
from src.auth.domain.repositories.user_repo import IUserRepository
from src.auth.domain.entities.users_entity import UserRegister, UserStore, UserOut, UserUpdate, UserUpdateAdmin
from src.shared.domain.exceptions import (
    ItemNotFoundException,
    AuthenticationFailedException,
    InvalidUpdateException,
    UserAlreadyExistsException,
    UnauthorizedException
)


class AuthUseCases:
    def __init__(self, user_repo: IUserRepository, auth_services: AuthService, user_services: UserService):
        self.user_repo = user_repo
        self.auth_services = auth_services
        self.user_services = user_services

    def signup(self, user: UserRegister) -> dict:
        if self.user_repo.read(user.username):
            raise UserAlreadyExistsException(
                f"User with username {user.username} already exists")
        now = datetime.utcnow()
        self.user_services.validate_user(user)
        hashed_password = self.auth_services.hash_password(user.password)
        user.password = hashed_password
        user = UserStore(**user.dict(), created_at=now)
        return self.user_repo.create(user.model_dump())

    def login(self, username: str, password: str) -> dict:
        user = self.user_repo.read(username)
        if not user or not self.auth_services.verify_password(password, user["password"]):
            raise AuthenticationFailedException(
                "Incorrect username or password")
        token = self.auth_services.create_access_token({"username": username})
        return {"access_token": token, "token_type": "bearer"}

    def delete_user(self, username: str, current_user: UserOut) -> dict:
        if not current_user.admin:
            raise UnauthorizedException("You cannot perform this action.")
        if not self.user_repo.read(username):
            raise ItemNotFoundException(
                f"User with username {username} not found")
        return self.user_repo.delete(username)

    def change_password(self, current_user: UserOut, password: str, new_password: str) -> dict:
        username = current_user.username
        user = self.user_repo.read(username)
        if not self.auth_services.verify_password(password, user["password"]):
            raise AuthenticationFailedException("Incorrect password")
        hashed_password = self.auth_services.hash_password(new_password)
        data = self.user_repo.update(username, {"password": hashed_password})
        return {
            "status": "ok",
            "message": "Password changed successfully",
            "username": data["username"]
        }

    def update_user(self, current_user: UserOut, update_data: UserUpdate) -> dict:
        username = current_user.username
        update_data = update_data.model_dump()
        update_data = {k: v for k, v in update_data.items() if v is not None}
        if "password" in update_data.keys():
            raise InvalidUpdateException(
                "Cannot update password. Use reset password instead.")
        return self.user_repo.update(username, update_data)

    def reset_password(self, username: str, current_user: UserOut) -> dict:
        if not current_user.admin:
            raise UnauthorizedException("You cannot perform this action.")
        if not self.user_repo.read(username):
            raise ItemNotFoundException(
                f"User with username {username} not found")
        new_password = self.auth_services.generate_password()
        hashed_password = self.auth_services.hash_password(new_password)
        data = self.user_repo.update(username, {"password": hashed_password})
        return {
            "status": "ok",
            "message": "Password reset successfully",
            "username": data["username"],
            "new_password": new_password
        }

    def update_other_user(self, current_user: UserOut, username: str, update_data: UserUpdateAdmin) -> dict:
        if not current_user.admin:
            raise UnauthorizedException("You cannot perform this action.")
        update_data = update_data.model_dump()
        update_data = {k: v for k, v in update_data.items() if v is not None}
        if not self.user_repo.read(username):
            raise ItemNotFoundException(
                f"User with username {username} not found")
        result = self.user_repo.update(username, update_data)
        return {
            "status": "ok",
            "message": "User updated successfully",
            "username": result["username"]}
