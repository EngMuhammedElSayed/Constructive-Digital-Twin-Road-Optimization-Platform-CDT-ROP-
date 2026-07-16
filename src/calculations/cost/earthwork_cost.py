"""
earthwork_cost.py
=================

Earthwork Cost Calculation Engine

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
class EarthworkQuantities:
    """
    Earthwork quantities computed by the earthwork engine.
    """

    cut_volume: float
    fill_volume: float

    disposal_volume: float = 0.0
    borrow_volume: float = 0.0

    average_haul_distance: float = 0.0


@dataclass(slots=True)
class CostFactors:
    """
    Project adjustment factors.
    """

    contingency: float = 0.0
    inflation: float = 0.0
    overhead: float = 0.0
    profit: float = 0.0
    tax: float = 0.0


# ============================================================
# Calculator
# ============================================================

class EarthworkCostCalculator:

    def __init__(

        self,

        quantities: EarthworkQuantities,

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
    def excavation_rate(self):

        return self.db.get_rate(
            "earthwork",
            "Excavation"
        )

    @property
    def embankment_rate(self):

        return self.db.get_rate(
            "earthwork",
            "Embankment"
        )

    @property
    def hauling_rate(self):

        return self.db.get_rate(
            "earthwork",
            "Hauling"
        )

    @property
    def disposal_rate(self):

        return self.db.get_rate(
            "earthwork",
            "Disposal"
        )

    @property
    def borrow_rate(self):

        return self.db.get_rate(
            "earthwork",
            "Borrow Material"
        )

    # ========================================================
    # Cost Items
    # ========================================================

    @property
    def excavation_cost(self):

        return (
            self.quantities.cut_volume
            * self.excavation_rate
        )

    @property
    def embankment_cost(self):

        return (
            self.quantities.fill_volume
            * self.embankment_rate
        )

    @property
    def hauling_cost(self):

        transported = max(

            self.quantities.cut_volume,

            self.quantities.fill_volume

        )

        return (

            transported

            * self.quantities.average_haul_distance

            * self.hauling_rate

        )

    @property
    def disposal_cost(self):

        return (

            self.quantities.disposal_volume

            * self.disposal_rate

        )

    @property
    def borrow_cost(self):

        return (

            self.quantities.borrow_volume

            * self.borrow_rate

        )

    # ========================================================
    # Totals
    # ========================================================

    @property
    def direct_cost(self):

        return (

            self.excavation_cost

            + self.embankment_cost

            + self.hauling_cost

            + self.disposal_cost

            + self.borrow_cost

        )

    @property
    def indirect_cost(self):

        return (

            self.direct_cost

            * (

                self.factors.contingency

                + self.factors.inflation

                + self.factors.overhead

                + self.factors.profit

            )

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

            "cut_volume": self.quantities.cut_volume,

            "fill_volume": self.quantities.fill_volume,

            "excavation_rate": self.excavation_rate,

            "embankment_rate": self.embankment_rate,

            "hauling_rate": self.hauling_rate,

            "disposal_rate": self.disposal_rate,

            "borrow_rate": self.borrow_rate,

            "excavation_cost": self.excavation_cost,

            "embankment_cost": self.embankment_cost,

            "hauling_cost": self.hauling_cost,

            "disposal_cost": self.disposal_cost,

            "borrow_cost": self.borrow_cost,

            "direct_cost": self.direct_cost,

            "indirect_cost": self.indirect_cost,

            "tax": self.tax,

            "total_cost": self.total_cost

        }