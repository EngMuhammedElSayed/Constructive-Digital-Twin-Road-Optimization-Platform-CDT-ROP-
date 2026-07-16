"""
maintenance_cost.py
===================

Maintenance Cost Calculation Engine

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
class MaintenanceQuantities:
    """
    Maintenance work quantities.
    """

    pavement_repair_area: float = 0.0      # m²

    crack_sealing_length: float = 0.0      # m

    pothole_count: int = 0

    shoulder_repair_length: float = 0.0    # m

    drainage_cleaning_length: float = 0.0  # m

    sign_replacement_count: int = 0

    marking_area: float = 0.0              # m²

    guardrail_length: float = 0.0          # m


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

class MaintenanceCostCalculator:

    def __init__(

        self,

        quantities: MaintenanceQuantities,

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
    def pavement_repair_rate(self):
        return self.db.get_rate("maintenance", "Pavement Repair")

    @property
    def crack_sealing_rate(self):
        return self.db.get_rate("maintenance", "Crack Sealing")

    @property
    def pothole_rate(self):
        return self.db.get_rate("maintenance", "Pothole Repair")

    @property
    def shoulder_rate(self):
        return self.db.get_rate("maintenance", "Shoulder Repair")

    @property
    def drainage_rate(self):
        return self.db.get_rate("maintenance", "Drainage Cleaning")

    @property
    def sign_rate(self):
        return self.db.get_rate("maintenance", "Sign Replacement")

    @property
    def marking_rate(self):
        return self.db.get_rate("maintenance", "Road Marking")

    @property
    def guardrail_rate(self):
        return self.db.get_rate("maintenance", "Guardrail Repair")

    # ========================================================
    # Cost Items
    # ========================================================

    @property
    def pavement_repair_cost(self):
        return (
            self.quantities.pavement_repair_area
            * self.pavement_repair_rate
        )

    @property
    def crack_sealing_cost(self):
        return (
            self.quantities.crack_sealing_length
            * self.crack_sealing_rate
        )

    @property
    def pothole_cost(self):
        return (
            self.quantities.pothole_count
            * self.pothole_rate
        )

    @property
    def shoulder_cost(self):
        return (
            self.quantities.shoulder_repair_length
            * self.shoulder_rate
        )

    @property
    def drainage_cost(self):
        return (
            self.quantities.drainage_cleaning_length
            * self.drainage_rate
        )

    @property
    def sign_cost(self):
        return (
            self.quantities.sign_replacement_count
            * self.sign_rate
        )

    @property
    def marking_cost(self):
        return (
            self.quantities.marking_area
            * self.marking_rate
        )

    @property
    def guardrail_cost(self):
        return (
            self.quantities.guardrail_length
            * self.guardrail_rate
        )

    # ========================================================
    # Totals
    # ========================================================

    @property
    def direct_cost(self):

        return (

            self.pavement_repair_cost

            + self.crack_sealing_cost

            + self.pothole_cost

            + self.shoulder_cost

            + self.drainage_cost

            + self.sign_cost

            + self.marking_cost

            + self.guardrail_cost

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

            "pavement_repair_cost": self.pavement_repair_cost,

            "crack_sealing_cost": self.crack_sealing_cost,

            "pothole_cost": self.pothole_cost,

            "shoulder_cost": self.shoulder_cost,

            "drainage_cost": self.drainage_cost,

            "sign_cost": self.sign_cost,

            "marking_cost": self.marking_cost,

            "guardrail_cost": self.guardrail_cost,

            "direct_cost": self.direct_cost,

            "indirect_cost": self.indirect_cost,

            "tax": self.tax,

            "total_cost": self.total_cost

        }