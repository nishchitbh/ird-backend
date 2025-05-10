from src.areas_of_work.domain.entities import AreasOfWork, AreasOfWorkUpdate
from src.areas_of_work.domain.repositories import IAreaRepo


class AreaServices:
    def __init__(self, area_repo: IAreaRepo):
        self.area_repo = area_repo

    def verify_creation(self, content: AreasOfWork) -> AreasOfWork:
        pass
