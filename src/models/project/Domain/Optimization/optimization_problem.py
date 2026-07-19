"""
optimization_problem.py
=======================

Optimization Problem Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the complete optimization problem definition.

The optimization problem is the Aggregate Root of the
Optimization Domain.

It references:

- Decision Variables
- Objectives
- Constraints
- Settings
- Metadata

No optimization algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass(slots=True)
class OptimizationProblem:
    """
    Represents a complete optimization problem.
    """

    # =====================================================
    # Identity
    # =====================================================

    problem_id: str = ""

    project_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Domain References
    # =====================================================

    decision_variable_ids: List[str] = field(default_factory=list)

    objective_ids: List[str] = field(default_factory=list)

    constraint_ids: List[str] = field(default_factory=list)

    # =====================================================
    # Configuration
    # =====================================================

    optimization_settings_id: str = ""

    algorithm_settings_id: str = ""

    evaluation_settings_id: str = ""

    convergence_criteria_id: str = ""

    optimization_metadata_id: str = ""

    # =====================================================
    # Problem Information
    # =====================================================

    optimization_type: str = "Multi-Objective"
    # Single-Objective
    # Multi-Objective

    enabled: bool = True

    validated: bool = False

    # =====================================================
    # Statistics
    # =====================================================

    number_of_variables: int = 0

    number_of_objectives: int = 0

    number_of_constraints: int = 0

    # =====================================================
    # Audit
    # =====================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    modified_at: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)