# src/sarathi/presentation/routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from src.sarathi.presentation.config import get_sarathi_use_cases
from src.sarathi.application.sarathi_service import SarathiAppService
from src.sarathi.domain.entities import SarathiMentee

from src.auth.presentation.config import get_current_user
from src.auth.domain.entities import UserOut

sarathi_router = APIRouter(prefix="/sarathi", tags=["Sarathi"])

@sarathi_router.get("/", status_code=status.HTTP_200_OK)
def list_sarathi(
    service: SarathiAppService = Depends(get_sarathi_use_cases)
):
    return service.list_mentees()

@sarathi_router.get("/{name}", status_code=status.HTTP_200_OK)
def get_sarathi(
    name: str,
    service: SarathiAppService = Depends(get_sarathi_use_cases)
):
    mentee = service.get_mentee(name)
    return mentee

@sarathi_router.post("/", status_code=status.HTTP_201_CREATED)
def create_sarathi(
    data: SarathiMentee,
    current_user: UserOut = (get_current_user("admin", "super")),
    service: SarathiAppService = Depends(get_sarathi_use_cases)
):
    try:
        return service.create_mentee(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@sarathi_router.put("/", status_code=status.HTTP_200_OK)
def update_sarathi(
    data: SarathiMentee,
    current_user: UserOut = (get_current_user("admin", "super")),
    service: SarathiAppService = Depends(get_sarathi_use_cases)
):
    try:
        return service.update_mentee(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@sarathi_router.delete("/{name}", status_code=status.HTTP_200_OK)
def delete_sarathi(
    name: str,
    current_user: UserOut = (get_current_user("admin", "super")),
    service: SarathiAppService = Depends(get_sarathi_use_cases)
):
    return service.delete_mentee(name)

