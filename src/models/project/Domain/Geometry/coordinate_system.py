"""
coordinate_system.py
====================

Coordinate System Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the spatial reference system used by
road geometry and project datasets.

This module stores coordinate system metadata only.

No coordinate transformation, projection, or
geodetic computations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class CoordinateSystem:
    """
    Represents a spatial reference system.
    """

    # =====================================================
    # Identity
    # =====================================================

    name: str = ""

    description: str = ""

    # =====================================================
    # Reference System
    # =====================================================

    epsg_code: int = 0

    authority: str = "EPSG"

    datum: str = ""

    projection: str = ""

    geoid_model: str = ""

    # =====================================================
    # Units
    # =====================================================

    horizontal_unit: str = "meter"

    vertical_unit: str = "meter"

    angular_unit: str = "degree"

    # =====================================================
    # Coordinate Information
    # =====================================================

    coordinate_type: str = "Projected"
    # Examples:
    # Projected
    # Geographic
    # Local

    zone: str = ""

    hemisphere: str = ""

    # =====================================================
    # References
    # =====================================================

    source: str = ""

    remarks: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)