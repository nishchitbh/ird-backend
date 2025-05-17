import os
import logging
import traceback
from src.shared.config import setting
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
from src.shared.domain.exceptions import AppException
from src.gallery.presentation.routes import gallery_router
from src.join_us.presentation.routes import join_us_router
from src.areas_of_work.presentation.routes import areas_router
from src.event_list.presentation.routes import event_list_router
from src.auth.presentation.routes import auth_router, user_router
from src.flagship_programs.presentation.routes import flagship_programs_router

ENV = os.getenv("ENV", 'prod').lower()
IS_PROD = ENV == "prod"

app = FastAPI(
    title="IRD Website Backend",
    docs_url=None if IS_PROD else "/docs",
    redoc_url=None if IS_PROD else "/redoc",
    openapi_url=None if IS_PROD else "/openapi.json",
)

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
        content={"detail": exc.detail},
    )

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    """Handles all unexpected exceptions."""
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


setting.upload_folder.mkdir(parents=True, exist_ok=True)
app.mount(
    "/uploads",
    StaticFiles(directory=str(setting.upload_folder), html=False),
    name="uploads",
)

api_router = APIRouter(prefix="/api")

api_router.include_router(auth_router)
api_router.include_router(user_router)
api_router.include_router(gallery_router)
api_router.include_router(areas_router)
api_router.include_router(join_us_router)
api_router.include_router(flagship_programs_router)
api_router.include_router(event_list_router)

app.include_router(api_router)
