"""
level_of_service.py
===================

Level of Service (LOS) Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents roadway or intersection Level of Service (LOS)
information.

This module stores LOS assessment results only.

No Highway Capacity Manual (HCM) calculations are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class LevelOfService:
    """
    Represents roadway Level of Service (LOS).
    """

    # =====================================================
    # Identity
    # =====================================================

    los_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    facility_id: str = ""

    # =====================================================
    # LOS
    # =====================================================

    level: str = ""
    # A
    # B
    # C
    # D
    # E
    # F

    facility_type: str = ""
    # Freeway
    # Urban Highway
    # Rural Highway
    # Signalized Intersection
    # Unsignalized Intersection
    # Roundabout

    # =====================================================
    # Performance Indicators
    # =====================================================

    average_speed_kmh: float = 0.0

    density_pc_per_km_per_lane: float = 0.0

    average_delay_sec_per_vehicle: float = 0.0

    volume_capacity_ratio: float = 0.0

    # =====================================================
    # Traffic
    # =====================================================

    traffic_volume_veh_per_hr: float = 0.0

    capacity_veh_per_hr: float = 0.0

    # =====================================================
    # Analysis
    # =====================================================

    analysis_period_minutes: float = 60.0

    peak_hour: bool = False

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