"""
lifecycle_cost.py
=================

Life Cycle Cost Analysis (LCCA)

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 2.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


# ============================================================
# Input Models
# ============================================================

@dataclass(slots=True)
class LifecycleEvent:
    """
    Future cost event.
    """

    name: str

    year: int

    cost: float


@dataclass(slots=True)
class LifecycleInputs:
    """
    Life cycle analysis inputs.
    """

    initial_cost: float

    design_life: int

    discount_rate: float

    salvage_value: float = 0.0

    maintenance_events: List[LifecycleEvent] | None = None

    rehabilitation_events: List[LifecycleEvent] | None = None

    operation_events: List[LifecycleEvent] | None = None


# ============================================================
# Calculator
# ============================================================

class LifecycleCostCalculator:

    def __init__(

        self,

        inputs: LifecycleInputs

    ):

        self.inputs = inputs

    # ========================================================
    # Discounting
    # ========================================================

    def present_worth(

        self,

        future_cost: float,

        year: int

    ) -> float:

        return (

            future_cost

            / ((1 + self.inputs.discount_rate) ** year)

        )

    # ========================================================
    # Maintenance
    # ========================================================

    @property
    def maintenance_pw(self):

        total = 0.0

        events = self.inputs.maintenance_events or []

        for event in events:

            total += self.present_worth(

                event.cost,

                event.year

            )

        return total

    # ========================================================
    # Rehabilitation
    # ========================================================

    @property
    def rehabilitation_pw(self):

        total = 0.0

        events = self.inputs.rehabilitation_events or []

        for event in events:

            total += self.present_worth(

                event.cost,

                event.year

            )

        return total

    # ========================================================
    # Operation
    # ========================================================

    @property
    def operation_pw(self):

        total = 0.0

        events = self.inputs.operation_events or []

        for event in events:

            total += self.present_worth(

                event.cost,

                event.year

            )

        return total

    # ========================================================
    # Salvage
    # ========================================================

    @property
    def salvage_pw(self):

        return self.present_worth(

            self.inputs.salvage_value,

            self.inputs.design_life

        )

    # ========================================================
    # Total LCCA
    # ========================================================

    @property
    def total_present_worth(self):

        return (

            self.inputs.initial_cost

            + self.maintenance_pw

            + self.rehabilitation_pw

            + self.operation_pw

            - self.salvage_pw

        )

    # ========================================================
    # Summary
    # ========================================================

    def summary(self) -> Dict:

        return {

            "design_life": self.inputs.design_life,

            "discount_rate": self.inputs.discount_rate,

            "initial_cost": self.inputs.initial_cost,

            "maintenance_pw": self.maintenance_pw,

            "rehabilitation_pw": self.rehabilitation_pw,

            "operation_pw": self.operation_pw,

            "salvage_pw": self.salvage_pw,

            "total_present_worth":

                self.total_present_worth

        }