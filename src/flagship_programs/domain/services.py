from src.flagship_programs.domain.entities import FlagshipProgram, FlagshipProgramUpdate
from src.flagship_programs.domain.repositories import IFlagshipRepo


class FlagshipService:
    """
    Add services if needed
    """

    def __init__(self, repo: IFlagshipRepo):
        self.repo = repo

    def verify_creation(self, content: FlagshipProgram) -> FlagshipProgram:
        pass
