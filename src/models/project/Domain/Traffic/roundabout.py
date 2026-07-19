"""
roundabout.py
==============

Roundabout Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway roundabout.

This module stores roundabout geometry and traffic
information only.

No roundabout capacity analysis, swept-path analysis,
or HCM calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Roundabout:
    """
    Represents a roadway roundabout.
    """

    # =====================================================
    # Identity
    # =====================================================

    roundabout_id: str = ""

    project_id: str = ""

    roadway_id: str = ""

    name: str = ""

    # =====================================================
    # Classification
    # =====================================================

    roundabout_type: str = ""
    # Mini
    # Compact
    # Single Lane
    # Multi Lane
    # Turbo

    # =====================================================
    # Geometry
    # =====================================================

    inscribed_circle_diameter_m: float = 0.0

    central_island_diameter_m: float = 0.0

    circulatory_roadway_width_m: float = 0.0

    entry_width_m: float = 0.0

    exit_width_m: float = 0.0

    truck_apron_width_m: float = 0.0

    splitter_island_length_m: float = 0.0

    number_of_approaches: int = 0

    # =====================================================
    # Traffic
    # =====================================================

    average_daily_traffic: float = 0.0

    design_hour_volume: float = 0.0

    heavy_vehicle_percentage: float = 0.0

    design_speed_kmh: float = 0.0

    # =====================================================
    # Design Vehicle
    # =====================================================

    design_vehicle: str = ""

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