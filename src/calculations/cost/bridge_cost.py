"""
bridge_cost.py
==============

Bridge Cost Calculation Engine

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
class BridgeQuantities:
    """
    Bridge quantities computed from the BIM/Digital Twin model.
    """

    concrete_volume: float = 0.0          # m³
    reinforcement_weight: float = 0.0     # ton
    prestressing_weight: float = 0.0      # ton
    structural_steel: float = 0.0         # ton

    foundation_volume: float = 0.0        # m³

    deck_area: float = 0.0                # m²

    bearing_count: int = 0

    expansion_joint_length: float = 0.0   # m

    barrier_length: float = 0.0           # m

    drainage_length: float = 0.0          # m

    lighting_units: int = 0


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

class BridgeCostCalculator:

    def __init__(

        self,

        quantities: BridgeQuantities,

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
    def concrete_rate(self):

        return self.db.get_rate(
            "bridge",
            "Concrete"
        )

    @property
    def reinforcement_rate(self):

        return self.db.get_rate(
            "bridge",
            "Reinforcement"
        )

    @property
    def prestressing_rate(self):

        return self.db.get_rate(
            "bridge",
            "Prestressing"
        )

    @property
    def steel_rate(self):

        return self.db.get_rate(
            "bridge",
            "Structural Steel"
        )

    @property
    def foundation_rate(self):

        return self.db.get_rate(
            "bridge",
            "Foundation"
        )

    @property
    def deck_rate(self):

        return self.db.get_rate(
            "bridge",
            "Deck"
        )

    @property
    def bearing_rate(self):

        return self.db.get_rate(
            "bridge",
            "Bearing"
        )

    @property
    def expansion_joint_rate(self):

        return self.db.get_rate(
            "bridge",
            "Expansion Joint"
        )

    @property
    def barrier_rate(self):

        return self.db.get_rate(
            "bridge",
            "Barrier"
        )

    @property
    def drainage_rate(self):

        return self.db.get_rate(
            "bridge",
            "Drainage"
        )

    @property
    def lighting_rate(self):

        return self.db.get_rate(
            "bridge",
            "Lighting"
        )

    # ========================================================
    # Cost Items
    # ========================================================

    @property
    def concrete_cost(self):

        return self.quantities.concrete_volume * self.concrete_rate

    @property
    def reinforcement_cost(self):

        return self.quantities.reinforcement_weight * self.reinforcement_rate

    @property
    def prestressing_cost(self):

        return self.quantities.prestressing_weight * self.prestressing_rate

    @property
    def steel_cost(self):

        return self.quantities.structural_steel * self.steel_rate

    @property
    def foundation_cost(self):

        return self.quantities.foundation_volume * self.foundation_rate

    @property
    def deck_cost(self):

        return self.quantities.deck_area * self.deck_rate

    @property
    def bearing_cost(self):

        return self.quantities.bearing_count * self.bearing_rate

    @property
    def expansion_joint_cost(self):

        return self.quantities.expansion_joint_length * self.expansion_joint_rate

    @property
    def barrier_cost(self):

        return self.quantities.barrier_length * self.barrier_rate

    @property
    def drainage_cost(self):

        return self.quantities.drainage_length * self.drainage_rate

    @property
    def lighting_cost(self):

        return self.quantities.lighting_units * self.lighting_rate

    # ========================================================
    # Totals
    # ========================================================

    @property
    def direct_cost(self):

        return (

            self.concrete_cost

            + self.reinforcement_cost

            + self.prestressing_cost

            + self.steel_cost

            + self.foundation_cost

            + self.deck_cost

            + self.bearing_cost

            + self.expansion_joint_cost

            + self.barrier_cost

            + self.drainage_cost

            + self.lighting_cost

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

            "direct_cost": self.direct_cost,

            "indirect_cost": self.indirect_cost,

            "tax": self.tax,

            "total_cost": self.total_cost

        }