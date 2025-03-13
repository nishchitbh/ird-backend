from src.auth.domain.repositories.user_repo import IUserRepository
from src.shared.domain.repositories.data_repo import IDataRepo


class UserRepo(IUserRepository):
    def __init__(self, repo: IDataRepo):
        self.repo = repo

    def create(self, user: dict) -> dict:
        message = self.repo.create(user)
        return message

    def read(self, username: str) -> dict:
        return self.repo.read({"username": username})

    def update(self, username: str, update_data: dict) -> dict:
        return self.repo.update({"username": username}, update_data)

    def delete(self, username: str) -> dict:
        return self.repo.delete({"username": username})
