"""
optimization_settings.py
========================

Optimization Settings Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents global optimization execution settings.

These settings control the optimization process
independently of the selected optimization algorithm.

No optimization algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class OptimizationSettings:
    """
    Global optimization settings.
    """

    # =====================================================
    # Identity
    # =====================================================

    settings_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Optimization Type
    # =====================================================

    optimization_type: str = "Multi-Objective"
    # Single-Objective
    # Multi-Objective

    algorithm_name: str = "NSGA-II"

    # =====================================================
    # Execution
    # =====================================================

    enabled: bool = True

    auto_start: bool = False

    parallel_execution: bool = False

    number_of_workers: int = 1

    random_seed: int = 42

    reproducible: bool = True

    # =====================================================
    # Logging & Monitoring
    # =====================================================

    verbose: bool = False

    logging_enabled: bool = True

    save_history: bool = True

    save_intermediate_results: bool = True

    # =====================================================
    # Output
    # =====================================================

    save_best_solution: bool = True

    save_pareto_front: bool = True

    export_results: bool = True

    export_statistics: bool = True

    export_history: bool = True

    # =====================================================
    # Runtime
    # =====================================================

    time_limit_seconds: float = 0.0
    # 0 = Unlimited

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)