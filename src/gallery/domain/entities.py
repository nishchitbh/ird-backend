from pydantic import BaseModel

class GalleryBase(BaseModel):
    src: str
    alt: str
    caption: str