"""
optimization_constraint.py
==========================

Optimization Constraint Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents an engineering constraint used by the
optimization problem.

A constraint defines a rule that every candidate
solution should satisfy.

This module stores constraint definitions only.

No constraint evaluation logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class OptimizationConstraint:
    """
    Represents a single optimization constraint.
    """

    # =====================================================
    # Identity
    # =====================================================

    constraint_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Classification
    # =====================================================

    category: str = "Geometry"
    # Geometry
    # Traffic
    # Pavement
    # Earthwork
    # Drainage
    # Structures
    # Utilities
    # Cost
    # Environment
    # Safety

    constraint_type: str = "Inequality"
    # Inequality
    # Equality
    # Range

    # =====================================================
    # Engineering Parameter
    # =====================================================

    engineering_parameter: str = ""

    unit: str = ""

    # =====================================================
    # Constraint Limits
    # =====================================================

    lower_bound: float = 0.0

    upper_bound: float = 0.0

    target_value: float = 0.0

    tolerance: float = 0.0

    # =====================================================
    # Optimization Behaviour
    # =====================================================

    enabled: bool = True

    mandatory: bool = True

    priority: int = 1

    penalty_factor: float = 1.0

    # =====================================================
    # References
    # =====================================================

    standard_reference: str = ""

    clause_reference: str = ""

    equation_reference: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)