"""
directional_distribution.py
===========================

Directional Distribution Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents directional traffic distribution information.

The directional distribution factor (D) describes the
percentage of total traffic traveling in the peak
direction during the design hour.

This module stores directional distribution data only.

No traffic calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class DirectionalDistribution:
    """
    Represents directional traffic distribution.
    """

    # =====================================================
    # Identity
    # =====================================================

    distribution_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    # =====================================================
    # Traffic Distribution
    # =====================================================

    total_volume_veh_per_hr: float = 0.0

    peak_direction_volume_veh_per_hr: float = 0.0

    opposite_direction_volume_veh_per_hr: float = 0.0

    # =====================================================
    # Directional Factor
    # =====================================================

    directional_factor: float = 0.0
    # Decimal value (e.g. 0.60)

    directional_percentage: float = 0.0
    # Percentage (e.g. 60)

    # =====================================================
    # Peak Period
    # =====================================================

    peak_hour: bool = True

    analysis_period_minutes: float = 60.0

    # =====================================================
    # Road Information
    # =====================================================

    roadway_type: str = ""

    direction_name: str = ""
    # Northbound
    # Southbound
    # Eastbound
    # Westbound
    # Increasing Station
    # Decreasing Station

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