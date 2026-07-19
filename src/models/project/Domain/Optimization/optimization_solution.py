"""
optimization_solution.py
========================

Optimization Solution Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents one engineering solution generated during
the optimization process.

A solution contains references to decision variables,
evaluation results, and optimization metrics.

This module stores solution data only.

No optimization algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass(slots=True)
class OptimizationSolution:
    """
    Represents one optimization solution.
    """

    # =====================================================
    # Identity
    # =====================================================

    solution_id: str = ""

    optimization_id: str = ""

    problem_id: str = ""

    # =====================================================
    # References
    # =====================================================

    chromosome_id: str = ""

    evaluation_result_id: str = ""

    fitness_id: str = ""

    decision_variable_ids: List[str] = field(default_factory=list)

    # =====================================================
    # Multi-Objective Information
    # =====================================================

    objective_values: List[float] = field(default_factory=list)

    constraint_violation: float = 0.0

    feasible: bool = True

    # =====================================================
    # NSGA-II Information
    # =====================================================

    rank: int = 0

    crowding_distance: float = 0.0

    domination_count: int = 0

    dominated_solution_ids: List[str] = field(default_factory=list)

    is_pareto_optimal: bool = False

    # =====================================================
    # Execution
    # =====================================================

    generation: int = 0

    iteration: int = 0

    evaluated: bool = False

    selected: bool = False

    # =====================================================
    # Audit
    # =====================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)