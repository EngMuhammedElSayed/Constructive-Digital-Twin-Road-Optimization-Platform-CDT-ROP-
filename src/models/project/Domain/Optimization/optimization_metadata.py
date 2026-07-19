"""
optimization_metadata.py
========================

Optimization Metadata Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents descriptive metadata associated with an
optimization process.

This module stores metadata only.

No optimization algorithms or engineering calculations
are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass(slots=True)
class OptimizationMetadata:
    """
    Descriptive metadata for an optimization process.
    """

    # =====================================================
    # Identity
    # =====================================================

    metadata_id: str = ""

    optimization_id: str = ""

    project_id: str = ""

    # =====================================================
    # General Information
    # =====================================================

    name: str = ""

    description: str = ""

    version: str = "1.0.0"

    # =====================================================
    # Project Information
    # =====================================================

    project_name: str = ""

    scenario_name: str = ""

    study_name: str = ""

    # =====================================================
    # Author Information
    # =====================================================

    created_by: str = ""

    organization: str = ""

    contact_email: str = ""

    # =====================================================
    # Execution Information
    # =====================================================

    software_name: str = "CDT-ROP"

    software_version: str = "1.0.0"

    algorithm_name: str = ""

    algorithm_version: str = ""

    # =====================================================
    # Classification
    # =====================================================

    optimization_type: str = "Multi-Objective"
    # Single-Objective
    # Multi-Objective

    status: str = "Draft"
    # Draft
    # Ready
    # Running
    # Completed
    # Archived

    tags: List[str] = field(default_factory=list)

    # =====================================================
    # Audit
    # =====================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    modified_at: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # Additional Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)