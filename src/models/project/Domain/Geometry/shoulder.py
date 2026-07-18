"""
shoulder.py
===========

Road Shoulder Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway shoulder.

A shoulder is the portion of the roadway adjacent to
the traffic lane intended for emergency stopping,
lateral support, drainage, and maintenance access.

This module stores shoulder properties only.

No geometric design, pavement calculations,
or engineering analysis is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass(slots=True)
class Shoulder:
    """
    Represents a roadway shoulder.
    """

    # =====================================================
    # Identity
    # =====================================================

    shoulder_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Classification
    # =====================================================

    shoulder_type: str = "Paved"
    # Paved
    # Unpaved
    # Stabilized
    # Gravel
    # Emergency

    side: str = "Right"
    # Left
    # Right
    # Both

    material: str = "Asphalt"

    # =====================================================
    # Geometry
    # =====================================================

    width: float = 0.0

    cross_slope: float = -4.0

    thickness: float = 0.0

    offset: float = 0.0

    # =====================================================
    # Station Range
    # =====================================================

    start_station: float = 0.0

    end_station: float = 0.0

    length: float = 0.0

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