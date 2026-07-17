"""
road_geometry.py
================

Road Geometry Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the complete roadway geometry model.

This module aggregates all geometric components of
a roadway project.

No engineering calculations are performed here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict
from uuid import uuid4

from src.models.geometry.alignment import Alignment
from src.models.geometry.profile import Profile
from src.models.geometry.corridor import Corridor
from src.models.geometry.cross_section import CrossSection


@dataclass(slots=True)
class RoadGeometry:
    """
    Represents the complete roadway geometry.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""

    description: str = ""

    # =====================================================
    # Main Geometry Components
    # =====================================================

    alignment: Alignment = field(default_factory=Alignment)

    profile: Profile = field(default_factory=Profile)

    corridor: Corridor = field(default_factory=Corridor)

    cross_sections: list[CrossSection] = field(default_factory=list)

    # =====================================================
    # Global Parameters
    # =====================================================

    design_speed_kph: float = 90.0

    total_length_m: float = 0.0

    station_start: float = 0.0

    station_end: float = 0.0

    coordinate_system: str = ""

    units: str = "Metric"

    # =====================================================
    # Metadata
    # =====================================================

    source: str = ""

    author: str = ""

    version: str = "1.0"

    properties: Dict[str, str] = field(default_factory=dict)

    # =====================================================
    # Helper Properties
    # =====================================================

    @property
    def cross_section_count(self) -> int:
        return len(self.cross_sections)

    @property
    def has_alignment(self) -> bool:
        return self.alignment is not None

    @property
    def has_profile(self) -> bool:
        return self.profile is not None

    @property
    def has_corridor(self) -> bool:
        return self.corridor is not None