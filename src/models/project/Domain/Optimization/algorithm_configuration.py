"""
algorithm_settings.py
=====================

Algorithm Settings Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the configuration parameters for an
optimization algorithm.

This module stores algorithm settings only.

No optimization algorithm is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class AlgorithmSettings:
    """
    Configuration of an optimization algorithm.
    """

    # =====================================================
    # Identity
    # =====================================================

    settings_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Algorithm
    # =====================================================

    algorithm_name: str = "NSGA-II"

    algorithm_version: str = "1.0"

    random_seed: int = 42

    # =====================================================
    # Population
    # =====================================================

    population_size: int = 100

    offspring_size: int = 100

    generations: int = 200

    # =====================================================
    # Genetic Operators
    # =====================================================

    crossover_probability: float = 0.90

    mutation_probability: float = 0.10

    selection_method: str = "Tournament"

    crossover_method: str = "SBX"

    mutation_method: str = "Polynomial"

    # =====================================================
    # Elitism
    # =====================================================

    elitism_enabled: bool = True

    elite_size: int = 2

    # =====================================================
    # Parallel Execution
    # =====================================================

    parallel_processing: bool = False

    number_of_workers: int = 1

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)