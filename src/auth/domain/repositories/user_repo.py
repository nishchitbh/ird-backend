from abc import ABC, abstractmethod
from typing import List


class IUserRepository(ABC):

    @abstractmethod
    def create(user: dict) -> dict:  # Returns UserOut in case of
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
