"""
cost_report.py
==============

Cost Report Generator

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


# ==========================================================
# Report Model
# ==========================================================

@dataclass(slots=True)
class CostReport:

    project_name: str

    currency: str = "Undefined"

    sections: Dict[str, Dict] = field(default_factory=dict)

    notes: List[str] = field(default_factory=list)

    # ------------------------------------------------------

    def add_section(

        self,

        name: str,

        summary: Dict

    ):

        """
        Adds a calculation summary to the report.

        Example:
            Earthwork
            Bridge
            Pavement
            Traffic
        """

        self.sections[name] = summary

    # ------------------------------------------------------

    def add_note(

        self,

        note: str

    ):

        self.notes.append(note)

    # ------------------------------------------------------

    @property
    def direct_cost(self):

        return sum(

            section.get("direct_cost", 0)

            for section in self.sections.values()

        )

    # ------------------------------------------------------

    @property
    def indirect_cost(self):

        return sum(

            section.get("indirect_cost", 0)

            for section in self.sections.values()

        )

    # ------------------------------------------------------

    @property
    def tax(self):

        return sum(

            section.get("tax", 0)

            for section in self.sections.values()

        )

    # ------------------------------------------------------

    @property
    def total_cost(self):

        return sum(

            section.get("total_cost", 0)

            for section in self.sections.values()

        )

    # ------------------------------------------------------

    def summary(self):

        return {

            "project": self.project_name,

            "currency": self.currency,

            "sections": list(self.sections.keys()),

            "direct_cost": self.direct_cost,

            "indirect_cost": self.indirect_cost,

            "tax": self.tax,

            "total_cost": self.total_cost,

            "notes": self.notes

        }

    # ------------------------------------------------------

    def clear(self):

        self.sections.clear()

        self.notes.clear()