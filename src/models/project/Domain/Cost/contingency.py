"""
contingency.py
==============

Contingency Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents contingency information for a road project.

This module stores contingency data only.

No engineering calculations or business logic are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Contingency:
    """
    Represents contingency information.
    """

    # =====================================================
    # General
    # =====================================================

    enabled: bool = True

    name: str = "Project Contingency"

    description: str = ""

    # =====================================================
    # Percentage
    # =====================================================

    percentage: float = 0.10

    # =====================================================
    # Value
    # =====================================================

    amount: float = 0.0

    currency: str = "EGP"

    # =====================================================
    # Classification
    # =====================================================

    contingency_type: str = "Construction"

    risk_level: str = "Medium"

    # =====================================================
    # Notes
    # =====================================================

    remarks: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)