"""
growth_factor.py
================

Traffic Growth Factor Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents traffic growth factor information used in
traffic forecasting and pavement design.

This module stores traffic growth parameters only.

No traffic forecasting equations or compound growth
calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class GrowthFactor:
    """
    Represents traffic growth information.
    """

    # =====================================================
    # Identity
    # =====================================================

    growth_factor_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    # =====================================================
    # Time
    # =====================================================

    base_year: int = 0

    forecast_year: int = 0

    design_period_years: int = 20

    # =====================================================
    # Growth
    # =====================================================

    annual_growth_rate_percent: float = 0.0

    cumulative_growth_factor: float = 1.0

    growth_method: str = ""
    # Constant
    # Compound
    # Historical
    # Regression
    # User Defined

    # =====================================================
    # Traffic
    # =====================================================

    base_aadt: float = 0.0

    forecast_aadt: float = 0.0

    truck_growth_rate_percent: float = 0.0

    # =====================================================
    # References
    # =====================================================

    source: str = ""

    design_standard: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)