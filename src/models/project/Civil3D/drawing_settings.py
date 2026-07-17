"""
drawing_settings.py
===================

Civil 3D Drawing Settings Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents drawing settings used by Civil 3D.

This module contains drawing configuration only.
No Autodesk Civil 3D API logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class DrawingSettings:
    """
    Represents Civil 3D drawing settings.
    """

    # =====================================================
    # Drawing Information
    # =====================================================

    drawing_name: str = ""

    template_name: str = ""

    drawing_scale: str = "1:1000"

    drawing_units: str = "Metric"

    # =====================================================
    # Coordinate System
    # =====================================================

    coordinate_system: str = ""

    horizontal_datum: str = ""

    vertical_datum: str = ""

    # =====================================================
    # Precision
    # =====================================================

    linear_precision: int = 3

    angular_precision: int = 4

    elevation_precision: int = 3

    station_precision: int = 2

    # =====================================================
    # Annotation
    # =====================================================

    annotation_scale: str = "1:1000"

    text_style: str = ""

    dimension_style: str = ""

    multileader_style: str = ""

    # =====================================================
    # Display
    # =====================================================

    background_color: str = "Black"

    grid_enabled: bool = False

    snap_enabled: bool = False

    ortho_enabled: bool = False

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)