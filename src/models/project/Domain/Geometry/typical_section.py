"""
typical_section.py
==================

Typical Section Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway typical cross section.

A typical section defines the standard arrangement
of roadway components such as lanes, shoulders,
medians, curbs, sidewalks, and subassemblies.

This module stores typical section data only.

No corridor generation, quantity computation,
or geometric calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass(slots=True)
class TypicalSection:
    """
    Represents a roadway typical section.
    """

    # =====================================================
    # Identity
    # =====================================================

    typical_section_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # References
    # =====================================================

    alignment_id: str = ""

    corridor_id: str = ""

    assembly_id: str = ""

    # =====================================================
    # Station Range
    # =====================================================

    start_station: float = 0.0

    end_station: float = 0.0

    # =====================================================
    # Components
    # =====================================================

    lane_ids: List[str] = field(default_factory=list)

    shoulder_ids: List[str] = field(default_factory=list)

    median_ids: List[str] = field(default_factory=list)

    curb_ids: List[str] = field(default_factory=list)

    sidewalk_ids: List[str] = field(default_factory=list)

    subassembly_ids: List[str] = field(default_factory=list)

    # =====================================================
    # General Properties
    # =====================================================

    roadway_width: float = 0.0

    pavement_width: float = 0.0

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