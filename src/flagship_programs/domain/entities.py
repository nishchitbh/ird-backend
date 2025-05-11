from pydantic import BaseModel
from typing import Optional, List


class FlagshipProgram(BaseModel):
    flagshipProgramsName: str
    flagshipProgramsDec: str
    flagshipProgramsImage: str
    link: str


class FlagshipProgramUpdate(BaseModel):
    flagshipProgramsName: Optional[str] = None
    flagshipProgramsDec: Optional[str] = None
    flagshipProgramsImage: Optional[str] = None
    link: Optional[str] = None


class FlagshipProgramResponse(BaseModel):
    data: FlagshipProgram


class FlagshipListResponse(BaseModel):
    data: List[FlagshipProgram]
