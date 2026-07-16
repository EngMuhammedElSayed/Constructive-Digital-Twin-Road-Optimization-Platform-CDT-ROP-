"""
optimization_config.py
======================

Optimization Engine Configuration

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


# ==========================================================
# Optimization Configuration
# ==========================================================

@dataclass(slots=True)
class OptimizationConfig:
    """
    Optimization engine configuration.

    This file contains only engine settings.

    No objective functions, constraints or equations
    are defined here.
    """

    # ------------------------------------------------------
    # General
    # ------------------------------------------------------

    enabled: bool = True

    algorithm: str = "NSGA-II"

    maximize_parallelism: bool = True

    random_seed: int = 42

    # ------------------------------------------------------
    # Population
    # ------------------------------------------------------

    population_size: int = 100

    offspring_size: int = 100

    generations: int = 200

    eliminate_duplicates: bool = True

    # ------------------------------------------------------
    # Crossover
    # ------------------------------------------------------

    crossover_operator: str = "SBX"

    crossover_probability: float = 0.90

    crossover_eta: float = 15.0

    # ------------------------------------------------------
    # Mutation
    # ------------------------------------------------------

    mutation_operator: str = "PM"

    mutation_probability: float | None = None

    mutation_eta: float = 20.0

    # ------------------------------------------------------
    # Sampling
    # ------------------------------------------------------

    sampling_method: str = "FloatRandomSampling"

    repair_operator: str | None = None

    # ------------------------------------------------------
    # Constraint Handling
    # ------------------------------------------------------

    constraint_strategy: str = "FeasibilityFirst"

    penalty_factor: float = 1.0

    # ------------------------------------------------------
    # Termination
    # ------------------------------------------------------

    termination_type: str = "n_gen"

    convergence_tolerance: float = 1e-6

    maximum_runtime_minutes: int = 120

    # ------------------------------------------------------
    # Parallel Processing
    # ------------------------------------------------------

    use_parallel_processing: bool = True

    max_workers: int = 8

    # ------------------------------------------------------
    # Checkpoint
    # ------------------------------------------------------

    save_checkpoint: bool = True

    checkpoint_interval: int = 10

    checkpoint_directory: Path = Path(
        "output/checkpoints"
    )

    # ------------------------------------------------------
    # Results
    # ------------------------------------------------------

    save_history: bool = True

    save_population: bool = True

    save_pareto_front: bool = True

    export_csv: bool = True

    export_json: bool = True

    export_excel: bool = True

    # ------------------------------------------------------
    # Visualization
    # ------------------------------------------------------

    generate_convergence_plot: bool = True

    generate_pareto_plot: bool = True

    generate_history_plot: bool = True


# ==========================================================
# Default Configuration
# ==========================================================

OPTIMIZATION_CONFIG = OptimizationConfig()
