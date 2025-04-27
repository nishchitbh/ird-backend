from pydantic import BaseModel
from typing import Optional


class GalleryBase(BaseModel):
    src: str
    alt: str
    caption: Optional[str]


class GalleryOut(GalleryBase):
    _id: str


class GalleryUpdate(BaseModel):
    src: str
    alt: Optional[str]
    caption: Optional[str]
