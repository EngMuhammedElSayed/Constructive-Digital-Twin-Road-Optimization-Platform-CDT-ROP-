"""
surface.py
==========

Surface Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the base domain model for all terrain and
roadway surfaces.

A surface may represent existing terrain, proposed
design, corridor models, or raster-based elevation
models.

This module stores surface metadata only.

No triangulation, interpolation, contour generation,
volume calculation, or terrain analysis is implemented
here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass(slots=True)
class Surface:
    """
    Base surface domain model.
    """

    # =====================================================
    # Identity
    # =====================================================

    surface_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Surface Classification
    # =====================================================

    surface_type: str = "Existing Ground"
    # Existing Ground
    # Finished Ground
    # TIN
    # Grid
    # Corridor
    # DEM
    # DTM
    # DSM

    source_type: str = "Civil3D"
    # Civil3D
    # OpenRoads
    # LandXML
    # DEM
    # LiDAR
    # Survey
    # GIS

    # =====================================================
    # Elevation Information
    # =====================================================

    minimum_elevation: float = 0.0

    maximum_elevation: float = 0.0

    average_elevation: float = 0.0

    # =====================================================
    # Spatial Extent
    # =====================================================

    minimum_x: float = 0.0

    minimum_y: float = 0.0

    maximum_x: float = 0.0

    maximum_y: float = 0.0

    # =====================================================
    # References
    # =====================================================

    coordinate_system_id: str = ""

    alignment_id: str = ""

    corridor_id: str = ""

    project_id: str = ""

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