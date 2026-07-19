"""
accident_data.py
================

Traffic Accident Data Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents recorded traffic accident information used
for roadway safety assessment and optimization.

This module stores accident data only.

No crash prediction or safety analysis algorithms are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass(slots=True)
class AccidentData:
    """
    Represents traffic accident information.
    """

    # =====================================================
    # Identity
    # =====================================================

    accident_id: str = ""

    project_id: str = ""

    roadway_id: str = ""

    # =====================================================
    # Location
    # =====================================================

    station: float = 0.0

    latitude: float = 0.0

    longitude: float = 0.0

    lane_number: int = 0

    direction: str = ""

    # =====================================================
    # Time
    # =====================================================

    accident_datetime: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # Accident Information
    # =====================================================

    accident_type: str = ""
    # Rear-End
    # Head-On
    # Side Collision
    # Run-Off-Road
    # Pedestrian
    # Bicycle
    # Animal
    # Other

    severity: str = ""
    # Property Damage Only
    # Minor Injury
    # Serious Injury
    # Fatal

    weather_condition: str = ""

    pavement_condition: str = ""

    lighting_condition: str = ""

    # =====================================================
    # Vehicles
    # =====================================================

    number_of_vehicles: int = 0

    heavy_vehicle_involved: bool = False

    pedestrian_involved: bool = False

    bicycle_involved: bool = False

    # =====================================================
    # Consequences
    # =====================================================

    fatalities: int = 0

    serious_injuries: int = 0

    minor_injuries: int = 0

    property_damage_only: bool = False

    # =====================================================
    # Metadata
    # =====================================================

    source: str = ""

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)