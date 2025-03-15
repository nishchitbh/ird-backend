from fastapi import FastAPI, APIRouter, Request
import logging
import traceback
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.auth.presentation.routes import auth_router, user_router
from src.shared.domain.exceptions import AppException


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    """Handles custom application exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    """Handles all unexpected exceptions."""

    # Log the error with traceback for debugging
    logger.error(f"Unexpected error: {str(exc)}")
    logger.error(traceback.format_exc())

    return JSONResponse(
        status_code=500,
        content={
            "detail": "An internal server error occurred. Please try again later."},
    )


@app.get("/", tags=["Root"])
def read_root() -> dict:
    return {"message": "Hello World"}


api_router = APIRouter(prefix="/api")

api_router.include_router(auth_router)
api_router.include_router(user_router)

app.include_router(api_router)
