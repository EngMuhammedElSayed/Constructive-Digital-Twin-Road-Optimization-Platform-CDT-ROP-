"""
maintenance_cost.py
===================

Maintenance Cost Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents operation and maintenance costs associated
with a roadway project.

This module stores maintenance cost data only.

No life-cycle cost analysis (LCCA), deterioration
models, or maintenance scheduling algorithms are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class MaintenanceCost:
    """
    Represents operation and maintenance costs.
    """

    # =====================================================
    # Pavement Maintenance
    # =====================================================

    pavement_maintenance_cost: float = 0.0

    # =====================================================
    # Drainage Maintenance
    # =====================================================

    drainage_maintenance_cost: float = 0.0

    # =====================================================
    # Road Furniture
    # =====================================================

    guardrail_maintenance_cost: float = 0.0

    traffic_sign_maintenance_cost: float = 0.0

    pavement_marking_cost: float = 0.0

    lighting_maintenance_cost: float = 0.0

    # =====================================================
    # Vegetation
    # =====================================================

    landscaping_maintenance_cost: float = 0.0

    # =====================================================
    # Structures
    # =====================================================

    bridge_maintenance_cost: float = 0.0

    culvert_maintenance_cost: float = 0.0

    retaining_wall_maintenance_cost: float = 0.0

    # =====================================================
    # Winter / Emergency Maintenance
    # =====================================================

    emergency_maintenance_cost: float = 0.0

    miscellaneous_cost: float = 0.0

    # =====================================================
    # Financial
    # =====================================================

    annual_cost: float = 0.0

    service_life_years: int = 20

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
        Returns the total maintenance cost.
        """
        return (
            self.pavement_maintenance_cost
            + self.drainage_maintenance_cost
            + self.guardrail_maintenance_cost
            + self.traffic_sign_maintenance_cost
            + self.pavement_marking_cost
            + self.lighting_maintenance_cost
            + self.landscaping_maintenance_cost
            + self.bridge_maintenance_cost
            + self.culvert_maintenance_cost
            + self.retaining_wall_maintenance_cost
            + self.emergency_maintenance_cost
            + self.miscellaneous_cost
        )