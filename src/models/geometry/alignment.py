"""
Alignment Data Model

This module defines the road alignment model used by the
Constructive Digital Twin Road Optimization Platform (CDT-ROP).

The Alignment object represents the geometric definition of a roadway
centerline. It stores only engineering data and does not perform any
calculations.

Author:
Eng. Muhammed

Research:
MSc Research - Cairo University
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Alignment:
    """
    Represents a roadway alignment.

    This model stores alignment metadata and geometric properties.
    Engineering calculations are implemented in the calculation engine.
    """

    # -------------------------------------------------
    # General Information
    # -------------------------------------------------

    name: str

    description: str = ""

    alignment_type: str = "Centerline"

    # -------------------------------------------------
    # Stationing
    # -------------------------------------------------

    start_station: float = 0.0

    end_station: float = 0.0

    length: float = 0.0

    # -------------------------------------------------
    # Design Parameters
    # -------------------------------------------------

    design_speed: float = 90.0      # km/h

    design_standard: str = "AASHTO"

    # -------------------------------------------------
    # Geometry Information
    # -------------------------------------------------

    number_of_tangents: int = 0

    number_of_horizontal_curves: int = 0

    number_of_vertical_curves: int = 0

    number_of_spirals: int = 0

    # -------------------------------------------------
    # References
    # -------------------------------------------------

    parent_project: Optional[str] = None

    source_file: Optional[str] = None
