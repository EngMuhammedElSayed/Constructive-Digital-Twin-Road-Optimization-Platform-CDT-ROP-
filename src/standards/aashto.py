"""
AASHTO Design Standards

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

This module contains engineering constants and design limits
derived from the AASHTO Green Book.

Only engineering reference values should be stored here.
No engineering calculations are implemented in this module.

Author:
Eng. Muhammed

Research:
MSc Research
Cairo University
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AASHTODesignCriteria:
    """
    AASHTO roadway design criteria.
    """

    # ==========================================================
    # Driver Characteristics
    # ==========================================================

    perception_reaction_time: float = 2.5      # seconds

    comfortable_deceleration: float = 3.4      # m/s²

    gravity: float = 9.81                      # m/s²

    # ==========================================================
    # Horizontal Alignment
    # ==========================================================

    maximum_superelevation: float = 0.06

    side_friction_90: float = 0.13

    side_friction_80: float = 0.14

    # ==========================================================
    # Lane Geometry
    # ==========================================================

    minimum_lane_width: float = 3.00

    recommended_lane_width: float = 3.60

    maximum_lane_width: float = 3.75

    # ==========================================================
    # Shoulder
    # ==========================================================

    minimum_shoulder_width: float = 1.20

    recommended_shoulder_width: float = 2.50

    # ==========================================================
    # Median
    # ==========================================================

    minimum_median_width: float = 1.20

    recommended_median_width: float = 5.00

    # ==========================================================
    # Longitudinal Grade
    # ==========================================================

    minimum_grade: float = 0.30

    maximum_grade: float = 5.00

    # ==========================================================
    # Traffic
    # ==========================================================

    default_lane_capacity: float = 2200

    design_vc_limit: float = 0.90
