"""
cross_section.py
================

Cross Section Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway cross section.

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
class CrossSection:
    """
    Represents a roadway cross section.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""

    description: str = ""

    # =====================================================
    # Station
    # =====================================================

    station: float = 0.0

    offset_left_m: float = 0.0

    offset_right_m: float = 0.0

    # =====================================================
    # Roadway Geometry
    # =====================================================

    carriageway_width_m: float = 0.0

    lane_width_m: float = 3.65

    lane_count: int = 4

    shoulder_width_left_m: float = 0.0

    shoulder_width_right_m: float = 0.0

    median_width_m: float = 0.0

    sidewalk_width_left_m: float = 0.0

    sidewalk_width_right_m: float = 0.0

    # =====================================================
    # Slopes
    # =====================================================

    cross_slope_left_percent: float = 2.0

    cross_slope_right_percent: float = 2.0

    side_slope_left: float = 2.0

    side_slope_right: float = 2.0

    # =====================================================
    # Elevations
    # =====================================================

    centerline_elevation_m: float = 0.0

    left_edge_elevation_m: float = 0.0

    right_edge_elevation_m: float = 0.0

    # =====================================================
    # Corridor Elements
    # =====================================================

    links: List[Any] = field(default_factory=list)

    shapes: List[Any] = field(default_factory=list)

    points: List[Any] = field(default_factory=list)

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
    def total_width(self) -> float:
        """
        Total cross section width.
        """
        return self.offset_left_m + self.offset_right_m

    @property
    def link_count(self) -> int:
        return len(self.links)

    @property
    def shape_count(self) -> int:
        return len(self.shapes)

    @property
    def point_count(self) -> int:
        return len(self.points)
