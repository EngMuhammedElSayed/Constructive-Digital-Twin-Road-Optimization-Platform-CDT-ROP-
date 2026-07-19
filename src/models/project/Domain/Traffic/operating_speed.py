"""
operating_speed.py
==================

Operating Speed Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents roadway operating speed information.

Operating speed is the observed speed at which drivers
travel under normal roadway, weather, and traffic
conditions.

This module stores operating speed data only.

No speed prediction models or statistical calculations
are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class OperatingSpeed:
    """
    Represents roadway operating speed.
    """

    # =====================================================
    # Identity
    # =====================================================

    operating_speed_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    # =====================================================
    # Operating Speed
    # =====================================================

    average_speed_kmh: float = 0.0

    average_speed_mph: float = 0.0

    percentile_85_speed_kmh: float = 0.0

    percentile_85_speed_mph: float = 0.0

    # =====================================================
    # Posted Speed
    # =====================================================

    posted_speed_limit_kmh: float = 0.0

    posted_speed_limit_mph: float = 0.0

    # =====================================================
    # Conditions
    # =====================================================

    roadway_type: str = ""

    terrain_type: str = ""

    traffic_condition: str = ""
    # Free Flow
    # Moderate
    # Congested

    weather_condition: str = ""
    # Dry
    # Wet
    # Snow
    # Fog

    # =====================================================
    # Survey Information
    # =====================================================

    observation_date: str = ""

    sample_size: int = 0

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