from pydantic import BaseModel
from typing import Optional,List

class SarathiMentee(BaseModel):
    name : str
    description : str
    image : str 