"""
total_project_cost.py
=====================

Total Project Cost Calculation Engine

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 2.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(slots=True)
class CostComponent:
    """
    Represents one project cost component.
    """

    name: str

    summary: Dict


class TotalProjectCostCalculator:
    """
    Aggregates all project cost modules into a single report.
    """

    def __init__(self):

        self.components: List[CostComponent] = []

    # =========================================================

    def add_component(
        self,
        name: str,
        summary: Dict
    ):

        self.components.append(
            CostComponent(name, summary)
        )

    # =========================================================

    @property
    def direct_cost(self):

        return sum(

            c.summary.get("direct_cost", 0.0)

            for c in self.components

        )

    # =========================================================

    @property
    def indirect_cost(self):

        return sum(

            c.summary.get("indirect_cost", 0.0)

            for c in self.components

        )

    # =========================================================

    @property
    def tax(self):

        return sum(

            c.summary.get("tax", 0.0)

            for c in self.components

        )

    # =========================================================

    @property
    def total_cost(self):

        return sum(

            c.summary.get("total_cost", 0.0)

            for c in self.components

        )

    # =========================================================

    @property
    def currency(self):

        if not self.components:

            return "Undefined"

        return self.components[0].summary.get(

            "currency",

            "Undefined"

        )

    # =========================================================

    def summary(self):

        return {

            "currency": self.currency,

            "components": {

                c.name: c.summary

                for c in self.components

            },

            "direct_cost": self.direct_cost,

            "indirect_cost": self.indirect_cost,

            "tax": self.tax,

            "total_cost": self.total_cost

        }

    # =========================================================

    def clear(self):

        self.components.clear()