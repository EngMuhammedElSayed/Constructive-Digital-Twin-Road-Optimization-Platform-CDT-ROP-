"""
alignment.py
============

Alignment Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the primary roadway alignment.

This module stores alignment data only.

No geometric computations, station calculations,
curve generation, or engineering algorithms are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List

from .alignment_station import AlignmentStation


@dataclass(slots=True)
class Alignment:
    """
    Represents a roadway alignment.
    """

    # =====================================================
    # Identity
    # =====================================================

    alignment_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # General
    # =====================================================

    design_speed: float = 90.0

    length: float = 0.0

    start_station: float = 0.0

    end_station: float = 0.0

    # =====================================================
    # Geometry
    # =====================================================

    stations: List[AlignmentStation] = field(default_factory=list)

    # =====================================================
    # References
    # =====================================================

    horizontal_alignment_id: str = ""

    vertical_alignment_id: str = ""

    profile_id: str = ""

    corridor_id: str = ""

    surface_id: str = ""

    coordinate_system: str = ""

    # =====================================================
    # Status
    # =====================================================

    active: bool = True

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)