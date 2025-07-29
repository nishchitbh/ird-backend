from src.join_us.domain.entities import (
    JoinUsProgram,
    JoinUsUpdate,
    JoinUsProgramResponse,
    JoinListResponse,
)
from src.join_us.application.join_us_use_cases import JoinUsUseCases
from src.join_us.presentation.config import get_join_use_cases
from src.join_us.presentation.config import join_us_router
from src.auth.domain.entities import UserOut
from src.auth.presentation.config import get_current_user
from fastapi import status, Depends


@join_us_router.get(
    "/", response_model=JoinListResponse, status_code=status.HTTP_200_OK
)
def get_all(use_cases: JoinUsUseCases = Depends(get_join_use_cases)):
    """
    Gets all Join Us Programs.
    """
    result = use_cases.get_all_join_us()
    return {"data": result}


@join_us_router.get(
    "/{id}", response_model=JoinUsProgramResponse, status_code=status.HTTP_200_OK
)
def get_one(id: str, use_cases: JoinUsUseCases = Depends(get_join_use_cases)):
    """
    Gets one Join Us Program.
    """
    result = use_cases.get_one_join_us(id)
    return {"data": result}


@join_us_router.post(
    "/", response_model=JoinUsProgramResponse, status_code=status.HTTP_201_CREATED
)
def create(
    content: JoinUsProgram,
    current_user: UserOut = Depends(get_current_user),
    use_cases: JoinUsUseCases = Depends(get_join_use_cases),
):
    """
    Creates an Join Us Program.
    """
    result = use_cases.create_join_us(content, current_user)
    return {"data": result}


@join_us_router.patch(
    "/{id}", status_code=status.HTTP_201_CREATED, response_model=JoinUsProgramResponse
)
def update(
    id: str,
    content: JoinUsUpdate,
    current_user: UserOut = Depends(get_current_user),
    use_cases: JoinUsUseCases = Depends(get_join_use_cases),
):
    """
    Updates an Join Us Program.
    """
    message = use_cases.update_join_us(id, content, current_user)
    return {"data": message}


@join_us_router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete(
    id: str,
    current_user: UserOut = Depends(get_current_user),
    use_cases: JoinUsUseCases = Depends(get_join_use_cases),
):
    """
    Deletes an Join Us Program.
    """
    return use_cases.delete_join_us(id, current_user)
