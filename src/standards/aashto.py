"""
===============================================================================
AASHTO Design Standards
===============================================================================

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

Description
-----------
This module provides engineering reference values based on the
AASHTO Green Book.

The module contains ONLY engineering reference data.
No engineering calculations should be implemented here.

These values are intended to be consumed by:

- Geometry Engine
- Safety Engine
- Traffic Engine
- Optimization Engine
- Civil 3D Add-in
- Digital Twin Engine

Author:
Eng. Muhammed

Research:
MSc Research
Cairo University

===============================================================================
"""

from dataclasses import dataclass
from typing import Dict


# =============================================================================
# Driver Characteristics
# =============================================================================

@dataclass(frozen=True)
class DriverCriteria:
    """
    Driver-related design assumptions.
    """

    perception_reaction_time: float = 2.5      # sec
    comfortable_deceleration: float = 3.4      # m/s²
    gravity: float = 9.81                      # m/s²


# =============================================================================
# Horizontal Alignment
# =============================================================================

@dataclass(frozen=True)
class HorizontalAlignmentCriteria:
    """
    Horizontal roadway design criteria.
    """

    maximum_superelevation: float = 0.06

    side_friction = {
        30: 0.24,
        40: 0.21,
        50: 0.18,
        60: 0.16,
        70: 0.15,
        80: 0.14,
        90: 0.13,
        100: 0.12,
        110: 0.11,
        120: 0.10
    }

    minimum_radius_limit: float = 50.0


# =============================================================================
# Lane Geometry
# =============================================================================

@dataclass(frozen=True)
class LaneCriteria:
    """
    Lane geometry criteria.
    """

    minimum_width: float = 3.00

    recommended_width: float = 3.60

    maximum_width: float = 3.75


# =============================================================================
# Shoulder
# =============================================================================

@dataclass(frozen=True)
class ShoulderCriteria:
    """
    Shoulder design criteria.
    """

    minimum_width: float = 1.20

    recommended_width: float = 2.50

    maximum_width: float = 3.00


# =============================================================================
# Median
# =============================================================================

@dataclass(frozen=True)
class MedianCriteria:
    """
    Median design criteria.
    """

    minimum_width: float = 1.20

    recommended_width: float = 5.00

    maximum_width: float = 30.00


# =============================================================================
# Longitudinal Grade
# =============================================================================

@dataclass(frozen=True)
class GradeCriteria:
    """
    Longitudinal grade limits.
    """

    minimum_grade: float = 0.30

    maximum_grade: float = 5.00


# =============================================================================
# Traffic
# =============================================================================

@dataclass(frozen=True)
class TrafficCriteria:
    """
    Simplified traffic criteria.
    """

    default_lane_capacity: float = 2200.0

    design_vc_limit: float = 0.90

    peak_hour_factor: float = 0.92


# =============================================================================
# Sight Distance
# =============================================================================

@dataclass(frozen=True)
class SightDistanceCriteria:
    """
    Sight distance assumptions.
    """

    eye_height: float = 1.08

    object_height: float = 0.60


# =============================================================================
# Roadside
# =============================================================================

@dataclass(frozen=True)
class RoadsideCriteria:
    """
    Roadside design values.
    """

    minimum_clear_zone: float = 3.0

    recommended_clear_zone: float = 6.0


# =============================================================================
# Main Standard Class
# =============================================================================

class AASHTO:

    """
    Central access point for all AASHTO engineering standards.
    """

    driver = DriverCriteria()

    horizontal = HorizontalAlignmentCriteria()

    lane = LaneCriteria()

    shoulder = ShoulderCriteria()

    median = MedianCriteria()

    grade = GradeCriteria()

    traffic = TrafficCriteria()

    sight_distance = SightDistanceCriteria()

    roadside = RoadsideCriteria()

    # -------------------------------------------------------------------------
    # Utility Methods
    # -------------------------------------------------------------------------

    @staticmethod
    def get_side_friction(design_speed: float) -> float:
        """
        Returns the AASHTO side friction factor for a given design speed.

        Parameters
        ----------
        design_speed : float
            Design speed (km/h)

        Returns
        -------
        float
        """

        table = AASHTO.horizontal.side_friction

        if design_speed in table:
            return table[design_speed]

        nearest = min(table.keys(), key=lambda x: abs(x-design_speed))

        return table[nearest]


    @staticmethod
    def minimum_radius(
            design_speed: float,
            superelevation: float = None
    ) -> float:
        """
        Compute minimum horizontal radius according to AASHTO.

        Parameters
        ----------
        design_speed : km/h

        superelevation : decimal

        Returns
        -------
        Radius (m)
        """

        if superelevation is None:
            superelevation = (
                AASHTO.horizontal.maximum_superelevation
            )

        f = AASHTO.get_side_friction(design_speed)

        return (
            design_speed ** 2
            /
            (
                127
                *
                (
                    superelevation + f
                )
            )
        )


    @staticmethod
    def summary() -> Dict:

        """
        Returns all design criteria.
        """

        return {

            "driver": AASHTO.driver,

            "horizontal": AASHTO.horizontal,

            "lane": AASHTO.lane,

            "shoulder": AASHTO.shoulder,

            "median": AASHTO.median,

            "grade": AASHTO.grade,

            "traffic": AASHTO.traffic,

            "sight_distance": AASHTO.sight_distance,

            "roadside": AASHTO.roadside
        }
