from abc import ABC, abstractmethod
from typing import List
from src.auth.domain.entities.users_entity import UserStore


class IUserRepository(ABC):

    @abstractmethod
    def create(user: UserStore) -> dict:  # Returns UserOut in case of
        ...

    @abstractmethod
    def read(username: str) -> dict:
        ...

    @abstractmethod
    def update(username: str) -> dict:
        ...

    @abstractmethod
    def delete(username: str) -> dict:
        ...

    @abstractmethod
    def get_all() -> List:
        ...
