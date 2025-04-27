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


class IScraper(ABC):
    @abstractmethod
    def scrape_shortcodes(self, username: str) -> list:
        ...

    @abstractmethod
    def scrape_posts(self, shortcode: str) -> dict:
        ...
