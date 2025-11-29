from .repositories import ISarathiRepo 
from .entities import SarathiMentee
class SarathiDomainService:

    def __init__(self, repo: ISarathiRepo):
        self.repo = repo

    def create_mentee(self, mentee: SarathiMentee) -> SarathiMentee:
        # Enforce uniqueness
        existing = self.repo.get_sarathi(mentee.name)
        if existing:
            raise ValueError(f"Mentee '{mentee.name}' already exists")

        return self.repo.add_sarathi(mentee)

    def update_mentee(self, mentee: SarathiMentee) -> SarathiMentee:
        # Optional rule: name cannot change
        existing = self.repo.get_sarathi(mentee.name)
        if not existing:
            raise ValueError(f"Mentee '{mentee.name}' does not exist")

        return self.repo.update_sarathi(mentee)

    def delete_mentee(self, name: str) -> None:
        self.repo.delete_sarathi(name)
