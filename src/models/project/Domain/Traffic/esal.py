"""
esal.py
=======

Equivalent Single Axle Load (ESAL) Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents Equivalent Single Axle Load (ESAL)
information used for pavement design.

This model stores ESAL data only.

No AASHTO pavement design equations or load
equivalency calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class ESAL:
    """
    Represents Equivalent Single Axle Load data.
    """

    # =====================================================
    # Identity
    # =====================================================

    esal_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    lane_id: str = ""

    # =====================================================
    # Traffic Information
    # =====================================================

    base_year: int = 0

    design_year: int = 0

    design_period_years: int = 20

    average_daily_trucks: float = 0.0

    annual_average_daily_traffic: float = 0.0

    annual_growth_rate_percent: float = 0.0

    # =====================================================
    # ESAL Values
    # =====================================================

    daily_esal: float = 0.0

    annual_esal: float = 0.0

    cumulative_esal: float = 0.0

    design_esal: float = 0.0

    # =====================================================
    # Distribution Factors
    # =====================================================

    directional_distribution_factor: float = 0.0

    lane_distribution_factor: float = 0.0

    truck_percentage: float = 0.0

    # =====================================================
    # References
    # =====================================================

    design_standard: str = ""

    standard_version: str = ""

    source: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)