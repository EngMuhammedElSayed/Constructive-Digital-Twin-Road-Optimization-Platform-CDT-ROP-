"""
optimization_objective.py
=========================

Optimization Objective Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents an optimization objective definition.

An objective defines what the optimization process
attempts to minimize, maximize, or target.

This module stores objective metadata and mathematical
definitions only.

No objective calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class OptimizationObjective:
    """
    Represents a single optimization objective.
    """

    # =====================================================
    # Identity
    # =====================================================

    objective_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Classification
    # =====================================================

    category: str = "Cost"
    # Cost
    # Geometry
    # Traffic
    # Safety
    # Pavement
    # Drainage
    # Earthwork
    # Environment
    # Sustainability

    optimization_goal: str = "Minimize"
    # Minimize
    # Maximize
    # Target

    # =====================================================
    # Mathematical Definition
    # =====================================================

    engineering_parameter: str = ""

    equation: str = ""

    expression: str = ""

    output_unit: str = ""

    normalized: bool = False

    # =====================================================
    # Objective Properties
    # =====================================================

    enabled: bool = True

    priority: int = 1

    weight: float = 1.0

    # =====================================================
    # References
    # =====================================================

    standard_reference: str = ""

    literature_reference: str = ""

    equation_reference: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)