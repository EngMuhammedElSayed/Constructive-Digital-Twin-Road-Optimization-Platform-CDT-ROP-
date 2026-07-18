"""
lane.py
=======

Lane Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway traffic lane.

This module stores lane geometry and descriptive
properties only.

No traffic simulation, capacity analysis,
or roadway design calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass(slots=True)
class Lane:
    """
    Represents a roadway traffic lane.
    """

    # =====================================================
    # Identity
    # =====================================================

    lane_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Classification
    # =====================================================

    lane_type: str = "Driving"
    # Driving
    # Passing
    # Climbing
    # Turning
    # Auxiliary
    # Shoulder
    # Bus
    # Bicycle
    # Parking

    side: str = "Right"
    # Left / Right / Center

    direction: str = "Forward"
    # Forward / Reverse / Bidirectional

    # =====================================================
    # Geometry
    # =====================================================

    width: float = 3.65

    cross_slope: float = -2.0

    superelevation: float = 0.0

    offset: float = 0.0

    # =====================================================
    # Station Limits
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