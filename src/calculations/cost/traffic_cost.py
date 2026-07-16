"""
traffic_cost.py
===============

Traffic Engineering Cost Calculation Engine

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
class TrafficQuantities:
    """
    Traffic engineering quantities extracted from the BIM / Digital Twin model.
    """

    road_marking_area: float = 0.0          # m²

    traffic_sign_count: int = 0

    guide_sign_count: int = 0

    gantry_sign_count: int = 0

    traffic_signal_count: int = 0

    street_light_count: int = 0

    guardrail_length: float = 0.0          # m

    concrete_barrier_length: float = 0.0   # m

    delineator_count: int = 0

    rumble_strip_length: float = 0.0       # m


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

class TrafficCostCalculator:

    def __init__(

        self,

        quantities: TrafficQuantities,

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
    def marking_rate(self):
        return self.db.get_rate("traffic", "Road Marking")

    @property
    def traffic_sign_rate(self):
        return self.db.get_rate("traffic", "Traffic Sign")

    @property
    def guide_sign_rate(self):
        return self.db.get_rate("traffic", "Guide Sign")

    @property
    def gantry_sign_rate(self):
        return self.db.get_rate("traffic", "Gantry Sign")

    @property
    def signal_rate(self):
        return self.db.get_rate("traffic", "Traffic Signal")

    @property
    def street_light_rate(self):
        return self.db.get_rate("traffic", "Street Light")

    @property
    def guardrail_rate(self):
        return self.db.get_rate("traffic", "Guardrail")

    @property
    def barrier_rate(self):
        return self.db.get_rate("traffic", "Concrete Barrier")

    @property
    def delineator_rate(self):
        return self.db.get_rate("traffic", "Delineator")

    @property
    def rumble_strip_rate(self):
        return self.db.get_rate("traffic", "Rumble Strip")

    # ========================================================
    # Cost Items
    # ========================================================

    @property
    def marking_cost(self):
        return self.quantities.road_marking_area * self.marking_rate

    @property
    def traffic_sign_cost(self):
        return self.quantities.traffic_sign_count * self.traffic_sign_rate

    @property
    def guide_sign_cost(self):
        return self.quantities.guide_sign_count * self.guide_sign_rate

    @property
    def gantry_sign_cost(self):
        return self.quantities.gantry_sign_count * self.gantry_sign_rate

    @property
    def signal_cost(self):
        return self.quantities.traffic_signal_count * self.signal_rate

    @property
    def street_light_cost(self):
        return self.quantities.street_light_count * self.street_light_rate

    @property
    def guardrail_cost(self):
        return self.quantities.guardrail_length * self.guardrail_rate

    @property
    def barrier_cost(self):
        return (
            self.quantities.concrete_barrier_length
            * self.barrier_rate
        )

    @property
    def delineator_cost(self):
        return self.quantities.delineator_count * self.delineator_rate

    @property
    def rumble_strip_cost(self):
        return (
            self.quantities.rumble_strip_length
            * self.rumble_strip_rate
        )

    # ========================================================
    # Totals
    # ========================================================

    @property
    def direct_cost(self):

        return (

            self.marking_cost

            + self.traffic_sign_cost

            + self.guide_sign_cost

            + self.gantry_sign_cost

            + self.signal_cost

            + self.street_light_cost

            + self.guardrail_cost

            + self.barrier_cost

            + self.delineator_cost

            + self.rumble_strip_cost

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

            "marking_cost": self.marking_cost,

            "traffic_sign_cost": self.traffic_sign_cost,

            "guide_sign_cost": self.guide_sign_cost,

            "gantry_sign_cost": self.gantry_sign_cost,

            "signal_cost": self.signal_cost,

            "street_light_cost": self.street_light_cost,

            "guardrail_cost": self.guardrail_cost,

            "barrier_cost": self.barrier_cost,

            "delineator_cost": self.delineator_cost,

            "rumble_strip_cost": self.rumble_strip_cost,

            "direct_cost": self.direct_cost,

            "indirect_cost": self.indirect_cost,

            "tax": self.tax,

            "total_cost": self.total_cost

        }