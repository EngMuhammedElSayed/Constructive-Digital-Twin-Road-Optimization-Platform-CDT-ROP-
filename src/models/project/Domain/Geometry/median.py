"""
median.py
=========

Median Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway median.

A median separates opposing directions of traffic and
may contain barriers, landscaping, drainage elements,
or other roadway features.

This module stores median data only.

No roadway design, traffic analysis, or engineering
calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass(slots=True)
class Median:
    """
    Represents a roadway median.
    """

    # =====================================================
    # Identity
    # =====================================================

    median_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Classification
    # =====================================================

    median_type: str = "Raised"
    # Raised
    # Depressed
    # Flush
    # Barrier
    # Landscaped

    material: str = ""

    # =====================================================
    # Geometry
    # =====================================================

    width: float = 0.0

    height: float = 0.0

    cross_slope: float = 0.0

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