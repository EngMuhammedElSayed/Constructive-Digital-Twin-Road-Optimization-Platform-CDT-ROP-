"""
cross_section.py
================

Cross Section Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway cross section.

This module stores cross-section data only.

No earthwork calculations, quantity takeoff,
section generation, or engineering algorithms
are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(slots=True)
class CrossSection:
    """
    Represents a roadway cross section.
    """

    # =====================================================
    # Identity
    # =====================================================

    section_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # References
    # =====================================================

    alignment_id: str = ""

    corridor_id: str = ""

    assembly_id: str = ""

    surface_id: str = ""

    # =====================================================
    # Station Information
    # =====================================================

    station: float = 0.0

    offset: float = 0.0

    # =====================================================
    # Geometry
    # =====================================================

    width: float = 0.0

    height: float = 0.0

    area: float = 0.0

    perimeter: float = 0.0

    # =====================================================
    # Cross Section Components
    # =====================================================

    lane_ids: List[str] = field(default_factory=list)

    shoulder_ids: List[str] = field(default_factory=list)

    sidewalk_ids: List[str] = field(default_factory=list)

    curb_ids: List[str] = field(default_factory=list)

    median_ids: List[str] = field(default_factory=list)

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)