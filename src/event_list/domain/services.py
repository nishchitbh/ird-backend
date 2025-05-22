from src.event_list.domain.entities import EventList
from src.event_list.domain.repositories import IEventListRepo


class EventListService:
    """
    Add services if needed
    """

    def __init__(self, repo: IEventListRepo):
        self.repo = repo

    def verify_creation(self, content: EventList) -> EventList:
        pass
