"""
structure_cost.py
=================

Structure Cost Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents structural construction costs associated
with roadway infrastructure projects.

This module stores structure-related cost data only.

No structural analysis, reinforcement design,
quantity takeoff, or cost estimation algorithms
are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class StructureCost:
    """
    Represents construction costs for roadway structures.
    """

    # =====================================================
    # Bridges
    # =====================================================

    bridge_cost: float = 0.0

    # =====================================================
    # Culverts
    # =====================================================

    culvert_cost: float = 0.0

    # =====================================================
    # Retaining Walls
    # =====================================================

    retaining_wall_cost: float = 0.0

    # =====================================================
    # Tunnels
    # =====================================================

    tunnel_cost: float = 0.0

    # =====================================================
    # Underpasses / Overpasses
    # =====================================================

    underpass_cost: float = 0.0

    overpass_cost: float = 0.0

    # =====================================================
    # Foundations
    # =====================================================

    foundation_cost: float = 0.0

    # =====================================================
    # Structural Concrete
    # =====================================================

    concrete_cost: float = 0.0

    reinforcement_cost: float = 0.0

    prestressing_cost: float = 0.0

    # =====================================================
    # Bearings & Expansion Joints
    # =====================================================

    bearing_cost: float = 0.0

    expansion_joint_cost: float = 0.0

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
        Returns the total structural construction cost.
        """
        return (
            self.bridge_cost
            + self.culvert_cost
            + self.retaining_wall_cost
            + self.tunnel_cost
            + self.underpass_cost
            + self.overpass_cost
            + self.foundation_cost
            + self.concrete_cost
            + self.reinforcement_cost
            + self.prestressing_cost
            + self.bearing_cost
            + self.expansion_joint_cost
            + self.miscellaneous_cost
        )