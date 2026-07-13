"""
===============================================================================
Egyptian Highway Design Standards
===============================================================================

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

Description
-----------
This module provides engineering reference values based on the
Egyptian Code for Urban and Rural Roads.

The module contains ONLY engineering reference values.

No engineering calculations should be implemented in this module.

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

    gravity: float = 9.81


# =============================================================================
# Horizontal Alignment
# =============================================================================

@dataclass(frozen=True)
class HorizontalAlignmentCriteria:
    """
    Horizontal roadway criteria.
    """

    maximum_superelevation: float = 0.08

    side_friction = {

        30: 0.24,

        40: 0.21,

        50: 0.19,

        60: 0.17,

        70: 0.16,

        80: 0.15,

        90: 0.14,

        100: 0.13,

        110: 0.12,

        120: 0.11

    }

    minimum_radius_limit: float = 40.0


# =============================================================================
# Lane Geometry
# =============================================================================

@dataclass(frozen=True)
class LaneCriteria:

    minimum_width: float = 3.25

    recommended_width: float = 3.60

    maximum_width: float = 3.75


# =============================================================================
# Shoulder
# =============================================================================

@dataclass(frozen=True)
class ShoulderCriteria:

    minimum_width: float = 2.00

    recommended_width: float = 2.50

    maximum_width: float = 3.00


# =============================================================================
# Median
# =============================================================================

@dataclass(frozen=True)
class MedianCriteria:

    minimum_width: float = 1.50

    recommended_width: float = 5.00

    maximum_width: float = 30.00


# =============================================================================
# Longitudinal Grade
# =============================================================================

@dataclass(frozen=True)
class GradeCriteria:

    minimum_grade: float = 0.50

    maximum_grade: float = 6.00


# =============================================================================
# Traffic
# =============================================================================

@dataclass(frozen=True)
class TrafficCriteria:

    default_lane_capacity: float = 2200.0

    design_vc_limit: float = 0.90

    peak_hour_factor: float = 0.92


# =============================================================================
# Sight Distance
# =============================================================================

@dataclass(frozen=True)
class SightDistanceCriteria:

    eye_height: float = 1.08

    object_height: float = 0.60


# =============================================================================
# Roadside
# =============================================================================

@dataclass(frozen=True)
class RoadsideCriteria:

    minimum_clear_zone: float = 3.00

    recommended_clear_zone: float = 6.00


# =============================================================================
# Main Standard
# =============================================================================

class EgyptCode:
    """
    Central access point for the Egyptian Highway Code.
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

    @staticmethod
    def get_side_friction(design_speed: float) -> float:
        """
        Returns the side friction factor for a given design speed.
        """

        table = EgyptCode.horizontal.side_friction

        if design_speed in table:
            return table[design_speed]

        nearest = min(table.keys(), key=lambda x: abs(x - design_speed))

        return table[nearest]

    @staticmethod
    def minimum_radius(
        design_speed: float,
        superelevation: float = None,
    ) -> float:
        """
        Computes minimum horizontal curve radius.
        """

        if superelevation is None:
            superelevation = (
                EgyptCode.horizontal.maximum_superelevation
            )

        f = EgyptCode.get_side_friction(design_speed)

        return (
            design_speed ** 2
        ) / (
            127 * (superelevation + f)
        )

    @staticmethod
    def summary() -> Dict:
        """
        Returns all design criteria.
        """

        return {

            "driver": EgyptCode.driver,

            "horizontal": EgyptCode.horizontal,

            "lane": EgyptCode.lane,

            "shoulder": EgyptCode.shoulder,

            "median": EgyptCode.median,

            "grade": EgyptCode.grade,

            "traffic": EgyptCode.traffic,

            "sight_distance": EgyptCode.sight_distance,

            "roadside": EgyptCode.roadside,
        }
