"""
lane_distribution.py
====================

Lane Distribution Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents traffic lane distribution information.

Lane distribution describes how traffic volume is
distributed among roadway lanes.

This module stores lane distribution data only.

No HCM calculations or traffic assignment algorithms
are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class LaneDistribution:
    """
    Represents traffic lane distribution.
    """

    # =====================================================
    # Identity
    # =====================================================

    lane_distribution_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    # =====================================================
    # Lane Information
    # =====================================================

    lane_number: int = 1

    direction: str = ""
    # Northbound
    # Southbound
    # Eastbound
    # Westbound
    # Increasing Station
    # Decreasing Station

    # =====================================================
    # Traffic
    # =====================================================

    total_directional_volume_veh_per_hr: float = 0.0

    lane_volume_veh_per_hr: float = 0.0

    lane_distribution_factor: float = 0.0
    # Decimal (0.80)

    lane_distribution_percentage: float = 0.0
    # Percent (80)

    # =====================================================
    # Lane Type
    # =====================================================

    lane_type: str = ""
    # Through
    # Left Turn
    # Right Turn
    # Climbing
    # Auxiliary
    # HOV

    design_lane: bool = False

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