"""
design_criteria.py
==================

Road Design Criteria Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines roadway design criteria used throughout the platform.

This module contains engineering design parameters only.
No engineering calculations are performed here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DesignCriteria:
    """
    Represents roadway geometric design criteria.
    """

    # =====================================================
    # General
    # =====================================================

    design_standard: str = "AASHTO"

    design_speed_kph: float = 90.0

    terrain_type: str = "Rolling"

    roadway_classification: str = "Urban Highway"

    # =====================================================
    # Cross Section
    # =====================================================

    lane_width_m: float = 3.65

    shoulder_width_m: float = 2.50

    median_width_m: float = 5.00

    cross_slope_percent: float = 2.0

    # =====================================================
    # Horizontal Alignment
    # =====================================================

    minimum_horizontal_radius_m: float = 0.0

    maximum_superelevation: float = 0.06

    maximum_side_friction: float = 0.13

    minimum_transition_length_m: float = 0.0

    # =====================================================
    # Vertical Alignment
    # =====================================================

    maximum_grade_percent: float = 5.0

    minimum_grade_percent: float = 0.3

    minimum_crest_k: float = 0.0

    minimum_sag_k: float = 0.0

    # =====================================================
    # Sight Distance
    # =====================================================

    stopping_sight_distance_m: float = 0.0

    passing_sight_distance_m: float = 0.0

    decision_sight_distance_m: float = 0.0

    intersection_sight_distance_m: float = 0.0

    # =====================================================
    # Traffic
    # =====================================================

    design_hour_volume: float = 0.0

    number_of_lanes: int = 4

    level_of_service: str = "C"

    # =====================================================
    # Safety
    # =====================================================

    reaction_time_sec: float = 2.5

    deceleration_rate_mps2: float = 3.4

    # =====================================================
    # Drainage
    # =====================================================

    minimum_drainage_slope_percent: float = 0.5

    # =====================================================
    # Earthwork
    # =====================================================

    maximum_cut_slope: float = 1.5

    maximum_fill_slope: float = 2.0