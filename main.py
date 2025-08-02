import os
from dotenv import load_dotenv

from fastapi import FastAPI

from src.areas_of_work.presentation.routes import areas_router
from src.event_list.presentation.routes import event_list_router
from src.flagship_programs.presentation.routes import flagship_programs_router
from src.gallery.presentation.routes import gallery_router
from src.join_us.presentation.routes import join_us_router
from src.auth.presentation.routes import AuthRoutes, UserRoutes

from src.shared.middlewares.rate_limiter import rate_limit_middleware
from src.shared.middlewares.generic_response import generic_middleware

load_dotenv()
ENV = os.getenv("ENV", "prod").lower()
IS_PROD = ENV == "prod"

app = FastAPI(
    title="IRD Backend",
    docs_url=None if IS_PROD else "/docs",
    redoc_url=None if IS_PROD else "/redoc",
    openapi_url=None if IS_PROD else "/openapi.json",
)


app.middleware("http")(rate_limit_middleware)
app.middleware("http")(generic_middleware)


@app.get("/")
@app.get("/health")
async def health():
    return (
        {"status": "ok", "message": "Go to /docs for documentation."}
        if not IS_PROD
        else {"status": "ok", "message": "Healthy!"}
    )


app.include_router(AuthRoutes().router)
app.include_router(UserRoutes().router)
app.include_router(areas_router)
app.include_router(gallery_router)
app.include_router(flagship_programs_router)
app.include_router(event_list_router)
app.include_router(join_us_router)
