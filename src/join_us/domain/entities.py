from pydantic import BaseModel
from typing import Optional, List


class JoinUsProgram(BaseModel):
    programName: str
    programDesc: str
    programImage: str
    programLink: str


class JoinUsUpdate(BaseModel):
    programName: Optional[str] = None
    programDesc: Optional[str] = None
    programImage: Optional[str] = None
    programLink: Optional[str] = None


class JoinUsProgramResponse(BaseModel):
    data: JoinUsProgram


class JoinListResponse(BaseModel):
    data: List[JoinUsProgram]
