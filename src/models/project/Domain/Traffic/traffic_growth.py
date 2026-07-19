"""
traffic_growth.py
=================

Traffic Growth Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents traffic growth information used for roadway
planning and design.

This module stores traffic growth data only.

No traffic forecasting algorithms or prediction models
are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class TrafficGrowth:
    """
    Represents traffic growth information.
    """

    # =====================================================
    # Identity
    # =====================================================

    traffic_growth_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    # =====================================================
    # Base Data
    # =====================================================

    base_year: int = 0

    design_year: int = 0

    forecast_year: int = 0

    # =====================================================
    # Traffic
    # =====================================================

    base_aadt: float = 0.0

    projected_aadt: float = 0.0

    annual_growth_rate_percent: float = 0.0

    cumulative_growth_factor: float = 1.0

    # =====================================================
    # Forecast
    # =====================================================

    forecast_method: str = ""
    # Historical
    # Regression
    # Government Forecast
    # Regional Model
    # Manual Estimate

    traffic_scenario: str = ""
    # Existing
    # Future
    # Optimistic
    # Conservative
    # Design

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