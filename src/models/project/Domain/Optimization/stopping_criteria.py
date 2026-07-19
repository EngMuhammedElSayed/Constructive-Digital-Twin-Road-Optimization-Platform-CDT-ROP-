"""
stopping_criteria.py
====================

Stopping Criteria Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents stopping conditions for an optimization
execution.

Stopping criteria determine when an optimization
process should terminate.

This module stores stopping criteria only.

No stopping logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class StoppingCriteria:
    """
    Represents optimization stopping criteria.
    """

    # =====================================================
    # Identity
    # =====================================================

    criteria_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Generation Limits
    # =====================================================

    maximum_generations: int = 500

    maximum_iterations: int = 500

    # =====================================================
    # Evaluation Limits
    # =====================================================

    maximum_function_evaluations: int = 100000

    # =====================================================
    # Runtime Limits
    # =====================================================

    maximum_runtime_seconds: float = 0.0
    # 0 = Unlimited

    # =====================================================
    # Convergence
    # =====================================================

    stop_when_converged: bool = True

    convergence_tolerance: float = 1e-6

    convergence_window: int = 20

    # =====================================================
    # Improvement
    # =====================================================

    minimum_improvement: float = 1e-8

    maximum_stagnation_generations: int = 50

    # =====================================================
    # Manual Control
    # =====================================================

    allow_manual_stop: bool = True

    # =====================================================
    # Status
    # =====================================================

    enabled: bool = True

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)