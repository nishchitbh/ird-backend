from src.areas_of_work.domain.entities import (
    AreasOfWork,
    AreasOfWorkUpdate,
    AreasListResponse,
    AreasOfWorkResponse,
)
from src.areas_of_work.application.areas_of_work_use_cases import AreaUseCases
from src.areas_of_work.presentation.config import get_areas_of_work_use_cases
from src.areas_of_work.presentation.config import areas_router
from src.auth.domain.entities import UserOut
from src.auth.presentation.config import get_current_user
from fastapi import status, Depends


@areas_router.get("/", response_model=AreasListResponse, status_code=status.HTTP_200_OK)
def get_areas_of_work(use_cases: AreaUseCases = Depends(get_areas_of_work_use_cases)):
    """
    Gets all areas of work.
    """
    result = use_cases.get_all_areas()
    return {"data": result}


@areas_router.get(
    "/{area_id}", response_model=AreasOfWorkResponse, status_code=status.HTTP_200_OK
)
def get_one_area(
    area_id: str, use_cases: AreaUseCases = Depends(get_areas_of_work_use_cases)
):
    """
    Gets one area of work.
    """
    result = use_cases.get_one_area(area_id)
    return {"data": result}


@areas_router.post(
    "/", response_model=AreasOfWorkResponse, status_code=status.HTTP_201_CREATED
)
def create_area(
    content: AreasOfWork,
    current_user: UserOut = get_current_user("admin", "super"),
    use_cases: AreaUseCases = Depends(get_areas_of_work_use_cases),
):
    """
    Creates an area of work.
    """
    result = use_cases.create_area(content, current_user)
    return {"data": result}


@areas_router.patch(
    "/{area_id}",
    status_code=status.HTTP_201_CREATED,
    response_model=AreasOfWorkResponse,
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
    message = use_cases.update_area(area_id, content, current_user)
    return {"data": message}


@areas_router.delete("/{area_id}", status_code=status.HTTP_200_OK)
def delete_area(
    area_id: str,
    current_user: UserOut = get_current_user("admin", "super"),
    use_cases: AreaUseCases = Depends(get_areas_of_work_use_cases),
):
    """
    Deletes an area of work.
    """
    return use_cases.delete_area(area_id, current_user)
