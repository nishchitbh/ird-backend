from src.join_us.domain.entities import JoinUsProgram, JoinUsUpdate
from src.join_us.domain.repositories import IJoinUsRepo
from src.join_us.domain.services import JoinUsServices


class JoinUsUseCases:
    def __init__(self, join_us_repo: IJoinUsRepo, join_services: JoinUsServices):
        self.repo = join_us_repo
        self.services = join_services

    def create_join_us(
        self, content: JoinUsProgram,
    ) -> JoinUsProgram:
        self.services.verify_creation(content)
        return self.repo.create(content.model_dump())

    def update_join_us(
        self, id: str, content: JoinUsUpdate,
    ) -> JoinUsProgram:
        update_data = content.model_dump()
        update_data = {k: v for k, v in update_data.items() if v is not None}
        message = self.repo.update(id, update_data)
        return message

    def delete_join_us(self, id: str,) -> dict:
        return self.repo.delete(id)

    def get_one_join_us(self, id: str) -> dict:
        return self.repo.read(id)

    def get_all_join_us(self) -> list:
        return self.repo.read_all()
