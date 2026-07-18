"""
corridor.py
===========

Corridor Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway corridor.

A corridor combines an alignment, profile, and one or
more assemblies to describe the roadway model.

This module stores corridor data only.

No corridor modelling, daylighting, surface generation,
or engineering calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass(slots=True)
class Corridor:
    """
    Represents a roadway corridor.
    """

    # =====================================================
    # Identity
    # =====================================================

    corridor_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # References
    # =====================================================

    alignment_id: str = ""

    profile_id: str = ""

    surface_id: str = ""

    coordinate_system_id: str = ""

    # Corridor regions (station ranges)
    region_ids: List[str] = field(default_factory=list)

    # Assemblies used within the corridor
    assembly_ids: List[str] = field(default_factory=list)

    # =====================================================
    # Station Range
    # =====================================================

    start_station: float = 0.0

    end_station: float = 0.0

    length: float = 0.0

    # =====================================================
    # Sampling
    # =====================================================

    frequency: float = 10.0

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