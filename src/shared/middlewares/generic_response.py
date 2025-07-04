# api/shared/middleware.py
import json
import traceback
from fastapi import Request
from fastapi.responses import JSONResponse, Response
from src.shared.domain.exceptions import AppException


async def generic_middleware(request: Request, call_next):
    if request.url.path.startswith(("/docs", "/redoc", "/openapi.json")):
        return await call_next(request)
    try:
        response: Response = await call_next(request)
        content_type = response.headers.get("content-type", "")
        if "application/json" not in content_type:
            return response

        body = [chunk async for chunk in response.body_iterator]
        raw = b"".join(body).decode()
        try:
            payload = json.loads(raw)
            pagination = None
            if isinstance(payload, dict) and "pagination" in payload:
                pagination = payload.pop("pagination")
        except json.JSONDecodeError:
            return response

        status_code = response.status_code
        is_success = 200 <= status_code < 300

        envelope = {
            "status": "success" if is_success else "error",
            "data": payload if is_success else None,
            "message": "Request successful!" if is_success else "Error occurred!",
            "error": (
                None if is_success else payload.get("detail", payload.get("error"))
            ),
            "pagination": pagination if is_success else None,
        }
        return JSONResponse(status_code=status_code, content=envelope)

    except AppException as exc:
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": "error",
                "data": None,
                "message": "Error occurred!",
                "error": exc.detail,
                "pagination": None,
            },
        )
    except Exception:
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "data": None,
                "message": "Error occurred!",
                "error": "Internal server error",
                "pagination": None,
            },
        )
