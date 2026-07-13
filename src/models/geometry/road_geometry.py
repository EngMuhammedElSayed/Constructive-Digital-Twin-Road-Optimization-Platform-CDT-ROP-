"""
Road Geometry Data Model

This module defines the roadway cross-section geometry used by the
Constructive Digital Twin Road Optimization Platform (CDT-ROP).

The model stores geometric design parameters only.
No engineering calculations are performed here.

Author:
Eng. Muhammed

Research:
MSc Research - Cairo University
"""

from dataclasses import dataclass


@dataclass
class RoadGeometry:
    """
    Represents the typical roadway cross-section.

    This class stores the geometric design parameters that define
    the roadway layout.
    """

    # -------------------------------------------------
    # General
    # -------------------------------------------------

    road_name: str = ""

    road_classification: str = "Urban Freeway"

    design_speed: float = 90.0      # km/h

    # -------------------------------------------------
    # Lane Configuration
    # -------------------------------------------------

    lanes_per_direction: int = 4

    lane_width: float = 3.60        # m

    shoulder_width: float = 2.50    # m

    median_width: float = 4.00      # m

    # -------------------------------------------------
    # Cross Section
    # -------------------------------------------------

    cross_slope: float = 0.02

    maximum_superelevation: float = 0.06

    side_slope: float = 2.0         # H:V

    clear_zone_width: float = 6.00  # m

    # -------------------------------------------------
    # Pavement
    # -------------------------------------------------

    pavement_width: float = 0.0

    total_roadway_width: float = 0.0

    # -------------------------------------------------
    # Design Limits
    # -------------------------------------------------

    minimum_lane_width: float = 3.00

    maximum_lane_width: float = 3.75

    minimum_shoulder_width: float = 1.20

    maximum_shoulder_width: float = 3.00
