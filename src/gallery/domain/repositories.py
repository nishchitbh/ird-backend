from abc import ABC, abstractmethod
from src.gallery.domain.entities import GalleryStore


class IGalleryRepo(ABC):
    @abstractmethod
    def create(self, gallery: GalleryStore) -> dict: ...

    @abstractmethod
    def update(self, id: str, update_data: dict) -> dict: ...

    @abstractmethod
    def delete(self, id: str) -> dict: ...

    @abstractmethod
    def read(self, id: str) -> dict: ...

    @abstractmethod
    def read_all(self) -> dict: ...
