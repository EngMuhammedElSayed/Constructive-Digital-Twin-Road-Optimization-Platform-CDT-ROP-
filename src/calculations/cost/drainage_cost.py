"""
drainage_cost.py
================

Drainage Cost Calculation Engine

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 2.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from .cost_database import CostDatabase


# ============================================================
# Input Models
# ============================================================

@dataclass(slots=True)
class DrainageQuantities:
    """
    Drainage quantities extracted from the Digital Twin model.
    """

    pipe_length: float = 0.0          # m

    manhole_count: int = 0

    catch_basin_count: int = 0

    culvert_length: float = 0.0       # m

    headwall_count: int = 0

    channel_length: float = 0.0       # m

    erosion_protection_area: float = 0.0   # m²


@dataclass(slots=True)
class CostFactors:

    contingency: float = 0.0
    inflation: float = 0.0
    overhead: float = 0.0
    profit: float = 0.0
    tax: float = 0.0


# ============================================================
# Calculator
# ============================================================

class DrainageCostCalculator:

    def __init__(

        self,

        quantities: DrainageQuantities,

        cost_database: CostDatabase,

        factors: CostFactors | None = None

    ):

        self.quantities = quantities
        self.db = cost_database
        self.factors = factors or CostFactors()

    # ========================================================
    # Rates
    # ========================================================

    @property
    def pipe_rate(self):

        return self.db.get_rate("drainage", "Pipe")

    @property
    def manhole_rate(self):

        return self.db.get_rate("drainage", "Manhole")

    @property
    def catch_basin_rate(self):

        return self.db.get_rate("drainage", "Catch Basin")

    @property
    def culvert_rate(self):

        return self.db.get_rate("drainage", "Culvert")

    @property
    def headwall_rate(self):

        return self.db.get_rate("drainage", "Headwall")

    @property
    def channel_rate(self):

        return self.db.get_rate("drainage", "Channel")

    @property
    def erosion_rate(self):

        return self.db.get_rate("drainage", "Erosion Protection")

    # ========================================================
    # Cost Items
    # ========================================================

    @property
    def pipe_cost(self):

        return self.quantities.pipe_length * self.pipe_rate

    @property
    def manhole_cost(self):

        return self.quantities.manhole_count * self.manhole_rate

    @property
    def catch_basin_cost(self):

        return self.quantities.catch_basin_count * self.catch_basin_rate

    @property
    def culvert_cost(self):

        return self.quantities.culvert_length * self.culvert_rate

    @property
    def headwall_cost(self):

        return self.quantities.headwall_count * self.headwall_rate

    @property
    def channel_cost(self):

        return self.quantities.channel_length * self.channel_rate

    @property
    def erosion_cost(self):

        return (
            self.quantities.erosion_protection_area
            * self.erosion_rate
        )

    # ========================================================
    # Totals
    # ========================================================

    @property
    def direct_cost(self):

        return (

            self.pipe_cost

            + self.manhole_cost

            + self.catch_basin_cost

            + self.culvert_cost

            + self.headwall_cost

            + self.channel_cost

            + self.erosion_cost

        )

    @property
    def indirect_cost(self):

        return self.direct_cost * (

            self.factors.contingency

            + self.factors.inflation

            + self.factors.overhead

            + self.factors.profit

        )

    @property
    def subtotal(self):

        return self.direct_cost + self.indirect_cost

    @property
    def tax(self):

        return self.subtotal * self.factors.tax

    @property
    def total_cost(self):

        return self.subtotal + self.tax

    # ========================================================
    # Summary
    # ========================================================

    def summary(self) -> Dict:

        return {

            "currency": self.db.currency,

            "pipe_cost": self.pipe_cost,

            "manhole_cost": self.manhole_cost,

            "catch_basin_cost": self.catch_basin_cost,

            "culvert_cost": self.culvert_cost,

            "headwall_cost": self.headwall_cost,

            "channel_cost": self.channel_cost,

            "erosion_cost": self.erosion_cost,

            "direct_cost": self.direct_cost,

            "indirect_cost": self.indirect_cost,

            "tax": self.tax,

            "total_cost": self.total_cost

        }