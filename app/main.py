from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="QuantumMoneyMachine",
    description="Autonomous AI business engine for opportunity hunting, monetization, analytics, and reinvestment.",
    version="0.1.0",
)


class HealthResponse(BaseModel):
    status: str
    app: str = "QuantumMoneyMachine"
    version: str = "0.1.0"


@app.get("/health")
async def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.get("/")
async def root() -> dict:
    return {
        "message": "QuantumMoneyMachine is online.",
        "status": "ready",
        "mode": "autonomous-growth-engine",
    }
