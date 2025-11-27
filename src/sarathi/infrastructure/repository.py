from typing import Optional, List
from bson import ObjectId

from src.shared.domain.repositories.data_repo import IDataRepo
from src.shared.domain.exceptions import NotFoundException

from src.sarathi.domain.repositories import ISarathiRepo
from src.sarathi.domain.services import SarathiMentee


class SarathiRepo(ISarathiRepo):
    """
    Infrastructure repository for SarathiMentee.
    Uses IDataRepo underneath (Mongo wrapper).
    """

    def __init__(self, repo: IDataRepo):
        self.repo = repo

    # -----------------------------
    # CREATE
    # -----------------------------
    def add_sarathi(self, data: SarathiMentee) -> SarathiMentee:
        payload = data.model_dump()
        created = self.repo.create(payload)
        return SarathiMentee(**created)

    # -----------------------------
    # READ (single)
    # -----------------------------
    def get_sarathi(self, name: str) -> Optional[SarathiMentee]:
        result = self.repo.read({"name": name})
        if not result:
            return None
        return SarathiMentee(**result)

    # -----------------------------
    # READ (all)
    # -----------------------------
    def list_sarathi(self) -> List[SarathiMentee]:
        results = self.repo.read_all()
        return [SarathiMentee(**doc) for doc in results]

    # -----------------------------
    # UPDATE
    # -----------------------------
    def update_sarathi(self, sarathi: SarathiMentee) -> SarathiMentee:
        filter_q = {"name": sarathi.name}
        update_q = sarathi.model_dump()

        updated = self.repo.update(filter_q, update_q)
        if not updated:
            raise NotFoundException(f"Sarathi '{sarathi.name}' not found")

        return SarathiMentee(**updated)

    # -----------------------------
    # DELETE
    # -----------------------------
    def delete_sarathi(self, name: str) -> None:
        deleted = self.repo.delete({"name": name})
        if not deleted:
            raise NotFoundException(f"Sarathi '{name}' not found")
