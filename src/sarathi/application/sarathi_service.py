# src/sarathi/application/services.py

from typing import List
from src.sarathi.domain.entities import SarathiMentee
from src.sarathi.domain.repositories import ISarathiRepo
from src.sarathi.domain.services import SarathiDomainService


class SarathiAppService:

    def __init__(self, repo: ISarathiRepo):
        self.repo = repo
        self.domain = SarathiDomainService(repo)

    # -------------------------------------------------
    # CREATE
    # -------------------------------------------------
    def create_mentee(self, data: SarathiMentee) -> SarathiMentee:
        # Domain handles validation (e.g., uniqueness)
        return self.domain.create_mentee(data)

    # -------------------------------------------------
    # READ ONE
    # -------------------------------------------------
    def get_mentee(self, name: str) -> SarathiMentee:
        mentee = self.repo.get_sarathi(name)
        if not mentee:
            # App-level error; domain doesn't care about this rule
            raise ValueError(f"Mentee '{name}' not found")
        return mentee

    # -------------------------------------------------
    # READ ALL
    # -------------------------------------------------
    def list_mentees(self) -> List[SarathiMentee]:
        return self.repo.list_sarathi()

    # -------------------------------------------------
    # UPDATE
    # -------------------------------------------------
    def update_mentee(self, data: SarathiMentee) -> SarathiMentee:
        # Domain can enforce rules (like immutable name)
        return self.domain.update_mentee(data)

    # -------------------------------------------------
    # DELETE
    # -------------------------------------------------
    def delete_mentee(self, name: str) -> None:
        return self.domain.delete_mentee(name)
