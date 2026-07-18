"""
geometry_metadata.py
====================

Geometry Metadata Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents metadata associated with geometry objects.

This module stores descriptive and management
information only.

No engineering calculations or geometry processing
are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass(slots=True)
class GeometryMetadata:
    """
    Represents metadata for any geometry object.
    """

    # =====================================================
    # Identity
    # =====================================================

    object_id: str = ""

    object_name: str = ""

    object_type: str = ""
    # Examples:
    # Alignment
    # Corridor
    # Surface
    # Profile
    # CrossSection
    # Assembly

    # =====================================================
    # Version Information
    # =====================================================

    version: str = "1.0.0"

    revision: int = 1

    status: str = "Draft"
    # Draft / Review / Approved / Archived

    # =====================================================
    # Author Information
    # =====================================================

    created_by: str = ""

    modified_by: str = ""

    organization: str = ""

    # =====================================================
    # Dates
    # =====================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    modified_at: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # External References
    # =====================================================

    source_file: str = ""

    source_application: str = ""

    external_id: str = ""

    # =====================================================
    # Description
    # =====================================================

    description: str = ""

    remarks: str = ""

    # =====================================================
    # User Defined Properties
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)