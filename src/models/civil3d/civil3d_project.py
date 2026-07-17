"""
civil3d_project.py
==================

Civil 3D Project Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a Civil 3D project inside the CDT-ROP domain.

This model contains engineering data only.
No Autodesk Civil 3D API calls are allowed here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


# ==========================================================
# Civil 3D Project
# ==========================================================

@dataclass(slots=True)
class Civil3DProject:
    """
    Domain model representing a Civil 3D project.
    """

    # ------------------------------------------------------
    # Project Information
    # ------------------------------------------------------

    name: str

    file_path: Path

    drawing_name: str

    description: str = ""

    coordinate_system: str = ""

    units: str = "Metric"

    version: str = ""

    # ------------------------------------------------------
    # Engineering Objects
    # ------------------------------------------------------

    alignments: List[Any] = field(default_factory=list)

    profiles: List[Any] = field(default_factory=list)

    corridors: List[Any] = field(default_factory=list)

    assemblies: List[Any] = field(default_factory=list)

    surfaces: List[Any] = field(default_factory=list)

    sample_lines: List[Any] = field(default_factory=list)

    pipe_networks: List[Any] = field(default_factory=list)

    pressure_networks: List[Any] = field(default_factory=list)

    parcels: List[Any] = field(default_factory=list)

    feature_lines: List[Any] = field(default_factory=list)

    cogo_points: List[Any] = field(default_factory=list)

    # ------------------------------------------------------
    # Metadata
    # ------------------------------------------------------

    author: str = ""

    company: str = ""

    created_date: Optional[str] = None

    modified_date: Optional[str] = None

    # ------------------------------------------------------
    # User Properties
    # ------------------------------------------------------

    properties: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------
    # Helper Methods
    # ------------------------------------------------------

    @property
    def alignment_count(self) -> int:
        return len(self.alignments)

    @property
    def profile_count(self) -> int:
        return len(self.profiles)

    @property
    def corridor_count(self) -> int:
        return len(self.corridors)

    @property
    def surface_count(self) -> int:
        return len(self.surfaces)

    @property
    def cogo_point_count(self) -> int:
        return len(self.cogo_points)

    @property
    def pipe_network_count(self) -> int:
        return len(self.pipe_networks)
