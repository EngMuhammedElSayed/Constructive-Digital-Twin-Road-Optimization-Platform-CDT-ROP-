"""
arc.py
======

Circular Arc Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a circular arc used in roadway geometry.

This module stores circular arc data only.

No curve calculations, station computations,
or coordinate geometry algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Arc:
    """
    Represents a circular arc.
    """

    # =====================================================
    # Identity
    # =====================================================

    arc_id: str = ""

    name: str = ""

    # =====================================================
    # Basic Geometry
    # =====================================================

    radius: float = 0.0

    length: float = 0.0

    central_angle: float = 0.0

    direction: str = "Right"   # Right / Left

    # =====================================================
    # Stations
    # =====================================================

    start_station: float = 0.0

    end_station: float = 0.0

    # =====================================================
    # Coordinates
    # =====================================================

    start_x: float = 0.0
    start_y: float = 0.0

    end_x: float = 0.0
    end_y: float = 0.0

    center_x: float = 0.0
    center_y: float = 0.0

    # =====================================================
    # References
    # =====================================================

    alignment_id: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    description: str = ""

    properties: Dict[str, str] = field(default_factory=dict)