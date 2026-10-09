from __future__ import annotations

from fastapi import FastAPI

from app.api.routes import router as growth_router
from app.main import app as api_app

api_app.include_router(growth_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
