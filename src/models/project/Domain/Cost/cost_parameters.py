"""
cost_parameters.py
==================

Cost Parameters Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents cost estimation parameters used throughout
the project.

This module stores configuration and input parameters only.

No estimation algorithms or engineering calculations are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class CostParameters:
    """
    Represents project cost estimation parameters.
    """

    # =====================================================
    # Currency
    # =====================================================

    currency: str = "EGP"

    exchange_rate: float = 1.0

    # =====================================================
    # Financial Parameters
    # =====================================================

    inflation_rate: float = 0.0

    tax_rate: float = 0.0

    contingency_rate: float = 0.10

    discount_rate: float = 0.0

    escalation_rate: float = 0.0

    # =====================================================
    # Labour
    # =====================================================

    labour_cost_index: float = 1.0

    # =====================================================
    # Equipment
    # =====================================================

    equipment_cost_index: float = 1.0

    # =====================================================
    # Materials
    # =====================================================

    material_cost_index: float = 1.0

    # =====================================================
    # Fuel
    # =====================================================

    fuel_cost_index: float = 1.0

    # =====================================================
    # Productivity
    # =====================================================

    productivity_factor: float = 1.0

    # =====================================================
    # Project
    # =====================================================

    project_location: str = ""

    estimation_date: str = ""

    cost_database: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)