"""
pavement_cost.py
================

Pavement Cost Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents calculated pavement quantities and costs.

This module contains engineering data only.
No calculations are performed here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class PavementCost:
    """
    Represents calculated pavement quantities and costs.
    """

    # =====================================================
    # Quantities
    # =====================================================

    pavement_area_m2: float = 0.0

    subgrade_volume_m3: float = 0.0

    subbase_volume_m3: float = 0.0

    base_volume_m3: float = 0.0

    asphalt_volume_m3: float = 0.0

    asphalt_mass_ton: float = 0.0

    # =====================================================
    # Unit Rates
    # =====================================================

    subgrade_rate: float = 0.0

    subbase_rate: float = 0.0

    base_rate: float = 0.0

    asphalt_rate: float = 0.0

    # =====================================================
    # Cost Components
    # =====================================================

    subgrade_cost: float = 0.0

    subbase_cost: float = 0.0

    base_cost: float = 0.0

    asphalt_cost: float = 0.0

    # =====================================================
    # Totals
    # =====================================================

    total_cost: float = 0.0

    currency: str = "EGP"

    # =====================================================
    # Helper Properties
    # =====================================================

    @property
    def average_cost_per_square_meter(self) -> float:
        """
        Average pavement cost per square meter.
        """

        if self.pavement_area_m2 == 0:
            return 0.0

        return self.total_cost / self.pavement_area_m2
