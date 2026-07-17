"""
document_settings.py
====================

Civil 3D Document Settings Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents Civil 3D drawing document settings.

This module stores document configuration only.
No Autodesk Civil 3D API logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(slots=True)
class DocumentSettings:
    """
    Represents Civil 3D document settings.
    """

    # =====================================================
    # Units
    # =====================================================

    drawing_units: str = "Metric"

    linear_unit: str = "Meter"

    angular_unit: str = "Degree"

    area_unit: str = "Square Meter"

    volume_unit: str = "Cubic Meter"

    # =====================================================
    # Coordinate System
    # =====================================================

    coordinate_system: str = ""

    vertical_datum: str = ""

    horizontal_datum: str = ""

    # =====================================================
    # Drawing Configuration
    # =====================================================

    annotation_scale: str = "1:1000"

    insertion_scale: str = "Meters"

    precision: int = 3

    # =====================================================
    # Styles
    # =====================================================

    alignment_style: str = ""

    profile_style: str = ""

    corridor_style: str = ""

    surface_style: str = ""

    label_set_style: str = ""

    # =====================================================
    # Layers
    # =====================================================

    default_layer: str = "0"

    layer_standard: str = ""

    layers: List[str] = field(default_factory=list)

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)