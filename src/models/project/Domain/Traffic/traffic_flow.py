"""
traffic_flow.py
===============

Traffic Flow Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents roadway traffic flow information.

Traffic flow describes the rate at which vehicles pass
a specific point on the roadway.

This module stores traffic flow information only.

No traffic flow theory equations, Highway Capacity Manual
(HCM) calculations, or simulation algorithms are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class TrafficFlow:
    """
    Represents roadway traffic flow.
    """

    # =====================================================
    # Identity
    # =====================================================

    flow_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    lane_id: str = ""

    # =====================================================
    # Flow Characteristics
    # =====================================================

    flow_rate_veh_per_hr: float = 0.0

    flow_rate_veh_per_min: float = 0.0

    peak_flow_rate_veh_per_hr: float = 0.0

    average_flow_rate_veh_per_hr: float = 0.0

    # =====================================================
    # Supporting Parameters
    # =====================================================

    average_speed_kmh: float = 0.0

    traffic_density_veh_per_km: float = 0.0

    lane_count: int = 0

    # =====================================================
    # Analysis
    # =====================================================

    analysis_period: str = ""
    # AM Peak
    # PM Peak
    # Daily
    # Weekend

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