"""
profile.py
==========

Vertical Profile Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway vertical profile.

This module contains engineering data only.
No profile calculations are performed here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List
from uuid import uuid4


@dataclass(slots=True)
class Profile:
    """
    Represents a roadway vertical profile.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""

    description: str = ""

    # =====================================================
    # References
    # =====================================================

    alignment_id: str = ""

    surface_id: str = ""

    # =====================================================
    # Stations
    # =====================================================

    start_station: float = 0.0

    end_station: float = 0.0

    total_length_m: float = 0.0

    # =====================================================
    # Profile Geometry
    # =====================================================

    pv_is: List[Any] = field(default_factory=list)

    tangents: List[Any] = field(default_factory=list)

    vertical_curves: List[Any] = field(default_factory=list)

    stations: List[Any] = field(default_factory=list)

    # =====================================================
    # Design Parameters
    # =====================================================

    maximum_grade_percent: float = 0.0

    minimum_grade_percent: float = 0.0

    minimum_crest_k: float = 0.0

    minimum_sag_k: float = 0.0

    # =====================================================
    # Metadata
    # =====================================================

    source: str = ""

    author: str = ""

    version: str = "1.0"

    properties: Dict[str, Any] = field(default_factory=dict)

    # =====================================================
    # Helper Properties
    # =====================================================

    @property
    def pvi_count(self) -> int:
        return len(self.pv_is)

    @property
    def tangent_count(self) -> int:
        return len(self.tangents)

    @property
    def vertical_curve_count(self) -> int:
        return len(self.vertical_curves)