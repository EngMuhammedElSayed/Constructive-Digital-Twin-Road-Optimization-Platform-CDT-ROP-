"""
grid_surface.py
===============

Grid Surface Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a grid-based terrain surface.

A Grid Surface stores terrain as a regularly spaced
grid of elevation values.

This module stores surface metadata only.

No interpolation, raster processing, volume
calculation, or terrain analysis is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass(slots=True)
class GridSurface:
    """
    Represents a grid-based terrain surface.
    """

    # =====================================================
    # Identity
    # =====================================================

    surface_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Grid Information
    # =====================================================

    rows: int = 0

    columns: int = 0

    cell_size_x: float = 0.0

    cell_size_y: float = 0.0

    # =====================================================
    # Elevation Range
    # =====================================================

    minimum_elevation: float = 0.0

    maximum_elevation: float = 0.0

    # =====================================================
    # Coordinate Information
    # =====================================================

    origin_x: float = 0.0

    origin_y: float = 0.0

    coordinate_system_id: str = ""

    # =====================================================
    # Data Source
    # =====================================================

    source_file: str = ""

    source_type: str = "DEM"
    # DEM
    # DSM
    # DTM
    # Raster

    # =====================================================
    # References
    # =====================================================

    project_id: str = ""

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