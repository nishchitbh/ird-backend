from src.areas_of_work.domain.entities import AreasOfWork, AreasOfWorkUpdate
from src.areas_of_work.domain.repositories import IAreasOfWorkRepository


class AreaServices:
    def __init__(self, area_repo: IAreasOfWorkRepository):
        self.area_repo = area_repo

    def verify_creation(self, content: AreasOfWork) -> AreasOfWork:
        if not content.initiativeName:
            raise ValueError("Initiative Name is required") 