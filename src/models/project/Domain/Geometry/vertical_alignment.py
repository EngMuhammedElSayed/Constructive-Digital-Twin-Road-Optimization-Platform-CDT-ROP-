"""
vertical_alignment.py
=====================

Vertical Alignment Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the vertical alignment of a roadway.

A vertical alignment defines the roadway elevation
along an alignment using grades, PVIs, and
vertical curves.

This module stores vertical alignment data only.

No vertical curve computation, grading analysis,
earthwork calculations, or engineering design
algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass(slots=True)
class VerticalAlignment:
    """
    Represents a roadway vertical alignment.
    """

    # =====================================================
    # Identity
    # =====================================================

    vertical_alignment_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # References
    # =====================================================

    alignment_id: str = ""

    profile_id: str = ""

    existing_surface_id: str = ""

    proposed_surface_id: str = ""

    # =====================================================
    # Station Limits
    # =====================================================

    start_station: float = 0.0

    end_station: float = 0.0

    total_length: float = 0.0

    # =====================================================
    # Design Criteria
    # =====================================================

    design_speed: float = 90.0

    minimum_grade: float = 0.0

    maximum_grade: float = 0.0

    # =====================================================
    # Geometry References
    # =====================================================

    pvi_ids: List[str] = field(default_factory=list)

    vertical_curve_ids: List[str] = field(default_factory=list)

    grade_ids: List[str] = field(default_factory=list)

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