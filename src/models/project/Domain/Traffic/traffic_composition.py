"""
traffic_composition.py
======================

Traffic Composition Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents roadway traffic composition.

Traffic composition describes the percentage of each
vehicle class within the traffic stream.

This module stores traffic composition information only.

No Passenger Car Equivalent (PCE), ESAL, or traffic
composition calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class TrafficComposition:
    """
    Represents traffic composition for a roadway segment.
    """

    # =====================================================
    # Identity
    # =====================================================

    composition_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    # =====================================================
    # Total Traffic
    # =====================================================

    total_vehicles: float = 0.0

    average_daily_traffic: float = 0.0

    design_hour_volume: float = 0.0

    # =====================================================
    # Vehicle Composition (%)
    # =====================================================

    passenger_car_percentage: float = 0.0

    light_truck_percentage: float = 0.0

    medium_truck_percentage: float = 0.0

    heavy_truck_percentage: float = 0.0

    bus_percentage: float = 0.0

    motorcycle_percentage: float = 0.0

    bicycle_percentage: float = 0.0

    pedestrian_percentage: float = 0.0

    agricultural_vehicle_percentage: float = 0.0

    special_vehicle_percentage: float = 0.0

    # =====================================================
    # Analysis
    # =====================================================

    analysis_year: int = 0

    traffic_scenario: str = ""
    # Existing
    # Forecast
    # Design Year
    # Construction Stage

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