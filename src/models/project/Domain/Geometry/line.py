"""
line.py
=======

Line Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a straight line (tangent) used in roadway
horizontal alignment.

This module stores line geometry only.

No coordinate geometry, bearing calculations,
or engineering algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Line:
    """
    Represents a straight tangent line.
    """

    # =====================================================
    # Identity
    # =====================================================

    line_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Station Range
    # =====================================================

    start_station: float = 0.0

    end_station: float = 0.0

    length: float = 0.0

    # =====================================================
    # Coordinates
    # =====================================================

    start_x: float = 0.0

    start_y: float = 0.0

    end_x: float = 0.0

    end_y: float = 0.0

    # =====================================================
    # Direction
    # =====================================================

    azimuth: float = 0.0

    bearing: float = 0.0

    # =====================================================
    # References
    # =====================================================

    alignment_id: str = ""

    horizontal_alignment_id: str = ""

    # =====================================================
    # Status
    # =====================================================

    active: bool = True

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)