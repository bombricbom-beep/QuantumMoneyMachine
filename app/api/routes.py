from __future__ import annotations

import uuid

from fastapi import APIRouter, HTTPException, status

from app.api.schemas import LeadCreateRequest, LeadListResponse, LeadResponse
from app.services.leadflow import lead_qualification_service

router = APIRouter(prefix="/api", tags=["leadflow"])

LEADS: dict[str, LeadResponse] = {}


@router.get("/health")
async def health() -> dict:
    return {"status": "ok", "app": "LeadFlow AI"}


@router.post("/leads", response_model=LeadResponse)
async def create_lead(request: LeadCreateRequest) -> LeadResponse:
    lead_id = str(uuid.uuid4())
    qualification = lead_qualification_service.qualify(request)

    lead = LeadResponse(
        id=lead_id,
        business_name=request.business_name,
        contact_name=request.contact_name,
        email=request.email,
        phone=request.phone,
        service_needed=request.service_needed,
        message=request.message,
        source=request.source,
        status="new",
        qualification_score=qualification.score,
        summary=qualification.summary,
    )
    LEADS[lead_id] = lead
    return lead


@router.get("/leads", response_model=LeadListResponse)
async def list_leads() -> LeadListResponse:
    items = list(LEADS.values())
    return LeadListResponse(items=items, total=len(items))


@router.post("/leads/{lead_id}/qualify")
async def qualify_lead(lead_id: str) -> dict:
    lead = LEADS.get(lead_id)
    if not lead:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="lead not found")

    request = LeadCreateRequest(
        business_name=lead.business_name,
        contact_name=lead.contact_name,
        email=lead.email,
        phone=lead.phone,
        service_needed=lead.service_needed,
        message=lead.message,
        source=lead.source,
    )
    result = lead_qualification_service.qualify(request)
    return {
        "lead_id": lead_id,
        "score": result.score,
        "summary": result.summary,
        "ready_for_followup": result.ready_for_followup,
        "next_action": result.next_action,
    }


@router.get("/dashboard")
async def dashboard() -> dict:
    items = list(LEADS.values())
    total = len(items)
    avg_score = sum(item.qualification_score for item in items) / total if total else 0
    return {
        "total_leads": total,
        "average_score": round(avg_score, 2),
        "high_intent": sum(1 for item in items if item.qualification_score >= 60),
        "sales_opportunities": sum(1 for item in items if item.qualification_score >= 85),
    }
