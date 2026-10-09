from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class LeadCreateRequest(BaseModel):
    business_name: str = Field(..., min_length=2, max_length=200)
    contact_name: str = Field(..., min_length=2, max_length=200)
    email: str = Field(..., min_length=3)
    phone: str = Field(..., min_length=5)
    service_needed: str = Field(..., min_length=2, max_length=200)
    message: str = Field(default="", max_length=2000)
    source: str = Field(default="website")


class LeadResponse(BaseModel):
    id: str
    business_name: str
    contact_name: str
    email: str
    phone: str
    service_needed: str
    message: str
    source: str
    status: str = "new"
    qualification_score: int = 0
    summary: str = ""


class LeadQualificationResult(BaseModel):
    score: int = Field(..., ge=0, le=100)
    summary: str
    ready_for_followup: bool
    next_action: str


class BusinessAccount(BaseModel):
    id: str
    business_name: str
    owner_name: str
    email: str
    plan: str = "starter"
    monthly_price: float = 79.0
    created_at: str


class ApiConfig(BaseModel):
    app_name: str = "LeadFlow AI"
    version: str = "0.1.0"
    environment: str = "development"
    features: list[str] = [
        "lead_capture",
        "lead_qualification",
        "response_summary",
        "follow_up_tracking",
    ]


class AccountSummary(BaseModel):
    business_name: str
    plan: str
    leads_received: int
    converted_leads: int
    response_rate: float
    revenue_estimate: float


class LeadListResponse(BaseModel):
    items: list[LeadResponse]
    total: int
