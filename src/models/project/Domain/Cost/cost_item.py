"""
cost_item.py
============

Cost Item Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a single cost item (BOQ item) within a road
construction project.

This module stores cost item data only.

No quantity takeoff, pricing logic, or estimation
algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict
from uuid import uuid4


@dataclass(slots=True)
class CostItem:
    """
    Represents a single BOQ cost item.
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

    category: str = ""

    work_package: str = ""

    # =====================================================
    # Quantity
    # =====================================================

    quantity: float = 0.0

    unit: str = ""

    # =====================================================
    # Pricing
    # =====================================================

    unit_price: float = 0.0

    currency: str = "EGP"

    # =====================================================
    # Status
    # =====================================================

    included: bool = True

    remarks: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)

    # =====================================================
    # Read-Only Properties
    # =====================================================

    @property
    def total_cost(self) -> float:
        return self.quantity * self.unit_price