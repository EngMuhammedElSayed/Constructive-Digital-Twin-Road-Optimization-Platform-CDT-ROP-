"""
alignment_station.py
====================

Alignment Station Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a station (chainage) along a roadway alignment.

This module stores station-related data only.

No station equations, chainage calculations,
or coordinate transformations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class AlignmentStation:
    """
    Represents a station (chainage) on a roadway alignment.
    """

    # =====================================================
    # Station Information
    # =====================================================

    station: float = 0.0

    station_label: str = ""

    description: str = ""

    # =====================================================
    # Coordinates
    # =====================================================

    x: float = 0.0

    y: float = 0.0

    z: float = 0.0

    # =====================================================
    # Geometry
    # =====================================================

    offset: float = 0.0

    elevation: float = 0.0

    bearing: float = 0.0

    # =====================================================
    # Alignment Reference
    # =====================================================

    alignment_id: str = ""

    region: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)