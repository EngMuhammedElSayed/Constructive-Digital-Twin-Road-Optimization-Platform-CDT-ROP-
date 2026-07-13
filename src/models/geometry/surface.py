"""
Surface Data Model

This module defines the surface model used by the
Constructive Digital Twin Road Optimization Platform (CDT-ROP).

A Surface represents any terrain or design surface used
throughout the engineering workflow.

This module stores engineering data only.
No calculations are implemented here.

Author:
Eng. Muhammed

Research:
MSc Research - Cairo University
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Surface:
    """
    Represents a terrain or design surface.
    """

    # -------------------------------------------------
    # General Information
    # -------------------------------------------------

    name: str

    description: str = ""

    surface_type: str = "Existing Ground"

    # -------------------------------------------------
    # Coordinate System
    # -------------------------------------------------

    coordinate_system: str = ""

    units: str = "Meters"

    # -------------------------------------------------
    # Spatial Information
    # -------------------------------------------------

    area: float = 0.0

    minimum_elevation: float = 0.0

    maximum_elevation: float = 0.0

    average_elevation: float = 0.0

    # -------------------------------------------------
    # Surface Source
    # -------------------------------------------------

    source_file: Optional[str] = None

    source_format: str = ""

    # -------------------------------------------------
    # Civil 3D Information
    # -------------------------------------------------

    civil3d_surface_name: str = ""

    civil3d_object_id: Optional[str] = None

    # -------------------------------------------------
    # Digital Twin
    # -------------------------------------------------

    is_dynamic: bool = False

    last_updated: Optional[str] = None

    # -------------------------------------------------
    # References
    # -------------------------------------------------

    parent_project: Optional[str] = None
