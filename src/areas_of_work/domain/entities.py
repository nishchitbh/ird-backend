from pydantic import BaseModel
from typing import List, Optional


class InitiativeList(BaseModel):
    initiativeListName: str
    initiativeListDesc: str
    initiativeListLink: str


class AreasOfWork(BaseModel):
    initiativeName: str
    initiativeDesc: str
    initiativeImage: str
    initiativeLists: List[InitiativeList]
    published: bool = False


class AreasOfWorkUpdate(BaseModel):
    initiativeName: Optional[str] = None
    initiativeDesc: Optional[str] = None
    initiativeImage: Optional[str] = None
    initiativeLists: Optional[List[InitiativeList]] = None
    published: Optional[bool] = None

