from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class EventList(BaseModel):
    eventName: str
    eventImage: str
    eventDate: datetime
    eventTag: str
    registerLink: str
    eventDisc: str


class EventListUpdate(BaseModel):
    eventName: Optional[str] = None
    eventImage: Optional[str] = None
    eventDate: Optional[datetime] = None
    eventTag: Optional[str] = None
    registerLink: Optional[str] = None
    eventDisc: Optional[str] = None


class EventLists(BaseModel):
    eventLists: List[EventList]
