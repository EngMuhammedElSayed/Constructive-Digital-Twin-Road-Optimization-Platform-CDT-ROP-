"""
speed_limit.py
==============

Posted Speed Limit Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the posted speed limit assigned to a roadway
segment.

This module stores legal speed limit information only.

No speed management, speed prediction, or design
consistency calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class SpeedLimit:
    """
    Represents posted roadway speed limits.
    """

    # =====================================================
    # Identity
    # =====================================================

    speed_limit_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    # =====================================================
    # Speed Limit
    # =====================================================

    posted_speed_limit_kmh: float = 0.0

    posted_speed_limit_mph: float = 0.0

    minimum_speed_limit_kmh: float = 0.0

    maximum_speed_limit_kmh: float = 0.0

    # =====================================================
    # Application
    # =====================================================

    roadway_type: str = ""
    # Urban Highway
    # Rural Highway
    # Expressway
    # Local Road
    # Collector
    # Arterial

    applies_to: str = ""
    # All Vehicles
    # Heavy Vehicles
    # Passenger Cars
    # School Zone

    # =====================================================
    # Restrictions
    # =====================================================

    school_zone: bool = False

    work_zone: bool = False

    weather_dependent: bool = False

    variable_speed_limit: bool = False

    # =====================================================
    # References
    # =====================================================

    governing_authority: str = ""

    design_standard: str = ""

    source: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)