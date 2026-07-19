"""
optimization_history.py
=======================

Optimization History Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the historical record of an optimization
execution.

The history stores references to optimization
iterations and summary execution information.

This module stores historical data only.

No optimization algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass(slots=True)
class OptimizationHistory:
    """
    Represents the complete optimization history.
    """

    # =====================================================
    # Identity
    # =====================================================

    history_id: str = ""

    optimization_id: str = ""

    problem_id: str = ""

    # =====================================================
    # Iteration History
    # =====================================================

    iteration_ids: List[str] = field(default_factory=list)

    total_iterations: int = 0

    # =====================================================
    # Solution History
    # =====================================================

    best_solution_history: List[str] = field(default_factory=list)

    pareto_front_history: List[str] = field(default_factory=list)

    # =====================================================
    # Execution Statistics
    # =====================================================

    total_function_evaluations: int = 0

    total_runtime_seconds: float = 0.0

    completed: bool = False

    # =====================================================
    # Audit
    # =====================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)