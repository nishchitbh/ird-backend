from src.auth.domain.services.auth_services import AuthService, UserService
from src.auth.domain.repositories.user_repo import IUserRepository
from src.auth.domain.entities.users_entity import UserRegister, UserStore
from fastapi import HTTPException
from datetime import datetime


class AuthUseCases:
    def __init__(self, user_repo: IUserRepository, auth_services: AuthService, user_services: UserService):
        self.user_repo = user_repo
        self.auth_services = auth_services
        self.user_services = user_services

    def signup(self, user: UserRegister) -> dict:
        try:
            now = datetime.utcnow()
            self.user_services.validate_user(user)
            hashed_password = self.auth_services.hash_password(user.password)
            user.password = hashed_password
            user = UserStore(**user.dict(), created_at=now)
            return self.user_repo.create(user.model_dump())
        except ValueError as e:
            raise HTTPException(
                status_code=400, detail=f"Invalid user data: {str(e)}.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def login(self, username: str, password: str) -> dict:
        user = self.user_repo.read(username)
        print(user)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials.")
        if not self.auth_services.verify_password(password, user["password"]):
            raise HTTPException(status_code=401, detail="Invalid credentials.")
        token = self.auth_services.create_access_token({"username": username})
        return {"token": token, "token_type": "bearer"}

    def delete_user(self, username: str) -> dict:
        return self.user_repo.delete(username)

    def change_password(self, username: str, password: str, new_password: str) -> dict:
        user = self.user_repo.read(username)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials.")
        if not self.auth_services.verify_password(password, user["password"]):
            raise HTTPException(status_code=401, detail="Invalid credentials.")
        hashed_password = self.auth_services.hash_password(new_password)
        return self.user_repo.update(username, {"password": hashed_password})

    def update_user(self, username: str, update_data: dict) -> dict:
        return self.user_repo.update(username, update_data)
