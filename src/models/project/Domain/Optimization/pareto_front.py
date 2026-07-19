"""
pareto_front.py
===============

Pareto Front Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a Pareto Front produced by a multi-objective
optimization process.

A Pareto Front is a collection of non-dominated
engineering solutions.

This module stores Pareto Front metadata only.

No Pareto sorting algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass(slots=True)
class ParetoFront:
    """
    Represents one Pareto Front.
    """

    # =====================================================
    # Identity
    # =====================================================

    pareto_front_id: str = ""

    optimization_id: str = ""

    iteration_id: str = ""

    # =====================================================
    # Solutions
    # =====================================================

    solution_ids: List[str] = field(default_factory=list)

    number_of_solutions: int = 0

    # =====================================================
    # Quality Indicators
    # =====================================================

    hypervolume: float = 0.0

    spacing: float = 0.0

    generational_distance: float = 0.0

    inverted_generational_distance: float = 0.0

    epsilon_indicator: float = 0.0

    # =====================================================
    # Status
    # =====================================================

    finalized: bool = False

    # =====================================================
    # Audit
    # =====================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)