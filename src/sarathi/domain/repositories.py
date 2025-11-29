# src/sarathi/domain/repositories.py
from abc import ABC, abstractmethod
from typing import List, Optional
from .entities import SarathiMentee

class ISarathiRepo(ABC):
    
    @abstractmethod
    def add_sarathi(self, data: SarathiMentee) -> SarathiMentee:
        """Add a new Sarathi"""
        pass

    @abstractmethod
    def get_sarathi(self, name: str) -> Optional[SarathiMentee]:
        """Get a Sarathi by name"""
        pass

    @abstractmethod
    def list_sarathi(self) -> List[SarathiMentee]:
        """Return all Sarathi"""
        pass

    @abstractmethod
    def update_sarathi(self, sarathi: SarathiMentee) -> SarathiMentee:
        """Update an existing Sarathi"""
        pass

    @abstractmethod
    def delete_sarathi(self, name: str) -> None:
        """Delete a Sarathi by name"""
        pass
