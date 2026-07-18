"""
assembly.py
===========

Assembly Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway assembly (typical cross section).

This module stores assembly information only.

No corridor generation, target mapping, daylighting,
or subassembly processing algorithms are implemented.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass(slots=True)
class Assembly:
    """
    Represents a roadway assembly.
    """

    # =====================================================
    # Identity
    # =====================================================

    assembly_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # General
    # =====================================================

    assembly_type: str = "Road"

    width: float = 0.0

    depth: float = 0.0

    # =====================================================
    # References
    # =====================================================

    corridor_id: str = ""

    alignment_id: str = ""

    typical_section_id: str = ""

    # IDs of SubAssemblies
    subassembly_ids: List[str] = field(default_factory=list)

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