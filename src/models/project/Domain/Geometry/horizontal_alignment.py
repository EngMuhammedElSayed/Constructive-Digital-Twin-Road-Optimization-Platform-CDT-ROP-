"""
horizontal_alignment.py
=======================

Horizontal Alignment Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the horizontal alignment of a roadway.

The horizontal alignment consists of tangents,
circular curves, and transition spirals.

This module stores alignment data only.

No geometric calculations, curve fitting,
or station computations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass(slots=True)
class HorizontalAlignment:
    """
    Represents a roadway horizontal alignment.
    """

    # =====================================================
    # Identity
    # =====================================================

    horizontal_alignment_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # References
    # =====================================================

    alignment_id: str = ""

    coordinate_system_id: str = ""

    # =====================================================
    # Station Range
    # =====================================================

    start_station: float = 0.0

    end_station: float = 0.0

    total_length: float = 0.0

    # =====================================================
    # Horizontal Elements
    # =====================================================

    tangent_ids: List[str] = field(default_factory=list)

    arc_ids: List[str] = field(default_factory=list)

    spiral_ids: List[str] = field(default_factory=list)

    pi_station_ids: List[str] = field(default_factory=list)

    # =====================================================
    # General Properties
    # =====================================================

    design_speed: float = 90.0

    active: bool = True

    # =====================================================
    # Audit
    # =====================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)