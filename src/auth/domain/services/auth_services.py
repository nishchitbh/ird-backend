from src.auth.domain.repositories.user_repo import IUserRepository
from src.shared.config import setting
from src.auth.domain.entities.users_entity import UserStore
from datetime import datetime, timedelta
import jwt
from jwt import PyJWTError
from passlib.context import CryptContext
import random
import string


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

    def generate_password(self) -> str:
        # Define possible character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Ensure the password has at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 symbol
        password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(digits),
            random.choice(symbols)
        ]

        # Fill the remaining characters to make the password 8 characters long
        remaining_characters = random.choices(lowercase + uppercase + digits + symbols, k=4)

        # Add the remaining characters to the password list
        password.extend(remaining_characters)

        # Shuffle the list to make the password random
        random.shuffle(password)

        # Join the list into a string and return the password
        return ''.join(password)

class UserService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def validate_user(self, user: UserStore):
        self.__check_uniqueness(user)
    def __check_uniqueness(self, user: UserStore):
        existing_user = self.user_repo.read(user.username)
        if existing_user:
            raise ValueError("User already exists")
