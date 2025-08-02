from typing import List
from src.areas_of_work.domain.entities import (
    AreasOfWork,
    AreasOfWorkUpdate,
)
from src.areas_of_work.application.areas_of_work_use_cases import AreaUseCases
from src.areas_of_work.presentation.config import get_areas_of_work_use_cases
from src.areas_of_work.presentation.config import areas_router
from src.auth.domain.entities import UserOut
from src.auth.presentation.config import get_current_user
from fastapi import status, Depends


@areas_router.get("/", response_model=List[AreasOfWork], status_code=status.HTTP_200_OK)
def get_areas_of_work(use_cases: AreaUseCases = Depends(get_areas_of_work_use_cases)):
    """
    Gets all areas of work.
    """
    result = use_cases.get_all_areas()
    return result


@areas_router.get(
    "/{area_id}", response_model=AreasOfWork, status_code=status.HTTP_200_OK
)
def get_one_area(
    area_id: str, use_cases: AreaUseCases = Depends(get_areas_of_work_use_cases)
):
    """
    Gets one area of work.
    """
    result = use_cases.get_one_area(area_id)
    return result


@areas_router.post(
    "/", response_model=AreasOfWork, status_code=status.HTTP_201_CREATED
)
def create_area(
    content: AreasOfWork,
    current_user: UserOut = get_current_user("admin", "super"),
    use_cases: AreaUseCases = Depends(get_areas_of_work_use_cases),
):
    """
    Creates an area of work.
    """
    result = use_cases.create_area(content)
    return result


@areas_router.patch(
    "/{area_id}",
    status_code=status.HTTP_201_CREATED,
    response_model=AreasOfWork,
)
def update_area(
    area_id: str,
    content: AreasOfWorkUpdate,
    current_user: UserOut = get_current_user("admin", "super"),
    use_cases: AreaUseCases = Depends(get_areas_of_work_use_cases),
):
    """
    Updates an area of work.
    """
    result = use_cases.update_area(area_id, content)
    return result


@areas_router.delete("/{area_id}", status_code=status.HTTP_200_OK)
def delete_area(
    area_id: str,
    current_user: UserOut = get_current_user("admin", "super"),
    use_cases: AreaUseCases = Depends(get_areas_of_work_use_cases),
):
    """
    Deletes an area of work.
    """
    return use_cases.delete_area(area_id)
