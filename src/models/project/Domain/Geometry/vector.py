"""
vector.py
=========

Vector Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a 3D vector used throughout the roadway
geometry domain.

This module stores vector data only.

No vector algebra, transformations, projections,
or geometric computations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Vector:
    """
    Represents a three-dimensional vector.
    """

    # =====================================================
    # Identity
    # =====================================================

    vector_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Components
    # =====================================================

    x: float = 0.0

    y: float = 0.0

    z: float = 0.0

    # =====================================================
    # Classification
    # =====================================================

    vector_type: str = "Generic"
    # Generic
    # Direction
    # Normal
    # Tangent
    # Binormal

    # =====================================================
    # Reference
    # =====================================================

    coordinate_system_id: str = ""

    # =====================================================
    # Status
    # =====================================================

    active: bool = True

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)