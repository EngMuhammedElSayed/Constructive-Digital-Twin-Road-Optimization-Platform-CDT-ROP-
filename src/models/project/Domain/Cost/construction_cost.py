"""
construction_cost.py
====================

Construction Cost Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents construction cost information for a road
project.

This module stores construction cost data only.

No cost calculations or estimation algorithms are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class ConstructionCost:
    """
    Represents construction cost information.
    """

    # =====================================================
    # Earthworks
    # =====================================================

    earthwork_cost: float = 0.0

    # =====================================================
    # Pavement
    # =====================================================

    pavement_cost: float = 0.0

    # =====================================================
    # Drainage
    # =====================================================

    drainage_cost: float = 0.0

    # =====================================================
    # Structures
    # =====================================================

    structure_cost: float = 0.0

    # =====================================================
    # Utilities
    # =====================================================

    utility_cost: float = 0.0

    # =====================================================
    # Right of Way
    # =====================================================

    right_of_way_cost: float = 0.0

    # =====================================================
    # Environmental
    # =====================================================

    environmental_cost: float = 0.0

    # =====================================================
    # Temporary Works
    # =====================================================

    temporary_work_cost: float = 0.0

    # =====================================================
    # Indirect Costs
    # =====================================================

    mobilization_cost: float = 0.0

    supervision_cost: float = 0.0

    contingency_cost: float = 0.0

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
    def direct_cost(self) -> float:
        return (
            self.earthwork_cost
            + self.pavement_cost
            + self.drainage_cost
            + self.structure_cost
            + self.utility_cost
            + self.right_of_way_cost
            + self.environmental_cost
            + self.temporary_work_cost
        )

    @property
    def indirect_cost(self) -> float:
        return (
            self.mobilization_cost
            + self.supervision_cost
            + self.contingency_cost
        )

    @property
    def total_cost(self) -> float:
        return self.direct_cost + self.indirect_cost