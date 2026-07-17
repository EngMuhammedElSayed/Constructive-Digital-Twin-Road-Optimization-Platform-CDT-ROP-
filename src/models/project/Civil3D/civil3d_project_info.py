"""
civil3d_project_info.py
=======================

Civil 3D Project Information Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents general information about a Civil 3D project.

This module stores metadata only.
No Autodesk Civil 3D API logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict
from uuid import uuid4


@dataclass(slots=True)
class Civil3DProjectInfo:
    """
    General information describing a Civil 3D project.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    project_name: str = ""

    drawing_name: str = ""

    drawing_path: Path | None = None

    project_directory: Path | None = None

    # =====================================================
    # Civil 3D Information
    # =====================================================

    civil3d_version: str = ""

    template_name: str = ""

    coordinate_system: str = ""

    units: str = "Metric"

    drawing_scale: str = "1:1000"

    # =====================================================
    # Organization
    # =====================================================

    company: str = ""

    client: str = ""

    designer: str = ""

    reviewer: str = ""

    approver: str = ""

    project_number: str = ""

    contract_number: str = ""

    # =====================================================
    # Dates
    # =====================================================

    created_date: datetime | None = None

    modified_date: datetime | None = None

    # =====================================================
    # Revision
    # =====================================================

    revision: str = ""

    status: str = "Working"

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)