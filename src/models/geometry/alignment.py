"""
alignment.py
============

Horizontal Alignment Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway horizontal alignment.

This module contains engineering data only.
No geometric calculations are performed here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List
from uuid import uuid4


@dataclass(slots=True)
class Alignment:
    """
    Represents a roadway horizontal alignment.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""

    description: str = ""

    # =====================================================
    # General
    # =====================================================

    station_start: float = 0.0

    station_end: float = 0.0

    total_length_m: float = 0.0

    design_speed_kph: float = 90.0

    # =====================================================
    # Geometry
    # =====================================================

    pi_points: List[Any] = field(default_factory=list)

    tangents: List[Any] = field(default_factory=list)

    circular_curves: List[Any] = field(default_factory=list)

    transition_curves: List[Any] = field(default_factory=list)

    stations: List[Any] = field(default_factory=list)

    # =====================================================
    # Design Parameters
    # =====================================================

    minimum_radius_m: float = 0.0

    maximum_superelevation: float = 0.06

    maximum_side_friction: float = 0.13

    lane_count: int = 4

    lane_width_m: float = 3.65

    # =====================================================
    # Coordinate System
    # =====================================================

    coordinate_system: str = ""

    units: str = "Metric"

    # =====================================================
    # Metadata
    # =====================================================

    source: str = ""

    author: str = ""

    version: str = "1.0"

    properties: Dict[str, Any] = field(default_factory=dict)

    # =====================================================
    # Helper Properties
    # =====================================================

    @property
    def pi_count(self) -> int:
        return len(self.pi_points)

    @property
    def tangent_count(self) -> int:
        return len(self.tangents)

    @property
    def curve_count(self) -> int:
        return len(self.circular_curves)

    @property
    def transition_count(self) -> int:
        return len(self.transition_curves)