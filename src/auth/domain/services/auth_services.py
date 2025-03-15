from src.auth.domain.repositories.user_repo import IUserRepository
from src.shared.config import setting
from src.auth.domain.entities.users_entity import UserStore
from datetime import datetime, timedelta
import jwt
from jwt import PyJWTError
from passlib.context import CryptContext


class AuthService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, plain_password: str) -> str:
        return self.pwd_context.hash(plain_password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=setting.access_token_expiry_time)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, setting.auth_secret, algorithm=setting.algorithm)

    def verify_token(self, token: str, credentials_exception) -> dict:
        try:
            payload = jwt.decode(token, setting.auth_secret,
                                 algorithms=[setting.algorithm])
            username = payload.get("username")
            if username is None:
                raise credentials_exception
            return payload
        except PyJWTError:
            raise credentials_exception


class UserService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def validate_user(self, user: UserStore):
        self.__check_missing_fields(user)
        self.__check_uniqueness(user)

    def __check_missing_fields(self, user: UserStore):
        missing_fields = [field for field in [
            "username", "password"] if not getattr(user, field)]
        if missing_fields:
            raise ValueError(f"Missing fields: {', '.join(missing_fields)}")

    def __check_uniqueness(self, user: UserStore):
        existing_user = self.user_repo.read(user.username)
        if existing_user:
            raise ValueError("User already exists")
