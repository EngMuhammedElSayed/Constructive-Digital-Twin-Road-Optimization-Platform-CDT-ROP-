"""
traffic_lane.py
===============

Traffic Lane Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway traffic lane.

This module stores traffic lane information only.

No traffic simulation, lane assignment algorithms,
capacity analysis, or HCM calculations are implemented
here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class TrafficLane:
    """
    Represents a roadway traffic lane.
    """

    # =====================================================
    # Identity
    # =====================================================

    lane_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    corridor_id: str = ""

    # =====================================================
    # Lane Information
    # =====================================================

    lane_number: int = 1

    direction: str = ""
    # Northbound
    # Southbound
    # Eastbound
    # Westbound

    lane_type: str = ""
    # General Purpose
    # HOV
    # Bus
    # Bicycle
    # Parking
    # Auxiliary
    # Acceleration
    # Deceleration
    # Turning

    # =====================================================
    # Geometry
    # =====================================================

    lane_width_m: float = 0.0

    lane_length_m: float = 0.0

    shoulder_width_m: float = 0.0

    # =====================================================
    # Traffic Characteristics
    # =====================================================

    speed_limit_kmh: float = 0.0

    operating_speed_kmh: float = 0.0

    design_speed_kmh: float = 0.0

    capacity_veh_per_hr: float = 0.0

    flow_rate_veh_per_hr: float = 0.0

    # =====================================================
    # Restrictions
    # =====================================================

    heavy_vehicle_allowed: bool = True

    pedestrian_allowed: bool = False

    bicycle_allowed: bool = False

    public_transport_only: bool = False

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