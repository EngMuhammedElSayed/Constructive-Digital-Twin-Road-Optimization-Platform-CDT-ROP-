"""
origin_destination.py
=====================

Origin-Destination (OD) Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents origin-destination (OD) traffic demand
between two traffic analysis zones (TAZ), nodes,
or geographic locations.

This module stores OD demand information only.

No traffic assignment, route choice, or travel demand
model calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class OriginDestination:
    """
    Represents an Origin-Destination traffic demand record.
    """

    # =====================================================
    # Identity
    # =====================================================

    od_id: str = ""

    project_id: str = ""

    scenario_id: str = ""

    # =====================================================
    # Origin
    # =====================================================

    origin_zone_id: str = ""

    origin_name: str = ""

    # =====================================================
    # Destination
    # =====================================================

    destination_zone_id: str = ""

    destination_name: str = ""

    # =====================================================
    # Traffic Demand
    # =====================================================

    trips_per_day: float = 0.0

    trips_per_hour: float = 0.0

    peak_hour_trips: float = 0.0

    # =====================================================
    # Vehicle Composition
    # =====================================================

    passenger_car_percentage: float = 0.0

    heavy_vehicle_percentage: float = 0.0

    bus_percentage: float = 0.0

    motorcycle_percentage: float = 0.0

    # =====================================================
    # Analysis
    # =====================================================

    analysis_year: int = 0

    analysis_period: str = ""
    # AM Peak
    # PM Peak
    # Daily
    # Weekend

    # =====================================================
    # References
    # =====================================================

    source: str = ""

    demand_model: str = ""
    # Four-Step
    # Survey
    # GPS
    # Mobile Data
    # User Defined

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)