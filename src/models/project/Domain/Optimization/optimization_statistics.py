"""
optimization_statistics.py
==========================

Optimization Statistics Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents statistical information generated during an
optimization execution.

This module stores summary statistics only.

No optimization algorithms or statistical calculations
are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class OptimizationStatistics:
    """
    Represents summary statistics of an optimization run.
    """

    # =====================================================
    # Identity
    # =====================================================

    statistics_id: str = ""

    optimization_id: str = ""

    problem_id: str = ""

    # =====================================================
    # Population Statistics
    # =====================================================

    population_size: int = 0

    feasible_solutions: int = 0

    infeasible_solutions: int = 0

    pareto_front_size: int = 0

    # =====================================================
    # Execution Statistics
    # =====================================================

    total_generations: int = 0

    total_iterations: int = 0

    total_function_evaluations: int = 0

    runtime_seconds: float = 0.0

    # =====================================================
    # Quality Indicators
    # =====================================================

    best_objective_value: float = 0.0

    worst_objective_value: float = 0.0

    average_objective_value: float = 0.0

    hypervolume: float = 0.0

    spacing: float = 0.0

    generational_distance: float = 0.0

    inverted_generational_distance: float = 0.0

    # =====================================================
    # Constraint Statistics
    # =====================================================

    average_constraint_violation: float = 0.0

    maximum_constraint_violation: float = 0.0

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)