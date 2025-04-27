from abc import ABC, abstractmethod
from src.gallery.domain.entities import Gallery


class IGalleryRepo(ABC):
    @abstractmethod
    def create(self, gallery: Gallery) -> dict:
        ...

    @abstractmethod
    def update(self, id: str) -> dict:
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