"""
earthwork_cost.py
=================

Earthwork Cost Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents earthwork cost information for a road project.

This module stores earthwork cost data only.

No volume computation, haul optimization, or cost
estimation algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class EarthworkCost:
    """
    Represents earthwork construction costs.
    """

    # =====================================================
    # Excavation
    # =====================================================

    excavation_cost: float = 0.0

    # =====================================================
    # Embankment
    # =====================================================

    embankment_cost: float = 0.0

    # =====================================================
    # Hauling
    # =====================================================

    hauling_cost: float = 0.0

    # =====================================================
    # Disposal
    # =====================================================

    disposal_cost: float = 0.0

    # =====================================================
    # Borrow Material
    # =====================================================

    borrow_cost: float = 0.0

    # =====================================================
    # Rock Excavation
    # =====================================================

    rock_excavation_cost: float = 0.0

    # =====================================================
    # Soil Stabilization
    # =====================================================

    stabilization_cost: float = 0.0

    # =====================================================
    # Miscellaneous
    # =====================================================

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
    def total_cost(self) -> float:
        """
        Returns the total earthwork cost.
        """
        return (
            self.excavation_cost
            + self.embankment_cost
            + self.hauling_cost
            + self.disposal_cost
            + self.borrow_cost
            + self.rock_excavation_cost
            + self.stabilization_cost
            + self.miscellaneous_cost
        )