"""
twin_metadata.py
================

Digital Twin Metadata Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents metadata describing a Constructive Digital Twin.

This module stores metadata only.

No synchronization, simulation, or communication logic
is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List
from uuid import uuid4


@dataclass(slots=True)
class TwinMetadata:
    """
    Metadata describing the Digital Twin.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    twin_name: str = ""

    description: str = ""

    version: str = "1.0.0"

    # =====================================================
    # Lifecycle
    # =====================================================

    lifecycle_stage: str = "Design"

    status: str = "Active"

    # =====================================================
    # Ownership
    # =====================================================

    owner: str = ""

    organization: str = ""

    author: str = ""

    # =====================================================
    # Dates
    # =====================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # Source Systems
    # =====================================================

    source_systems: List[str] = field(default_factory=list)

    # =====================================================
    # Classification
    # =====================================================

    tags: List[str] = field(default_factory=list)

    keywords: List[str] = field(default_factory=list)

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)