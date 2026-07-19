"""
convergence_status.py
=====================

Convergence Status Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the current convergence status of an
optimization process.

This module stores convergence information only.

No convergence detection algorithms are implemented
here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass(slots=True)
class ConvergenceStatus:
    """
    Represents the convergence state of an optimization run.
    """

    # =====================================================
    # Identity
    # =====================================================

    convergence_status_id: str = ""

    optimization_id: str = ""

    # =====================================================
    # Current Progress
    # =====================================================

    current_generation: int = 0

    current_iteration: int = 0

    function_evaluations: int = 0

    # =====================================================
    # Convergence
    # =====================================================

    converged: bool = False

    convergence_measure: float = 0.0

    stagnation_generations: int = 0

    # =====================================================
    # Reason
    # =====================================================

    termination_reason: str = ""
    # MaximumGenerations
    # MaximumEvaluations
    # HypervolumeStable
    # ObjectiveStable
    # ManualStop
    # TimeLimit
    # Error

    # =====================================================
    # Performance Indicators
    # =====================================================

    hypervolume: float = 0.0

    spacing: float = 0.0

    generational_distance: float = 0.0

    # =====================================================
    # Runtime
    # =====================================================

    elapsed_time_seconds: float = 0.0

    # =====================================================
    # Audit
    # =====================================================

    updated_at: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)