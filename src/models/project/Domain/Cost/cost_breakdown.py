"""
cost_breakdown.py
=================

Cost Breakdown Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the breakdown of project construction costs.

This module stores cost components only.

No estimation formulas or engineering calculations are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class CostBreakdown:
    """
    Represents the breakdown of project costs.
    """

    # =====================================================
    # Direct Costs
    # =====================================================

    earthwork: float = 0.0

    pavement: float = 0.0

    drainage: float = 0.0

    structures: float = 0.0

    utilities: float = 0.0

    right_of_way: float = 0.0

    environmental: float = 0.0

    traffic_control: float = 0.0

    temporary_works: float = 0.0

    # =====================================================
    # Indirect Costs
    # =====================================================

    mobilization: float = 0.0

    supervision: float = 0.0

    engineering: float = 0.0

    contingency: float = 0.0

    # =====================================================
    # Financial
    # =====================================================

    taxes: float = 0.0

    inflation: float = 0.0

    # =====================================================
    # Currency
    # =====================================================

    currency: str = "EGP"

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)

    # =====================================================
    # Read-Only Properties
    # =====================================================

    @property
    def direct_cost(self) -> float:
        return (
            self.earthwork
            + self.pavement
            + self.drainage
            + self.structures
            + self.utilities
            + self.right_of_way
            + self.environmental
            + self.traffic_control
            + self.temporary_works
        )

    @property
    def indirect_cost(self) -> float:
        return (
            self.mobilization
            + self.supervision
            + self.engineering
            + self.contingency
        )

    @property
    def financial_cost(self) -> float:
        return self.taxes + self.inflation

    @property
    def total_cost(self) -> float:
        return (
            self.direct_cost
            + self.indirect_cost
            + self.financial_cost
        )