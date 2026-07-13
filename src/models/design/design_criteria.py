"""
Design Criteria Data Model

This module defines the engineering design criteria used by
the Constructive Digital Twin Road Optimization Platform (CDT-ROP).

The values represent engineering inputs and design limits.
No engineering calculations are implemented here.
"""

from dataclasses import dataclass


@dataclass
class DesignCriteria:
    """
    Engineering design criteria used throughout the project.
    """

    # ----------------------------------------
    # General
    # ----------------------------------------

    design_standard: str = "AASHTO"

    design_speed: float = 100.0        # km/h

    terrain_type: str = "Rolling"

    road_classification: str = "Rural Arterial"

    # ----------------------------------------
    # Cross Section
    # ----------------------------------------

    lane_width: float = 3.65           # m

    shoulder_width: float = 2.50       # m

    median_width: float = 6.00         # m

    cross_slope: float = 0.02

    max_superelevation: float = 0.08

    # ----------------------------------------
    # Horizontal Alignment
    # ----------------------------------------

    minimum_curve_radius: float = 0.0

    minimum_spiral_length: float = 0.0

    maximum_deflection_angle: float = 0.0

    # ----------------------------------------
    # Vertical Alignment
    # ----------------------------------------

    maximum_grade: float = 0.06

    minimum_grade: float = 0.005

    minimum_k_value: float = 0.0

    # ----------------------------------------
    # Sight Distance
    # ----------------------------------------

    stopping_sight_distance: float = 0.0

    passing_sight_distance: float = 0.0

    decision_sight_distance: float = 0.0
