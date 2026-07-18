"""
profile.py
==========

Vertical Profile Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway vertical profile.

A profile defines roadway elevations along an
alignment using grades and PVIs.

This module stores profile data only.

No vertical alignment design, grading calculations,
or engineering algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass(slots=True)
class Profile:
    """
    Represents a roadway vertical profile.
    """

    # =====================================================
    # Identity
    # =====================================================

    profile_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # References
    # =====================================================

    alignment_id: str = ""

    coordinate_system_id: str = ""

    existing_surface_id: str = ""

    proposed_surface_id: str = ""

    # =====================================================
    # Station Range
    # =====================================================

    start_station: float = 0.0

    end_station: float = 0.0

    total_length: float = 0.0

    # =====================================================
    # Vertical Elements
    # =====================================================

    pvi_ids: List[str] = field(default_factory=list)

    grade_ids: List[str] = field(default_factory=list)

    vertical_curve_ids: List[str] = field(default_factory=list)

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