"""
environmental_cost.py
=====================

Environmental Cost Calculation Engine

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
class EnvironmentalQuantities:
    """
    Environmental mitigation quantities.
    """

    tree_count: int = 0

    landscaped_area: float = 0.0          # m²

    noise_barrier_length: float = 0.0     # m

    erosion_control_area: float = 0.0     # m²

    sediment_basin_count: int = 0

    wildlife_crossing_count: int = 0

    carbon_offset_ton: float = 0.0


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

class EnvironmentalCostCalculator:

    def __init__(

        self,

        quantities: EnvironmentalQuantities,

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
    def tree_rate(self):
        return self.db.get_rate("environment", "Tree Planting")

    @property
    def landscape_rate(self):
        return self.db.get_rate("environment", "Landscaping")

    @property
    def noise_barrier_rate(self):
        return self.db.get_rate("environment", "Noise Barrier")

    @property
    def erosion_rate(self):
        return self.db.get_rate("environment", "Erosion Control")

    @property
    def sediment_basin_rate(self):
        return self.db.get_rate("environment", "Sediment Basin")

    @property
    def wildlife_crossing_rate(self):
        return self.db.get_rate("environment", "Wildlife Crossing")

    @property
    def carbon_offset_rate(self):
        return self.db.get_rate("environment", "Carbon Offset")

    # ========================================================
    # Cost Items
    # ========================================================

    @property
    def tree_cost(self):
        return self.quantities.tree_count * self.tree_rate

    @property
    def landscaping_cost(self):
        return self.quantities.landscaped_area * self.landscape_rate

    @property
    def noise_barrier_cost(self):
        return (
            self.quantities.noise_barrier_length
            * self.noise_barrier_rate
        )

    @property
    def erosion_control_cost(self):
        return (
            self.quantities.erosion_control_area
            * self.erosion_rate
        )

    @property
    def sediment_basin_cost(self):
        return (
            self.quantities.sediment_basin_count
            * self.sediment_basin_rate
        )

    @property
    def wildlife_crossing_cost(self):
        return (
            self.quantities.wildlife_crossing_count
            * self.wildlife_crossing_rate
        )

    @property
    def carbon_offset_cost(self):
        return (
            self.quantities.carbon_offset_ton
            * self.carbon_offset_rate
        )

    # ========================================================
    # Totals
    # ========================================================

    @property
    def direct_cost(self):

        return (

            self.tree_cost

            + self.landscaping_cost

            + self.noise_barrier_cost

            + self.erosion_control_cost

            + self.sediment_basin_cost

            + self.wildlife_crossing_cost

            + self.carbon_offset_cost

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

            "tree_cost": self.tree_cost,

            "landscaping_cost": self.landscaping_cost,

            "noise_barrier_cost": self.noise_barrier_cost,

            "erosion_control_cost": self.erosion_control_cost,

            "sediment_basin_cost": self.sediment_basin_cost,

            "wildlife_crossing_cost": self.wildlife_crossing_cost,

            "carbon_offset_cost": self.carbon_offset_cost,

            "direct_cost": self.direct_cost,

            "indirect_cost": self.indirect_cost,

            "tax": self.tax,

            "total_cost": self.total_cost

        }
        