"""
pavement_cost.py
================

Pavement Cost Calculation Engine

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
class PavementQuantities:
    """
    Pavement quantities extracted from the BIM / Digital Twin model.
    """

    subgrade_volume: float = 0.0          # m³

    subbase_volume: float = 0.0           # m³

    base_volume: float = 0.0              # m³

    asphalt_base_volume: float = 0.0      # m³

    binder_volume: float = 0.0            # m³

    wearing_volume: float = 0.0           # m³

    prime_coat_area: float = 0.0          # m²

    tack_coat_area: float = 0.0           # m²

    milling_area: float = 0.0             # m²

    geotextile_area: float = 0.0          # m²


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

class PavementCostCalculator:

    def __init__(

        self,

        quantities: PavementQuantities,

        cost_database: CostDatabase,

        factors: CostFactors | None = None

    ):

        self.quantities = quantities
        self.db = cost_database
        self.factors = factors or CostFactors()

    # ========================================================
    # Unit Rates
    # ========================================================

    @property
    def subgrade_rate(self):
        return self.db.get_rate("pavement", "Subgrade")

    @property
    def subbase_rate(self):
        return self.db.get_rate("pavement", "Subbase")

    @property
    def base_rate(self):
        return self.db.get_rate("pavement", "Base")

    @property
    def asphalt_base_rate(self):
        return self.db.get_rate("pavement", "Asphalt Base")

    @property
    def binder_rate(self):
        return self.db.get_rate("pavement", "Binder Course")

    @property
    def wearing_rate(self):
        return self.db.get_rate("pavement", "Wearing Course")

    @property
    def prime_coat_rate(self):
        return self.db.get_rate("pavement", "Prime Coat")

    @property
    def tack_coat_rate(self):
        return self.db.get_rate("pavement", "Tack Coat")

    @property
    def milling_rate(self):
        return self.db.get_rate("pavement", "Milling")

    @property
    def geotextile_rate(self):
        return self.db.get_rate("pavement", "Geotextile")

    # ========================================================
    # Cost Items
    # ========================================================

    @property
    def subgrade_cost(self):
        return self.quantities.subgrade_volume * self.subgrade_rate

    @property
    def subbase_cost(self):
        return self.quantities.subbase_volume * self.subbase_rate

    @property
    def base_cost(self):
        return self.quantities.base_volume * self.base_rate

    @property
    def asphalt_base_cost(self):
        return self.quantities.asphalt_base_volume * self.asphalt_base_rate

    @property
    def binder_cost(self):
        return self.quantities.binder_volume * self.binder_rate

    @property
    def wearing_cost(self):
        return self.quantities.wearing_volume * self.wearing_rate

    @property
    def prime_coat_cost(self):
        return self.quantities.prime_coat_area * self.prime_coat_rate

    @property
    def tack_coat_cost(self):
        return self.quantities.tack_coat_area * self.tack_coat_rate

    @property
    def milling_cost(self):
        return self.quantities.milling_area * self.milling_rate

    @property
    def geotextile_cost(self):
        return self.quantities.geotextile_area * self.geotextile_rate

    # ========================================================
    # Totals
    # ========================================================

    @property
    def direct_cost(self):

        return (

            self.subgrade_cost

            + self.subbase_cost

            + self.base_cost

            + self.asphalt_base_cost

            + self.binder_cost

            + self.wearing_cost

            + self.prime_coat_cost

            + self.tack_coat_cost

            + self.milling_cost

            + self.geotextile_cost

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

            "subgrade_cost": self.subgrade_cost,

            "subbase_cost": self.subbase_cost,

            "base_cost": self.base_cost,

            "asphalt_base_cost": self.asphalt_base_cost,

            "binder_cost": self.binder_cost,

            "wearing_cost": self.wearing_cost,

            "prime_coat_cost": self.prime_coat_cost,

            "tack_coat_cost": self.tack_coat_cost,

            "milling_cost": self.milling_cost,

            "geotextile_cost": self.geotextile_cost,

            "direct_cost": self.direct_cost,

            "indirect_cost": self.indirect_cost,

            "tax": self.tax,

            "total_cost": self.total_cost

        }