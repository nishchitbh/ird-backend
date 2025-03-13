from abc import ABC, abstractmethod


class IDataRepo(ABC):
    @abstractmethod
    def handle_error(self, exception: Exception) -> dict:
        ...

    @abstractmethod
    def create(self, data: dict) -> dict:
        ...

    @abstractmethod
    def read(self, identifier: dict) -> dict:
        ...

    @abstractmethod
    def update(self, identifier: dict, update_data: dict) -> dict:
        ...

    @abstractmethod
    def delete(self, identifier: dict) -> dict:
        ...
