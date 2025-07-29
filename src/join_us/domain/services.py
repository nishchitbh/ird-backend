from src.join_us.domain.entities import JoinUsProgram
from src.join_us.domain.repositories import IJoinUsRepo


class JoinUsServices:
    def __init__(self, repo: IJoinUsRepo):
        self.repo = repo

    def verify_creation(self, content: JoinUsProgram) -> JoinUsProgram:
        pass
