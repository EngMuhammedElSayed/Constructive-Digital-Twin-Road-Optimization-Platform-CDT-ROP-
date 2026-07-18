"""
pavement_cost.py
================

Pavement Cost Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents pavement construction costs for a roadway
project.

This module stores pavement cost information only.

No pavement design, thickness calculation, ESAL
analysis, MEPDG, or cost estimation algorithms are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class PavementCost:
    """
    Represents pavement construction costs.
    """

    # =====================================================
    # Flexible Pavement Layers
    # =====================================================

    subgrade_cost: float = 0.0

    subbase_cost: float = 0.0

    base_course_cost: float = 0.0

    binder_course_cost: float = 0.0

    wearing_course_cost: float = 0.0

    # =====================================================
    # Rigid Pavement
    # =====================================================

    concrete_pavement_cost: float = 0.0

    reinforcement_cost: float = 0.0

    dowel_bar_cost: float = 0.0

    tie_bar_cost: float = 0.0

    # =====================================================
    # Ancillary Works
    # =====================================================

    shoulder_cost: float = 0.0

    prime_coat_cost: float = 0.0

    tack_coat_cost: float = 0.0

    seal_coat_cost: float = 0.0

    pavement_marking_cost: float = 0.0

    miscellaneous_cost: float = 0.0

    # =====================================================
    # Currency
    # =====================================================

    currency: str = "EGP"

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)

    # =====================================================
    # Read-Only Properties
    # =====================================================

    @property
    def flexible_pavement_cost(self) -> float:
        """
        Returns the total flexible pavement cost.
        """
        return (
            self.subgrade_cost
            + self.subbase_cost
            + self.base_course_cost
            + self.binder_course_cost
            + self.wearing_course_cost
        )

    @property
    def rigid_pavement_cost(self) -> float:
        """
        Returns the total rigid pavement cost.
        """
        return (
            self.concrete_pavement_cost
            + self.reinforcement_cost
            + self.dowel_bar_cost
            + self.tie_bar_cost
        )

    @property
    def ancillary_cost(self) -> float:
        """
        Returns ancillary pavement costs.
        """
        return (
            self.shoulder_cost
            + self.prime_coat_cost
            + self.tack_coat_cost
            + self.seal_coat_cost
            + self.pavement_marking_cost
            + self.miscellaneous_cost
        )

    @property
    def total_cost(self) -> float:
        """
        Returns the total pavement cost.
        """
        return (
            self.flexible_pavement_cost
            + self.rigid_pavement_cost
            + self.ancillary_cost
        )