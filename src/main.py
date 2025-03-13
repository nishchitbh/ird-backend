from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from src.auth.presentation.routes import auth_router, user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
def read_root() -> dict:
    return {"message": "Hello World"}


api_router = APIRouter(prefix="/api")

api_router.include_router(auth_router)
api_router.include_router(user_router)

app.include_router(api_router)

# To be setup later
# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title="IRD Web Backend",
#         version="1.0.0",
#         routes=app.routes,
#     )
#     updated_paths = {}
#     for path, path_data in openapi_schema["paths"].items():
#         new_path = path.replace("/api/v1", "", 1)
#         updated_paths[new_path] = path_data

#     openapi_schema["paths"] = updated_paths

#     openapi_schema["servers"] = [
#         {"url": "/api/v1", "description": "Base API URL"}]

#     app.openapi_schema = openapi_schema
#     return app.openapi_schema

# app.openapi = custom_openapi
