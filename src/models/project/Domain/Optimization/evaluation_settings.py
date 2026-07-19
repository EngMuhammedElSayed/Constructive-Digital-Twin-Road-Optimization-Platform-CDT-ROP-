"""
evaluation_settings.py
======================

Evaluation Settings Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents configuration parameters controlling the
evaluation of optimization solutions.

This module stores evaluation settings only.

No objective or constraint calculations are implemented
here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class EvaluationSettings:
    """
    Represents evaluation settings.
    """

    # =====================================================
    # Identity
    # =====================================================

    settings_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Evaluation
    # =====================================================

    evaluate_objectives: bool = True

    evaluate_constraints: bool = True

    evaluate_fitness: bool = True

    normalize_objectives: bool = False

    apply_penalty_functions: bool = True

    # =====================================================
    # Constraint Handling
    # =====================================================

    constraint_handling_method: str = "Deb"
    # Deb
    # Penalty
    # Repair
    # AdaptivePenalty

    # =====================================================
    # Precision
    # =====================================================

    tolerance: float = 1e-6

    numerical_precision: int = 6

    # =====================================================
    # Parallel Evaluation
    # =====================================================

    parallel_evaluation: bool = False

    number_of_workers: int = 1

    # =====================================================
    # Status
    # =====================================================

    enabled: bool = True

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)