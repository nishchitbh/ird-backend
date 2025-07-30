from src.flagship_programs.domain.entities import (
    FlagshipProgram,
    FlagshipProgramUpdate,
    FlagshipProgramResponse,
    FlagshipListResponse,
)
from src.flagship_programs.application.flagship_use_cases import FlagshipUseCases
from src.flagship_programs.presentation.config import flagship_programs_router
from src.flagship_programs.presentation.config import get_flagship_programse_cases
from src.auth.domain.entities import UserOut
from src.auth.presentation.config import get_current_user
from fastapi import status, Depends


@flagship_programs_router.get(
    "/", response_model=FlagshipListResponse, status_code=status.HTTP_200_OK
)
def get_all(use_cases: FlagshipUseCases = Depends(get_flagship_programse_cases)):
    """
    Gets all Join Us Programs.
    """
    result = use_cases.get_all_flagship_programs()
    return {"data": result}


@flagship_programs_router.get(
    "/{id}", response_model=FlagshipProgramResponse, status_code=status.HTTP_200_OK
)
def get_one(
    id: str, use_cases: FlagshipUseCases = Depends(get_flagship_programse_cases)
):
    """
    Gets one Join Us Program.
    """
    result = use_cases.get_one_flagship_programs(id)
    return {"data": result}


@flagship_programs_router.post(
    "/", response_model=FlagshipProgramResponse, status_code=status.HTTP_201_CREATED
)
def create(
    content: FlagshipProgram,
    current_user: UserOut = get_current_user("admin", "super"),
    use_cases: FlagshipUseCases = Depends(get_flagship_programse_cases),
):
    """
    Creates an Join Us Program.
    """
    result = use_cases.create_flagship_programs(content, current_user)
    return {"data": result}


@flagship_programs_router.patch(
    "/{id}", status_code=status.HTTP_201_CREATED, response_model=FlagshipProgramResponse
)
def update(
    id: str,
    content: FlagshipProgramUpdate,
    current_user: UserOut = get_current_user("admin", "super"),
    use_cases: FlagshipUseCases = Depends(get_flagship_programse_cases),
):
    """
    Updates an Join Us Program.
    """
    message = use_cases.update_flagship_programs(id, content, current_user)
    return {"data": message}


@flagship_programs_router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete(
    id: str,
    current_user: UserOut = get_current_user("admin", "super"),
    use_cases: FlagshipUseCases = Depends(get_flagship_programse_cases),
):
    """
    Deletes an Join Us Program.
    """
    return use_cases.delete_flagship_programs(id, current_user)
