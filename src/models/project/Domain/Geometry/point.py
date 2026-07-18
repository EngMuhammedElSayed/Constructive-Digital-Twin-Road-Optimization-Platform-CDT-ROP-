"""
point.py
========

Point Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a 3D point used throughout the roadway model.

This module stores point data only.

No coordinate transformation, distance calculation,
or geometric processing is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Point:
    """
    Represents a 3D point.
    """

    # =====================================================
    # Identity
    # =====================================================

    point_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Coordinates
    # =====================================================

    x: float = 0.0

    y: float = 0.0

    z: float = 0.0

    # =====================================================
    # Station Information
    # =====================================================

    station: float = 0.0

    offset: float = 0.0

    # =====================================================
    # Point Classification
    # =====================================================

    point_type: str = "Generic"
    # Generic
    # PI
    # PC
    # PT
    # TS
    # SC
    # CS
    # ST
    # Survey
    # Surface
    # Corridor
    # Control

    # =====================================================
    # Coordinate System
    # =====================================================

    coordinate_system_id: str = ""

    # =====================================================
    # References
    # =====================================================

    alignment_id: str = ""

    surface_id: str = ""

    corridor_id: str = ""

    # =====================================================
    # Status
    # =====================================================

    active: bool = True

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)