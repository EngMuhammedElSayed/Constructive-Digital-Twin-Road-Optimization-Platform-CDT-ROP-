"""
objective_function.py
=====================

Objective Function Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a mathematical objective function used by
an optimization objective.

The objective function defines how an objective value
is calculated.

This module stores objective-function metadata only.

No mathematical calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class ObjectiveFunction:
    """
    Represents an objective function definition.
    """

    # =====================================================
    # Identity
    # =====================================================

    function_id: str = ""

    objective_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Mathematical Information
    # =====================================================

    equation: str = ""

    expression: str = ""

    output_parameter: str = ""

    output_unit: str = ""

    # =====================================================
    # Optimization Direction
    # =====================================================

    optimization_goal: str = "Minimize"
    # Minimize
    # Maximize
    # Target

    # =====================================================
    # Status
    # =====================================================

    enabled: bool = True

    differentiable: bool = False

    normalized: bool = False

    # =====================================================
    # References
    # =====================================================

    standard_reference: str = ""

    literature_reference: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)