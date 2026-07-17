"""
surface.py
==========

Surface Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a terrain or roadway surface.

This module contains engineering data only.
No surface calculations are performed here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List
from uuid import uuid4


@dataclass(slots=True)
class Surface:
    """
    Represents a terrain or roadway surface.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""

    description: str = ""

    # =====================================================
    # Surface Information
    # =====================================================

    surface_type: str = "TIN"

    source: str = ""

    coordinate_system: str = ""

    units: str = "Metric"

    # =====================================================
    # Geometry
    # =====================================================

    vertices: List[Any] = field(default_factory=list)

    triangles: List[Any] = field(default_factory=list)

    breaklines: List[Any] = field(default_factory=list)

    boundaries: List[Any] = field(default_factory=list)

    contours: List[Any] = field(default_factory=list)

    # =====================================================
    # Extents
    # =====================================================

    minimum_elevation_m: float = 0.0

    maximum_elevation_m: float = 0.0

    average_elevation_m: float = 0.0

    area_m2: float = 0.0

    # =====================================================
    # Metadata
    # =====================================================

    author: str = ""

    version: str = "1.0"

    properties: Dict[str, Any] = field(default_factory=dict)

    # =====================================================
    # Helper Properties
    # =====================================================

    @property
    def vertex_count(self) -> int:
        return len(self.vertices)

    @property
    def triangle_count(self) -> int:
        return len(self.triangles)

    @property
    def breakline_count(self) -> int:
        return len(self.breaklines)

    @property
    def contour_count(self) -> int:
        return len(self.contours)