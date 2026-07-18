"""
project_metadata.py
===================

Civil 3D Project Metadata Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents project metadata associated with a Civil 3D project.

This module stores metadata only.
No Autodesk Civil 3D API logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass(slots=True)
class ProjectMetadata:
    """
    Represents project metadata.
    """

    # =====================================================
    # Project Information
    # =====================================================

    project_name: str = ""

    project_number: str = ""

    contract_number: str = ""

    client: str = ""

    consultant: str = ""

    contractor: str = ""

    # =====================================================
    # Organization
    # =====================================================

    company: str = ""

    department: str = ""

    office: str = ""

    # =====================================================
    # Team
    # =====================================================

    project_manager: str = ""

    design_engineer: str = ""

    bim_manager: str = ""

    reviewer: str = ""

    approver: str = ""

    # =====================================================
    # Document Control
    # =====================================================

    revision: str = "A"

    status: str = "Work In Progress"

    issue_date: datetime | None = None

    created_date: datetime | None = None

    modified_date: datetime | None = None

    # =====================================================
    # Standards
    # =====================================================

    design_standard: str = "AASHTO"

    coordinate_system: str = ""

    units: str = "Metric"

    # =====================================================
    # Metadata
    # =====================================================

    keywords: list[str] = field(default_factory=list)

    notes: str = ""

    custom_properties: Dict[str, str] = field(default_factory=dict)