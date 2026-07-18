"""
spiral.py
=========

Transition Spiral Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a horizontal transition spiral.

A transition spiral provides a gradual change in
curvature between a tangent and a circular curve.

This module stores spiral properties only.

No clothoid calculations, superelevation
development, or engineering computations are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Spiral:
    """
    Represents a roadway transition spiral.
    """

    # =====================================================
    # Identity
    # =====================================================

    spiral_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Spiral Classification
    # =====================================================

    spiral_type: str = "Clothoid"
    # Clothoid
    # Bloss
    # Cubic
    # Sine

    direction: str = "Left"
    # Left
    # Right

    # =====================================================
    # Stationing
    # =====================================================

    start_station: float = 0.0

    end_station: float = 0.0

    length: float = 0.0

    # =====================================================
    # Radius
    # =====================================================

    start_radius: float = 0.0

    end_radius: float = 0.0

    # =====================================================
    # Design Parameters
    # =====================================================

    design_speed: float = 90.0

    design_radius: float = 0.0

    # =====================================================
    # References
    # =====================================================

    alignment_id: str = ""

    horizontal_alignment_id: str = ""

    incoming_line_id: str = ""

    outgoing_arc_id: str = ""

    # =====================================================
    # Status
    # =====================================================

    active: bool = True

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)