"""
earthwork_cost.py
=================

Earthwork Cost Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the calculated earthwork cost for a roadway
project.

This module contains engineering data only.
No calculations are performed here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class EarthworkCost:
    """
    Represents the calculated earthwork quantities and costs.
    """

    # =====================================================
    # Quantities
    # =====================================================

    excavation_volume_m3: float = 0.0

    embankment_volume_m3: float = 0.0

    unsuitable_material_volume_m3: float = 0.0

    disposal_volume_m3: float = 0.0

    borrow_volume_m3: float = 0.0

    # =====================================================
    # Unit Rates
    # =====================================================

    excavation_rate: float = 0.0

    embankment_rate: float = 0.0

    disposal_rate: float = 0.0

    borrow_rate: float = 0.0

    # =====================================================
    # Cost Components
    # =====================================================

    excavation_cost: float = 0.0

    embankment_cost: float = 0.0

    disposal_cost: float = 0.0

    borrow_cost: float = 0.0

    # =====================================================
    # Totals
    # =====================================================

    total_volume_m3: float = 0.0

    total_cost: float = 0.0

    currency: str = "EGP"

    # =====================================================
    # Helper Properties
    # =====================================================

    @property
    def average_cost_per_m3(self) -> float:
        """
        Average earthwork cost per cubic meter.
        """

        if self.total_volume_m3 == 0:
            return 0.0

        return self.total_cost / self.total_volume_m3
