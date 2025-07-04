import os
from dotenv import load_dotenv

from fastapi import FastAPI

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


app.include_router(AuthRoutes().router)
app.include_router(UserRoutes().router)
