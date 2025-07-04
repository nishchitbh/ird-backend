from abc import ABC, abstractmethod
from src.event_list.domain.entities import EventList


class IEventListRepo(ABC):
    @abstractmethod
    def create(self, gallery: EventList) -> dict: ...

    @abstractmethod
    def update(self, id: str, update_data: dict) -> dict: ...

    @abstractmethod
    def delete(self, id: str) -> dict: ...

    @abstractmethod
    def read(self, id: str) -> dict: ...

    @abstractmethod
    def read_all(self) -> dict: ...
