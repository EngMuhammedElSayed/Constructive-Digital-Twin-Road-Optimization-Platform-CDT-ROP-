"""
drainage_cost.py
================

Drainage Cost Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents drainage-related construction costs for a road
project.

This module stores drainage cost data only.

No hydraulic calculations, quantity takeoff, or cost
estimation logic are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class DrainageCost:
    """
    Represents drainage construction costs.
    """

    # =====================================================
    # Pipe Network
    # =====================================================

    pipe_cost: float = 0.0

    # =====================================================
    # Manholes
    # =====================================================

    manhole_cost: float = 0.0

    # =====================================================
    # Catch Basins
    # =====================================================

    catch_basin_cost: float = 0.0

    # =====================================================
    # Culverts
    # =====================================================

    culvert_cost: float = 0.0

    # =====================================================
    # Open Channels
    # =====================================================

    channel_cost: float = 0.0

    # =====================================================
    # Headwalls / Wingwalls
    # =====================================================

    headwall_cost: float = 0.0

    # =====================================================
    # Outfalls
    # =====================================================

    outfall_cost: float = 0.0

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
        Returns the total drainage cost.
        """
        return (
            self.pipe_cost
            + self.manhole_cost
            + self.catch_basin_cost
            + self.culvert_cost
            + self.channel_cost
            + self.headwall_cost
            + self.outfall_cost
            + self.miscellaneous_cost
        )