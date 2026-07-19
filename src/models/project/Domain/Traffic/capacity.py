"""
capacity.py
===========

Traffic Capacity Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents roadway traffic capacity information.

This module stores roadway capacity data only.

No Highway Capacity Manual (HCM) calculations are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Capacity:
    """
    Represents roadway capacity information.
    """

    # =====================================================
    # Identity
    # =====================================================

    capacity_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    # =====================================================
    # Roadway Characteristics
    # =====================================================

    facility_type: str = ""
    # Freeway
    # Expressway
    # Urban Highway
    # Rural Highway
    # Arterial
    # Collector
    # Local Road

    analysis_direction: str = ""

    lane_count: int = 0

    lane_width_m: float = 0.0

    shoulder_width_m: float = 0.0

    median_type: str = ""

    terrain_type: str = ""
    # Level
    # Rolling
    # Mountainous

    # =====================================================
    # Traffic Capacity
    # =====================================================

    base_capacity_veh_per_hr: float = 0.0

    adjusted_capacity_veh_per_hr: float = 0.0

    service_flow_rate_veh_per_hr: float = 0.0

    demand_volume_veh_per_hr: float = 0.0

    # =====================================================
    # Heavy Vehicles
    # =====================================================

    heavy_vehicle_percentage: float = 0.0

    passenger_car_equivalent: float = 1.0

    # =====================================================
    # Performance
    # =====================================================

    free_flow_speed_kmh: float = 0.0

    operating_speed_kmh: float = 0.0

    level_of_service: str = ""

    volume_capacity_ratio: float = 0.0

    # =====================================================
    # References
    # =====================================================

    design_standard: str = ""

    hcm_edition: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)