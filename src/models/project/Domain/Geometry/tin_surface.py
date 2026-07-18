"""
tin_surface.py
==============

TIN Surface Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a Triangulated Irregular Network (TIN)
surface used in roadway engineering.

A TIN surface consists of irregularly distributed
survey points connected by triangular faces.

This module stores TIN surface metadata only.

No triangulation, interpolation, contour generation,
volume computation, or terrain analysis is implemented
here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass

from .surface import Surface


@dataclass(slots=True)
class TINSurface(Surface):
    """
    Represents a TIN surface.
    """

    # =====================================================
    # TIN Statistics
    # =====================================================

    point_count: int = 0

    triangle_count: int = 0

    breakline_count: int = 0

    boundary_count: int = 0

    # =====================================================
    # Source Information
    # =====================================================

    has_breaklines: bool = False

    has_boundaries: bool = False

    has_voids: bool = False

    # =====================================================
    # Surface Quality
    # =====================================================

    average_triangle_area: float = 0.0

    maximum_triangle_area: float = 0.0

    minimum_triangle_area: float = 0.0