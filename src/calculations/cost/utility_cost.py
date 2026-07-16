"""
utility_cost.py
===============

Utility Cost Calculation Engine

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
class UtilityQuantities:
    """
    Utility quantities extracted from the BIM / Digital Twin model.
    """

    water_pipe_length: float = 0.0          # m

    sewer_pipe_length: float = 0.0          # m

    storm_pipe_length: float = 0.0          # m

    power_cable_length: float = 0.0         # m

    telecom_cable_length: float = 0.0       # m

    gas_pipe_length: float = 0.0            # m

    utility_manhole_count: int = 0

    utility_relocation_count: int = 0


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

class UtilityCostCalculator:

    def __init__(

        self,

        quantities: UtilityQuantities,

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
    def water_rate(self):
        return self.db.get_rate("utility", "Water Pipe")

    @property
    def sewer_rate(self):
        return self.db.get_rate("utility", "Sewer Pipe")

    @property
    def storm_rate(self):
        return self.db.get_rate("utility", "Storm Pipe")

    @property
    def power_rate(self):
        return self.db.get_rate("utility", "Power Cable")

    @property
    def telecom_rate(self):
        return self.db.get_rate("utility", "Telecommunication Cable")

    @property
    def gas_rate(self):
        return self.db.get_rate("utility", "Gas Pipe")

    @property
    def manhole_rate(self):
        return self.db.get_rate("utility", "Utility Manhole")

    @property
    def relocation_rate(self):
        return self.db.get_rate("utility", "Utility Relocation")

    # ========================================================
    # Cost Items
    # ========================================================

    @property
    def water_cost(self):
        return self.quantities.water_pipe_length * self.water_rate

    @property
    def sewer_cost(self):
        return self.quantities.sewer_pipe_length * self.sewer_rate

    @property
    def storm_cost(self):
        return self.quantities.storm_pipe_length * self.storm_rate

    @property
    def power_cost(self):
        return self.quantities.power_cable_length * self.power_rate

    @property
    def telecom_cost(self):
        return self.quantities.telecom_cable_length * self.telecom_rate

    @property
    def gas_cost(self):
        return self.quantities.gas_pipe_length * self.gas_rate

    @property
    def manhole_cost(self):
        return self.quantities.utility_manhole_count * self.manhole_rate

    @property
    def relocation_cost(self):
        return (
            self.quantities.utility_relocation_count
            * self.relocation_rate
        )

    # ========================================================
    # Totals
    # ========================================================

    @property
    def direct_cost(self):

        return (

            self.water_cost

            + self.sewer_cost

            + self.storm_cost

            + self.power_cost

            + self.telecom_cost

            + self.gas_cost

            + self.manhole_cost

            + self.relocation_cost

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

            "water_cost": self.water_cost,

            "sewer_cost": self.sewer_cost,

            "storm_cost": self.storm_cost,

            "power_cost": self.power_cost,

            "telecom_cost": self.telecom_cost,

            "gas_cost": self.gas_cost,

            "manhole_cost": self.manhole_cost,

            "relocation_cost": self.relocation_cost,

            "direct_cost": self.direct_cost,

            "indirect_cost": self.indirect_cost,

            "tax": self.tax,

            "total_cost": self.total_cost

        }