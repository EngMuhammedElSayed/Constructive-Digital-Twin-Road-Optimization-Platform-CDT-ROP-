"""
version_control.py
==================

Digital Twin Version Control Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents version information for the Constructive
Digital Twin.

This module stores version metadata only.

No Git integration, repository management, or
versioning logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict
from uuid import uuid4


@dataclass(slots=True)
class VersionControl:
    """
    Represents version information for a Digital Twin.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    # =====================================================
    # Version Information
    # =====================================================

    version: str = "1.0.0"

    revision: str = "A"

    build_number: int = 1

    status: str = "Draft"

    # =====================================================
    # History
    # =====================================================

    previous_version: str = ""

    parent_version: str = ""

    change_description: str = ""

    # =====================================================
    # Dates
    # =====================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    released_at: datetime | None = None

    # =====================================================
    # Ownership
    # =====================================================

    author: str = ""

    reviewer: str = ""

    approver: str = ""

    # =====================================================
    # Flags
    # =====================================================

    is_current: bool = True

    is_baseline: bool = False

    is_archived: bool = False

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)