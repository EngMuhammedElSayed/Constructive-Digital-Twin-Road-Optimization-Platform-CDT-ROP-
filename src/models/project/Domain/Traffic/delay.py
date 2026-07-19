"""
delay.py
========

Traffic Delay Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents traffic delay information for a roadway,
intersection, or traffic movement.

This module stores delay-related data only.

No Highway Capacity Manual (HCM) delay calculations or
traffic simulation algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Delay:
    """
    Represents traffic delay information.
    """

    # =====================================================
    # Identity
    # =====================================================

    delay_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    movement_id: str = ""

    # =====================================================
    # Delay Type
    # =====================================================

    delay_type: str = ""
    # Control
    # Uniform
    # Incremental
    # Queue
    # Incident
    # Travel Time

    # =====================================================
    # Average Delay
    # =====================================================

    average_delay_sec_per_vehicle: float = 0.0

    total_delay_hours: float = 0.0

    maximum_delay_sec: float = 0.0

    minimum_delay_sec: float = 0.0

    # =====================================================
    # Traffic
    # =====================================================

    demand_volume_veh_per_hr: float = 0.0

    served_volume_veh_per_hr: float = 0.0

    level_of_service: str = ""

    # =====================================================
    # Analysis Period
    # =====================================================

    analysis_period_minutes: float = 60.0

    peak_hour: bool = False

    # =====================================================
    # References
    # =====================================================

    design_standard: str = ""

    hcm_edition: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)