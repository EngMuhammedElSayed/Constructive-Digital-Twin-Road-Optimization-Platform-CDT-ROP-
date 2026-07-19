"""
queue.py
========

Traffic Queue Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents traffic queue information for roadway
segments, intersections, and approaches.

This module stores queue information only.

No queue estimation models, HCM equations, or traffic
simulation algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Queue:
    """
    Represents traffic queue information.
    """

    # =====================================================
    # Identity
    # =====================================================

    queue_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    intersection_id: str = ""

    approach_id: str = ""

    lane_id: str = ""

    # =====================================================
    # Queue Characteristics
    # =====================================================

    average_queue_length_m: float = 0.0

    maximum_queue_length_m: float = 0.0

    average_queue_vehicles: float = 0.0

    maximum_queue_vehicles: float = 0.0

    average_queue_time_sec: float = 0.0

    maximum_queue_time_sec: float = 0.0

    # =====================================================
    # Traffic Conditions
    # =====================================================

    traffic_volume_veh_per_hr: float = 0.0

    capacity_veh_per_hr: float = 0.0

    volume_capacity_ratio: float = 0.0

    # =====================================================
    # Analysis
    # =====================================================

    queue_type: str = ""
    # Signalized
    # Unsignalized
    # Roundabout
    # Freeway
    # Work Zone

    peak_hour: bool = False

    analysis_period_minutes: float = 60.0

    # =====================================================
    # References
    # =====================================================

    design_standard: str = ""

    hcm_edition: str = ""

    source: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)