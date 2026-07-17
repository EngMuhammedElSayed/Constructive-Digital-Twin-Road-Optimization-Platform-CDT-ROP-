"""
row_cost.py
===========

Right-of-Way (ROW) Cost Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents calculated Right-of-Way (ROW) quantities
and acquisition costs.

This module contains engineering data only.
No calculations are performed here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RightOfWayCost:
    """
    Represents calculated Right-of-Way (ROW) costs.
    """

    # =====================================================
    # Quantities
    # =====================================================

    land_area_m2: float = 0.0

    building_area_m2: float = 0.0

    utility_corridor_length_m: float = 0.0

    affected_properties: int = 0

    # =====================================================
    # Unit Rates
    # =====================================================

    land_rate_per_m2: float = 0.0

    building_rate_per_m2: float = 0.0

    utility_relocation_rate_per_m: float = 0.0

    compensation_rate_per_property: float = 0.0

    # =====================================================
    # Cost Components
    # =====================================================

    land_cost: float = 0.0

    building_cost: float = 0.0

    utility_relocation_cost: float = 0.0

    compensation_cost: float = 0.0

    # =====================================================
    # Totals
    # =====================================================

    total_cost: float = 0.0

    currency: str = "EGP"

    # =====================================================
    # Helper Properties
    # =====================================================

    @property
    def average_land_cost_per_m2(self) -> float:
        """
        Average land acquisition cost per square meter.
        """

        if self.land_area_m2 == 0:
            return 0.0

        return self.land_cost / self.land_area_m2
