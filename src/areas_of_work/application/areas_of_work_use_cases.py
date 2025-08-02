from src.areas_of_work.domain.entities import AreasOfWork, AreasOfWorkUpdate
from src.areas_of_work.domain.repositories import IAreaRepo
from src.areas_of_work.domain.services import AreaServices


class AreaUseCases:
    def __init__(self, area_repo: IAreaRepo, area_services: AreaServices):
        self.area_repo = area_repo
        self.area_services = area_services

    def create_area(self, content: AreasOfWork) -> AreasOfWork:
        self.area_services.verify_creation(content)
        return self.area_repo.create(content.model_dump())

    def update_area(
        self, area_id: str, content: AreasOfWorkUpdate
    ) -> AreasOfWork:
        update_data = content.model_dump()
        update_data = {k: v for k, v in update_data.items() if v is not None}
        message = self.area_repo.update(area_id, update_data)
        return message

    def delete_area(self, area_id: str) -> dict:
        return self.area_repo.delete(area_id)

    def get_one_area(self, area_id: str) -> dict:
        return self.area_repo.read(area_id)

    def get_all_areas(self) -> list:
        return self.area_repo.read_all()
