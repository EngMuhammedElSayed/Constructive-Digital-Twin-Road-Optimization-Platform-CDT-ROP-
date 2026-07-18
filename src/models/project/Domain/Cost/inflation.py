"""
inflation.py
============

Inflation Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents inflation assumptions used during project
cost estimation.

This module stores inflation data only.

No forecasting, financial modelling, or cost escalation
algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Dict


@dataclass(slots=True)
class Inflation:
    """
    Represents inflation information for project cost estimation.
    """

    # =====================================================
    # General
    # =====================================================

    enabled: bool = True

    annual_rate: float = 0.0

    base_year: int = date.today().year

    target_year: int = date.today().year

    # =====================================================
    # Financial
    # =====================================================

    escalation_rate: float = 0.0

    cumulative_factor: float = 1.0

    inflation_cost: float = 0.0

    # =====================================================
    # Currency
    # =====================================================

    currency: str = "EGP"

    # =====================================================
    # Source
    # =====================================================

    source: str = ""

    remarks: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)