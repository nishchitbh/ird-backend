from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from bson import ObjectId


class GalleryBase(BaseModel):
    alt: str
    caption: Optional[str]


class GalleryOut(GalleryBase):
    id: str = Field(..., alias="_id")
    src: str

    model_config = {
        "populate_by_name": True,
    }

    @field_validator("id", mode="before")
    @classmethod
    def _convert_objectid(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v


class GalleryList(BaseModel):
    data: List[GalleryOut]
    model_config = {"populate_by_name": True}


class GalleryStore(GalleryBase):
    src: str


class GalleryUpdate(BaseModel):
    src: Optional[str] = None
    alt: Optional[str] = None
    caption: Optional[str] = None


class GalleryUpload(GalleryBase):
    pass
