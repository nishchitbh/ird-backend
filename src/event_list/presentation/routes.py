from src.event_list.presentation.config import event_list_router, get_event_list_cases
from src.event_list.domain.entities import EventList, EventListUpdate, EventLists
from src.event_list.application.event_use_cases import EventListUseCases
from src.auth.domain.entities import UserOut
from src.auth.presentation.config import get_current_user
from fastapi import status, Depends


@event_list_router.get("/", response_model=EventLists, status_code=status.HTTP_200_OK)
def get_all(use_cases: EventList = Depends(get_event_list_cases)):
    """
    Gets all Event Lists.
    """
    result = use_cases.get_all_flagship_programs()
    return {"data": result}


@event_list_router.get(
    "/{id}", response_model=EventList, status_code=status.HTTP_200_OK
)
def get_one(id: str, use_cases: EventListUseCases = Depends(get_event_list_cases)):
    """
    Gets one Event List.
    """
    result = use_cases.get_one_flagship_programs(id)
    return {"data": result}


@event_list_router.post(
    "/", response_model=EventList, status_code=status.HTTP_201_CREATED
)
def create(
    content: EventList,
    current_user: UserOut = get_current_user("admin", "super"),
    use_cases: EventListUseCases = Depends(get_event_list_cases),
):
    """
    Creates an Event List.
    """
    result = use_cases.create_flagship_programs(content, current_user)
    return {"data": result}


@event_list_router.patch(
    "/{id}", status_code=status.HTTP_201_CREATED, response_model=EventList
)
def update(
    id: str,
    content: EventListUpdate,
    current_user: UserOut = get_current_user("admin", "super"),
    use_cases: EventListUseCases = Depends(get_event_list_cases),
):
    """
    Updates an Event List.
    """
    message = use_cases.update_flagship_programs(id, content, current_user)
    return {"data": message}


@event_list_router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete(
    id: str,
    current_user: UserOut = get_current_user("admin", "super"),
    use_cases: EventListUseCases = Depends(get_event_list_cases),
):
    """
    Deletes an Event List.
    """
    return use_cases.delete_flagship_programs(id, current_user)
