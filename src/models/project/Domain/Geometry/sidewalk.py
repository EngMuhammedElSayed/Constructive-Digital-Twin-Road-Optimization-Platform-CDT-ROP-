"""
sidewalk.py
===========

Sidewalk Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway sidewalk.

A sidewalk is a pedestrian facility adjacent to
the roadway.

This module stores sidewalk properties only.

No accessibility analysis, pavement design,
or engineering calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass(slots=True)
class Sidewalk:
    """
    Represents a roadway sidewalk.
    """

    # =====================================================
    # Identity
    # =====================================================

    sidewalk_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Classification
    # =====================================================

    sidewalk_type: str = "Concrete"
    # Concrete
    # Asphalt
    # Pavers
    # Brick
    # Stone

    side: str = "Right"
    # Left
    # Right
    # Both

    material: str = "Concrete"

    # =====================================================
    # Geometry
    # =====================================================

    width: float = 0.0

    thickness: float = 0.0

    cross_slope: float = -2.0

    longitudinal_slope: float = 0.0

    offset: float = 0.0

    # =====================================================
    # Station Range
    # =====================================================

    start_station: float = 0.0

    end_station: float = 0.0

    length: float = 0.0

    # =====================================================
    # Accessibility
    # =====================================================

    accessible: bool = True

    tactile_paving: bool = False

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
    # Audit
    # =====================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)