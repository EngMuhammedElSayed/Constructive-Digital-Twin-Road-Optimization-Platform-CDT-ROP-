"""
utility_cost.py
===============

Utility Cost Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents utility-related construction and relocation
costs associated with roadway projects.

This module stores utility cost information only.

No clash detection, relocation design, quantity
takeoff, or cost estimation algorithms are implemented
here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class UtilityCost:
    """
    Represents utility construction and relocation costs.
    """

    # =====================================================
    # Water Network
    # =====================================================

    water_network_cost: float = 0.0

    # =====================================================
    # Sewer Network
    # =====================================================

    sewer_network_cost: float = 0.0

    # =====================================================
    # Storm Drainage
    # =====================================================

    storm_drainage_cost: float = 0.0

    # =====================================================
    # Electrical Network
    # =====================================================

    electrical_network_cost: float = 0.0

    street_lighting_cost: float = 0.0

    # =====================================================
    # Telecommunications
    # =====================================================

    telecom_network_cost: float = 0.0

    fiber_optic_cost: float = 0.0

    # =====================================================
    # Gas Network
    # =====================================================

    gas_network_cost: float = 0.0

    # =====================================================
    # Utility Relocation
    # =====================================================

    relocation_cost: float = 0.0

    protection_cost: float = 0.0

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
        Returns the total utility cost.
        """
        return (
            self.water_network_cost
            + self.sewer_network_cost
            + self.storm_drainage_cost
            + self.electrical_network_cost
            + self.street_lighting_cost
            + self.telecom_network_cost
            + self.fiber_optic_cost
            + self.gas_network_cost
            + self.relocation_cost
            + self.protection_cost
            + self.miscellaneous_cost
        )