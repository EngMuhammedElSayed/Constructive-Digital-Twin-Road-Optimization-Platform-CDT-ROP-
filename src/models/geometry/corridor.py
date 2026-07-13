"""
Corridor Data Model

This module defines the roadway corridor model used by the
Constructive Digital Twin Road Optimization Platform (CDT-ROP).

A Corridor represents the physical roadway generated from one or more
alignments, profiles, and assemblies.

This module contains only engineering data.
No calculations are performed here.

Author:
Eng. Muhammed

Research:
MSc Research - Cairo University
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Corridor:
    """
    Represents a roadway corridor.

    A corridor is generated from an alignment, profile,
    and assembly definition.
    """

    # -------------------------------------------------
    # General Information
    # -------------------------------------------------

    name: str

    description: str = ""

    # -------------------------------------------------
    # Corridor References
    # -------------------------------------------------

    alignment_name: str = ""

    profile_name: str = ""

    assembly_name: str = ""

    # -------------------------------------------------
    # Station Range
    # -------------------------------------------------

    start_station: float = 0.0

    end_station: float = 0.0

    length: float = 0.0

    # -------------------------------------------------
    # Corridor Configuration
    # -------------------------------------------------

    region_count: int = 1

    baseline_count: int = 1

    frequency: float = 10.0          # meters

    # -------------------------------------------------
    # Surfaces
    # -------------------------------------------------

    existing_ground_surface: str = ""

    finished_ground_surface: str = ""

    # -------------------------------------------------
    # Quantities
    # -------------------------------------------------

    corridor_volume_available: bool = False

    section_count: int = 0

    # -------------------------------------------------
    # References
    # -------------------------------------------------

    parent_project: Optional[str] = None

    source_file: Optional[str] = None
