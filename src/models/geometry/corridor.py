"""
corridor.py
===========

Road Corridor Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway corridor.

This module contains engineering data only.
No corridor modelling or Civil 3D logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List
from uuid import uuid4


@dataclass(slots=True)
class Corridor:
    """
    Represents a roadway corridor.
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

    profile_id: str = ""

    assembly_id: str = ""

    baseline_name: str = ""

    # =====================================================
    # Stations
    # =====================================================

    start_station: float = 0.0

    end_station: float = 0.0

    length_m: float = 0.0

    # =====================================================
    # Corridor Components
    # =====================================================

    regions: List[Any] = field(default_factory=list)

    targets: List[Any] = field(default_factory=list)

    feature_lines: List[Any] = field(default_factory=list)

    surfaces: List[Any] = field(default_factory=list)

    sample_lines: List[Any] = field(default_factory=list)

    # =====================================================
    # Design Parameters
    # =====================================================

    frequency_along_tangent_m: float = 10.0

    frequency_along_curve_m: float = 5.0

    frequency_along_spiral_m: float = 5.0

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
    def region_count(self) -> int:
        return len(self.regions)

    @property
    def surface_count(self) -> int:
        return len(self.surfaces)

    @property
    def feature_line_count(self) -> int:
        return len(self.feature_lines)

    @property
    def target_count(self) -> int:
        return len(self.targets)