from abc import ABC, abstractmethod
from src.flagship_programs.domain.entities import FlagshipProgram


class IFlagshipRepo(ABC):
    @abstractmethod
    def create(self, gallery: FlagshipProgram) -> dict:
        ...

    @abstractmethod
    def update(self, id: str, update_data: dict) -> dict:
        ...

    @abstractmethod
    def delete(self, id: str) -> dict:
        ...

    @abstractmethod
    def read(self, id: str) -> dict:
        ...

    @abstractmethod
    def read_all(self) -> dict:
        ...
