from abc import ABC, abstractmethod
from typing import List, Optional

class IAreasOfWorkRepository(ABC):
    @abstractmethod
    def create(self, initiative: dict) -> dict:
        pass

    @abstractmethod
    def read(self, initiative_id: str) -> Optional[dict]:
        pass

    @abstractmethod
    def read_all(self) -> List[dict]:
        pass

    @abstractmethod
    def update(self, initiative_id: str, update_data: dict) -> dict:
        pass

    @abstractmethod
    def delete(self, initiative_id: str) -> dict:
        pass
