from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RevenueStream:
    name: str
    rate_per_second: float = 0.0
    revenue_today: float = 0.0
    revenue_total: float = 0.0
    active: bool = True
    roi: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class Opportunity:
    name: str
    niche: str
    problem: str
    solution: str
    estimated_monthly_revenue: float
    effort: float
    confidence: float
    channels: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class MetricsSnapshot:
    revenue_per_second: float
    daily_revenue: float
    monthly_revenue: float
    total_revenue: float
    total_reinvestment: float
    total_profit: float
    opportunities_scanned: int
    channels_active: int
