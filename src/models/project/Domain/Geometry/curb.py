"""
curb.py
=======

Curb Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway curb element.

This module stores curb geometry and metadata only.

No curb design, quantity takeoff, drainage analysis,
or construction calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Curb:
    """
    Represents a roadway curb.
    """

    # =====================================================
    # Identity
    # =====================================================

    curb_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Type
    # =====================================================

    curb_type: str = "Barrier"
    # Examples:
    # Barrier
    # Mountable
    # Rolled
    # Integral
    # Extruded

    material: str = "Concrete"

    # =====================================================
    # Dimensions
    # =====================================================

    width: float = 0.0

    height: float = 0.0

    length: float = 0.0

    slope: float = 0.0

    # =====================================================
    # Location
    # =====================================================

    side: str = "Right"
    # Left / Right / Center

    station_start: float = 0.0

    station_end: float = 0.0

    offset: float = 0.0

    # =====================================================
    # References
    # =====================================================

    alignment_id: str = ""

    corridor_id: str = ""

    assembly_id: str = ""

    cross_section_id: str = ""

    # =====================================================
    # Status
    # =====================================================

    active: bool = True

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)