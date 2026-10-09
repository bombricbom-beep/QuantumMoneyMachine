from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Any


@dataclass
class StreamStatus:
    name: str
    rate_per_second: float
    active: bool = True
    roi: float = 0.0
    revenue_total: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class DashboardSnapshot:
    timestamp: str
    revenue_per_second: float
    daily_revenue: float
    monthly_revenue: float
    total_revenue: float
    total_reinvestment: float
    total_profit: float
    opportunities_scanned: int
    active_streams: list[StreamStatus]


class DashboardEngine:
    def __init__(self) -> None:
        self.streams = [
            StreamStatus(name="youtube", rate_per_second=0.12, roi=1.8, revenue_total=0.0),
            StreamStatus(name="affiliates", rate_per_second=0.08, roi=2.1, revenue_total=0.0),
            StreamStatus(name="dropshipping", rate_per_second=0.18, roi=1.7, revenue_total=0.0),
            StreamStatus(name="saas", rate_per_second=0.14, roi=2.5, revenue_total=0.0),
            StreamStatus(name="lead_generation", rate_per_second=0.09, roi=2.0, revenue_total=0.0),
            StreamStatus(name="services", rate_per_second=0.10, roi=1.9, revenue_total=0.0),
            StreamStatus(name="microtx", rate_per_second=0.20, roi=1.5, revenue_total=0.0),
            StreamStatus(name="data", rate_per_second=0.06, roi=1.3, revenue_total=0.0),
        ]
        self.total_revenue = 0.0
        self.total_reinvestment = 0.0
        self.total_profit = 0.0
        self.opportunities_scanned = 0

    def tick(self) -> DashboardSnapshot:
        for stream in self.streams:
            variation = random.uniform(0.85, 1.35)
            stream.rate_per_second = round(stream.rate_per_second * variation, 4)
            stream.revenue_total += stream.rate_per_second * 3600
            self.total_revenue += stream.rate_per_second * 3600
        self.total_reinvestment = self.total_revenue * 0.10
        self.total_profit = self.total_revenue - self.total_reinvestment
        self.opportunities_scanned += 3

        return DashboardSnapshot(
            timestamp="live",
            revenue_per_second=sum(s.rate_per_second for s in self.streams),
            daily_revenue=sum(s.rate_per_second for s in self.streams) * 86400,
            monthly_revenue=sum(s.rate_per_second for s in self.streams) * 86400 * 30,
            total_revenue=self.total_revenue,
            total_reinvestment=self.total_reinvestment,
            total_profit=self.total_profit,
            opportunities_scanned=self.opportunities_scanned,
            active_streams=self.streams,
        )


dashboard = DashboardEngine()
