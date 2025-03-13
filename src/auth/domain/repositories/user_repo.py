from abc import ABC, abstractmethod


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