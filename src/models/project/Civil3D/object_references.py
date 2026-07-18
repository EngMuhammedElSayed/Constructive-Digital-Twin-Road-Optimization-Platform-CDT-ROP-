"""
object_references.py
====================

Civil 3D Object References Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Stores references to Civil 3D objects contained in a DWG.

This module contains references only.
No Autodesk Civil 3D API logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(slots=True)
class ObjectReferences:
    """
    References to Civil 3D objects.
    """

    # =====================================================
    # Alignment Objects
    # =====================================================

    alignment_ids: List[str] = field(default_factory=list)

    offset_alignment_ids: List[str] = field(default_factory=list)

    # =====================================================
    # Profile Objects
    # =====================================================

    profile_ids: List[str] = field(default_factory=list)

    profile_view_ids: List[str] = field(default_factory=list)

    # =====================================================
    # Corridor Objects
    # =====================================================

    corridor_ids: List[str] = field(default_factory=list)

    assembly_ids: List[str] = field(default_factory=list)

    region_ids: List[str] = field(default_factory=list)

    # =====================================================
    # Surface Objects
    # =====================================================

    surface_ids: List[str] = field(default_factory=list)

    tin_surface_ids: List[str] = field(default_factory=list)

    grid_surface_ids: List[str] = field(default_factory=list)

    # =====================================================
    # Section Objects
    # =====================================================

    sample_line_group_ids: List[str] = field(default_factory=list)

    sample_line_ids: List[str] = field(default_factory=list)

    section_view_ids: List[str] = field(default_factory=list)

    # =====================================================
    # Pipe Network
    # =====================================================

    pipe_network_ids: List[str] = field(default_factory=list)

    pipe_ids: List[str] = field(default_factory=list)

    structure_ids: List[str] = field(default_factory=list)

    # =====================================================
    # Feature Objects
    # =====================================================

    feature_line_ids: List[str] = field(default_factory=list)

    grading_ids: List[str] = field(default_factory=list)

    parcel_ids: List[str] = field(default_factory=list)

    # =====================================================
    # Metadata
    # =====================================================

    custom_references: Dict[str, str] = field(default_factory=dict)