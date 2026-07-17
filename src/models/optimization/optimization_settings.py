"""
optimization_settings.py
========================

Optimization Settings Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines optimization parameters used by optimization
algorithms.

This module contains configuration data only.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(slots=True)
class OptimizationSettings:
    """
    Represents optimization algorithm settings.
    """

    # =====================================================
    # General
    # =====================================================

    algorithm: str = "NSGA-II"

    enabled: bool = True

    random_seed: int = 42

    # =====================================================
    # Population
    # =====================================================

    population_size: int = 100

    offspring_size: int = 100

    generations: int = 200

    # =====================================================
    # Termination
    # =====================================================

    tolerance: float = 1e-6

    maximum_runtime_sec: float = 3600.0

    # =====================================================
    # Objectives
    # =====================================================

    objective_names: List[str] = field(
        default_factory=list
    )

    objective_weights: Dict[str, float] = field(
        default_factory=dict
    )

    # =====================================================
    # Constraints
    # =====================================================

    constraint_names: List[str] = field(
        default_factory=list
    )

    hard_constraints: bool = True

    penalty_factor: float = 1000.0

    # =====================================================
    # Output
    # =====================================================

    save_history: bool = True

    save_pareto_front: bool = True

    export_results: bool = True

    # =====================================================
    # Parallel Processing
    # =====================================================

    enable_parallel_processing: bool = False

    number_of_workers: int = 1

    # =====================================================
    # Metadata
    # =====================================================

    version: str = "1.0"

    properties: Dict[str, str] = field(
        default_factory=dict
    )