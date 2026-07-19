"""
intersection.py
===============

Intersection Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway intersection.

This module stores geometric and traffic-related
intersection information only.

No intersection capacity analysis, signal timing,
or traffic simulation algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Intersection:
    """
    Represents a roadway intersection.
    """

    # =====================================================
    # Identity
    # =====================================================

    intersection_id: str = ""

    project_id: str = ""

    name: str = ""

    # =====================================================
    # Location
    # =====================================================

    station: float = 0.0

    latitude: float = 0.0

    longitude: float = 0.0

    # =====================================================
    # Classification
    # =====================================================

    intersection_type: str = ""
    # Three-Leg
    # Four-Leg
    # Multi-Leg
    # Roundabout
    # Interchange
    # Signalized
    # Unsignalized

    control_type: str = ""
    # Signal
    # Stop
    # Yield
    # Roundabout
    # Free Flow

    # =====================================================
    # Geometry
    # =====================================================

    number_of_approaches: int = 0

    number_of_lanes: int = 0

    design_speed_kmh: float = 0.0

    corner_radius_m: float = 0.0

    # =====================================================
    # Traffic
    # =====================================================

    average_daily_traffic: float = 0.0

    peak_hour_volume: float = 0.0

    heavy_vehicle_percentage: float = 0.0

    # =====================================================
    # Safety
    # =====================================================

    crash_history_available: bool = False

    # =====================================================
    # References
    # =====================================================

    design_standard: str = ""

    source: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)