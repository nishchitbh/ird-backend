from src.flagship_programs.domain.entities import FlagshipProgram, FlagshipProgramUpdate
from src.shared.domain.exceptions import UnauthorizedException
from src.auth.domain.entities import UserOut
from src.flagship_programs.domain.repositories import IFlagshipRepo
from src.flagship_programs.domain.services import FlagshipService


class FlagshipUseCases:
    def __init__(
        self, flagship_programs_repo: IFlagshipRepo, flagship_services: FlagshipService
    ):
        self.repo = flagship_programs_repo
        self.services = flagship_services

    def create_flagship_programs(
        self, content: FlagshipProgram, current_user: UserOut
    ) -> FlagshipProgram:
        if not current_user.approved:
            raise UnauthorizedException("You cannot perform this action.")
        self.services.verify_creation(content)
        return self.repo.create(content.model_dump())

    def update_flagship_programs(
        self, id: str, content: FlagshipProgramUpdate, current_user: UserOut
    ) -> FlagshipProgram:
        if not current_user.approved:
            raise UnauthorizedException("You cannot perform this action.")
        update_data = content.model_dump()
        update_data = {k: v for k, v in update_data.items() if v is not None}
        message = self.repo.update(id, update_data)
        return message

    def delete_flagship_programs(self, id: str, current_user: UserOut) -> dict:
        if not current_user.approved:
            raise UnauthorizedException("You cannot perform this action.")
        return self.repo.delete(id)

    def get_one_flagship_programs(self, id: str) -> dict:
        return self.repo.read(id)

    def get_all_flagship_programs(self) -> list:
        return self.repo.read_all()
