"""
traffic_density.py
==================

Traffic Density Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents roadway traffic density information.

Traffic density is the number of vehicles occupying a
unit length of roadway.

This module stores traffic density data only.

No Highway Capacity Manual (HCM) calculations or traffic
flow equations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class TrafficDensity:
    """
    Represents roadway traffic density.
    """

    # =====================================================
    # Identity
    # =====================================================

    density_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    lane_id: str = ""

    # =====================================================
    # Density
    # =====================================================

    density_veh_per_km: float = 0.0

    density_veh_per_km_per_lane: float = 0.0

    density_veh_per_mile: float = 0.0

    density_veh_per_mile_per_lane: float = 0.0

    # =====================================================
    # Supporting Traffic Data
    # =====================================================

    traffic_volume_veh_per_hr: float = 0.0

    average_speed_kmh: float = 0.0

    operating_speed_kmh: float = 0.0

    # =====================================================
    # Analysis
    # =====================================================

    analysis_period: str = ""
    # AM Peak
    # PM Peak
    # Daily
    # Off Peak

    roadway_type: str = ""

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