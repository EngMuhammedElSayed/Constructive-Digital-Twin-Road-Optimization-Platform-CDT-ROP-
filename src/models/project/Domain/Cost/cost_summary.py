"""
cost_summary.py
===============

Cost Summary Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the final summary of project costs.

This module stores summarized cost values only.

No engineering calculations, quantity takeoff,
or cost estimation logic are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class CostSummary:
    """
    Represents the summarized project cost.
    """

    # =====================================================
    # Direct Cost
    # =====================================================

    direct_cost: float = 0.0

    # =====================================================
    # Indirect Cost
    # =====================================================

    indirect_cost: float = 0.0

    # =====================================================
    # Financial
    # =====================================================

    contingency_cost: float = 0.0

    taxes: float = 0.0

    inflation_cost: float = 0.0

    # =====================================================
    # Final Cost
    # =====================================================

    total_cost: float = 0.0

    currency: str = "EGP"

    # =====================================================
    # Reporting
    # =====================================================

    estimation_level: str = "Conceptual"

    estimate_date: str = ""

    remarks: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)