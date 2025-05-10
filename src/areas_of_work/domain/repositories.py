from abc import ABC, abstractmethod
from src.areas_of_work.domain.entities import AreasOfWork


class IAreaRepo(ABC):
    @abstractmethod
    def create(self, gallery: AreasOfWork) -> dict:
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
