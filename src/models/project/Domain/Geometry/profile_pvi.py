"""
profile_pvi.py
==============

Profile PVI Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a Point of Vertical Intersection (PVI)
within a roadway vertical profile.

This module stores PVI data only.

No vertical curve calculations, grading,
or profile analysis are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class ProfilePVI:
    """
    Represents a Point of Vertical Intersection (PVI).
    """

    # =====================================================
    # Identity
    # =====================================================

    pvi_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Station & Elevation
    # =====================================================

    station: float = 0.0

    elevation: float = 0.0

    # =====================================================
    # Incoming / Outgoing Grades
    # =====================================================

    incoming_grade: float = 0.0

    outgoing_grade: float = 0.0

    grade_difference: float = 0.0

    # =====================================================
    # Vertical Curve
    # =====================================================

    vertical_curve_length: float = 0.0

    vertical_curve_type: str = ""
    # Crest
    # Sag

    # =====================================================
    # References
    # =====================================================

    profile_id: str = ""

    alignment_id: str = ""

    # =====================================================
    # Status
    # =====================================================

    active: bool = True

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)