"""
geometry_extent.py
==================

Geometry Extent Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the spatial extent (bounding box) of
geometry contained within a project.

This module stores spatial boundary information only.

No spatial analysis, coordinate transformation,
or extent calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class GeometryExtent:
    """
    Represents the spatial extent of project geometry.
    """

    # =====================================================
    # Horizontal Extent
    # =====================================================

    min_x: float = 0.0

    max_x: float = 0.0

    min_y: float = 0.0

    max_y: float = 0.0

    # =====================================================
    # Vertical Extent
    # =====================================================

    min_z: float = 0.0

    max_z: float = 0.0

    # =====================================================
    # Coordinate System
    # =====================================================

    coordinate_system_id: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    description: str = ""

    properties: Dict[str, str] = field(default_factory=dict)

    # =====================================================
    # Read-Only Properties
    # =====================================================

    @property
    def width(self) -> float:
        """Returns the horizontal width of the extent."""
        return self.max_x - self.min_x

    @property
    def height(self) -> float:
        """Returns the horizontal height of the extent."""
        return self.max_y - self.min_y

    @property
    def elevation_range(self) -> float:
        """Returns the vertical elevation range."""
        return self.max_z - self.min_z