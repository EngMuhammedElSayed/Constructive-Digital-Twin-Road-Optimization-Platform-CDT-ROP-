"""
cost_category.py
================

Cost Category Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a project cost category.

This module defines the classification of cost items.

No engineering calculations or business logic are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict
from uuid import uuid4


@dataclass(slots=True)
class CostCategory:
    """
    Represents a project cost category.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    code: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Classification
    # =====================================================

    parent_category: str = ""

    is_direct_cost: bool = True

    is_active: bool = True

    # =====================================================
    # Financial
    # =====================================================

    currency: str = "EGP"

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)