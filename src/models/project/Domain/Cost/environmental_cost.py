"""
environmental_cost.py
=====================

Environmental Cost Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents environmental protection costs associated
with a road construction project.

This module stores environmental cost data only.

No environmental assessment, carbon estimation,
or engineering calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class EnvironmentalCost:
    """
    Represents environmental protection costs.
    """

    # =====================================================
    # Erosion & Sediment Control
    # =====================================================

    erosion_control_cost: float = 0.0

    sediment_control_cost: float = 0.0

    # =====================================================
    # Landscaping
    # =====================================================

    landscaping_cost: float = 0.0

    revegetation_cost: float = 0.0

    # =====================================================
    # Noise Mitigation
    # =====================================================

    noise_barrier_cost: float = 0.0

    # =====================================================
    # Air Quality
    # =====================================================

    dust_control_cost: float = 0.0

    emission_mitigation_cost: float = 0.0

    # =====================================================
    # Water Protection
    # =====================================================

    water_protection_cost: float = 0.0

    wetland_protection_cost: float = 0.0

    # =====================================================
    # Waste Management
    # =====================================================

    waste_management_cost: float = 0.0

    recycling_cost: float = 0.0

    # =====================================================
    # Environmental Monitoring
    # =====================================================

    monitoring_cost: float = 0.0

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
        Returns the total environmental cost.
        """
        return (
            self.erosion_control_cost
            + self.sediment_control_cost
            + self.landscaping_cost
            + self.revegetation_cost
            + self.noise_barrier_cost
            + self.dust_control_cost
            + self.emission_mitigation_cost
            + self.water_protection_cost
            + self.wetland_protection_cost
            + self.waste_management_cost
            + self.recycling_cost
            + self.monitoring_cost
            + self.miscellaneous_cost
        )