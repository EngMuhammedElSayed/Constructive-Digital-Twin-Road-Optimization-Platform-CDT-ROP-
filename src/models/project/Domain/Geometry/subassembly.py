"""
subassembly.py
==============

Subassembly Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway corridor subassembly.

A subassembly is a reusable roadway component used
to construct roadway assemblies and corridor models.

This module stores subassembly properties only.

No corridor generation, target mapping, or geometric
processing is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass(slots=True)
class Subassembly:
    """
    Represents a roadway corridor subassembly.
    """

    # =====================================================
    # Identity
    # =====================================================

    subassembly_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Classification
    # =====================================================

    subassembly_type: str = ""
    # Lane
    # Shoulder
    # Median
    # Curb
    # Sidewalk
    # Ditch
    # Barrier
    # Daylight
    # Generic

    code: str = ""

    version: str = "1.0"

    # =====================================================
    # Geometry
    # =====================================================

    width: float = 0.0

    height: float = 0.0

    slope: float = 0.0

    offset: float = 0.0

    # =====================================================
    # References
    # =====================================================

    assembly_id: str = ""

    corridor_id: str = ""

    alignment_id: str = ""

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