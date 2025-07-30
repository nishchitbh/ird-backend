from src.gallery.domain.entities import (
    GalleryOut,
    GalleryUpload,
    GalleryList,
    GalleryUpdate,
)
from fastapi import status, UploadFile, File, Query, Depends, HTTPException
from src.gallery.application.gallery_use_cases import GalleryUseCases
from src.gallery.presentation.config import get_gallery_use_cases
from src.gallery.presentation.config import gallery_router
from src.auth.domain.entities import UserOut
from src.auth.presentation.config import get_current_user
from src.shared.domain.exceptions import AppException
from typing import Optional


@gallery_router.post(
    "/upload", status_code=status.HTTP_201_CREATED, response_model=GalleryOut
)
async def upload_photo(
    alt: str = Query(..., description="Alt"),
    caption: Optional[str] = Query(None, description="Caption"),
    file: UploadFile = File(...),
    gallery_use_cases: GalleryUseCases = Depends(get_gallery_use_cases),
    current_user: UserOut = get_current_user("admin", "super"),
):
    try:
        gallery_data = GalleryUpload(
            alt=alt,
            caption=caption,
        )
        message = await gallery_use_cases.create_gallery(
            file=file, current_user=current_user, gallery=gallery_data
        )
        return message
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@gallery_router.get(
    "/gallery", status_code=status.HTTP_200_OK, response_model=GalleryList
)
async def get_gallery(
    gallery_use_cases: GalleryUseCases = Depends(get_gallery_use_cases),
):
    try:
        raw = gallery_use_cases.read_all()
        items = [{**d, "_id": str(d["_id"])} for d in raw]
        return {"data": items}
    except AppException as e:
        return HTTPException(status_code=e.status_code, detail=e.detail)


@gallery_router.get(
    "/gallery/{gallery_id}", status_code=status.HTTP_200_OK, response_model=GalleryOut
)
async def get_gallery_by_id(
    gallery_id: str,
    gallery_use_cases: GalleryUseCases = Depends(get_gallery_use_cases),
):
    try:
        raw = gallery_use_cases.read_gallery(gallery_id)
        return {**raw, "_id": str(raw["_id"])}
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@gallery_router.patch(
    "/gallery/{gallery_id}", status_code=status.HTTP_200_OK, response_model=GalleryOut
)
async def update_gallery_by_id(
    gallery_id: str,
    gallery_data: GalleryUpdate,
    gallery_use_cases: GalleryUseCases = Depends(get_gallery_use_cases),
    current_user: UserOut = get_current_user("admin", "super"),
):
    try:
        return gallery_use_cases.update_gallery(
            gallery_id=gallery_id, gallery=gallery_data, current_user=current_user
        )
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@gallery_router.delete("/gallery/{gallery_id}", status_code=status.HTTP_200_OK)
async def delete_gallery_by_id(
    gallery_id: str,
    gallery_use_cases: GalleryUseCases = Depends(get_gallery_use_cases),
    current_user: UserOut = get_current_user("admin", "super"),
):
    try:
        return gallery_use_cases.delete_gallery(
            current_user=current_user, gallery_id=gallery_id
        )
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
