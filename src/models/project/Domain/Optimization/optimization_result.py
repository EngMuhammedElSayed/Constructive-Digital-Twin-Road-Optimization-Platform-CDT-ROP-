"""
optimization_result.py
======================

Optimization Result Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the final result produced by an optimization
execution.

This model stores references to the best solution,
Pareto front, execution statistics, and convergence
information.

No optimization algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass(slots=True)
class OptimizationResult:
    """
    Represents the final optimization result.
    """

    # =====================================================
    # Identity
    # =====================================================

    result_id: str = ""

    optimization_id: str = ""

    problem_id: str = ""

    # =====================================================
    # Solution References
    # =====================================================

    best_solution_id: str = ""

    solution_ids: List[str] = field(default_factory=list)

    pareto_solution_ids: List[str] = field(default_factory=list)

    # =====================================================
    # History References
    # =====================================================

    optimization_history_id: str = ""

    convergence_status_id: str = ""

    # =====================================================
    # Statistics
    # =====================================================

    total_generations: int = 0

    total_iterations: int = 0

    total_function_evaluations: int = 0

    pareto_front_size: int = 0

    # =====================================================
    # Quality Indicators
    # =====================================================

    hypervolume: float = 0.0

    spacing: float = 0.0

    generational_distance: float = 0.0

    inverted_generational_distance: float = 0.0

    # =====================================================
    # Execution
    # =====================================================

    runtime_seconds: float = 0.0

    converged: bool = False

    successful: bool = False

    termination_reason: str = ""

    # =====================================================
    # Status
    # =====================================================

    status: str = "Completed"
    # Pending
    # Running
    # Completed
    # Failed
    # Cancelled

    message: str = ""

    # =====================================================
    # Audit
    # =====================================================

    completed_at: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)