"""
safety_indicator.py
===================

Traffic Safety Indicator Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents roadway traffic safety performance indicators.

This module stores safety assessment data only.

No crash prediction models, Highway Safety Manual (HSM)
equations, or statistical safety analysis are implemented
here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class SafetyIndicator:
    """
    Represents roadway traffic safety indicators.
    """

    # =====================================================
    # Identity
    # =====================================================

    safety_indicator_id: str = ""

    project_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    intersection_id: str = ""

    # =====================================================
    # Crash Statistics
    # =====================================================

    total_crashes: int = 0

    fatal_crashes: int = 0

    injury_crashes: int = 0

    property_damage_only_crashes: int = 0

    # =====================================================
    # Safety Performance
    # =====================================================

    crash_rate: float = 0.0
    # crashes / million vehicle-km

    severity_index: float = 0.0

    conflict_points: int = 0

    # =====================================================
    # Speed Characteristics
    # =====================================================

    design_speed_kmh: float = 0.0

    operating_speed_kmh: float = 0.0

    speed_consistency_index: float = 0.0

    # =====================================================
    # Roadway Characteristics
    # =====================================================

    horizontal_curve_radius_m: float = 0.0

    longitudinal_grade_percent: float = 0.0

    stopping_sight_distance_m: float = 0.0

    # =====================================================
    # Overall Assessment
    # =====================================================

    safety_level: str = ""
    # Excellent
    # Good
    # Fair
    # Poor
    # Critical

    safety_score: float = 0.0

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