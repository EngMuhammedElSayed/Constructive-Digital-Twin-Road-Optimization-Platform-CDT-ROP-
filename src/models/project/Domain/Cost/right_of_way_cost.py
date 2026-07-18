"""
right_of_way_cost.py
====================

Right-of-Way Cost Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents right-of-way (ROW) costs associated with
roadway projects.

This module stores ROW cost information only.

No land valuation, property appraisal, compensation,
or acquisition calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class RightOfWayCost:
    """
    Represents right-of-way acquisition costs.
    """

    # =====================================================
    # Land Acquisition
    # =====================================================

    land_acquisition_cost: float = 0.0

    # =====================================================
    # Property Compensation
    # =====================================================

    building_compensation_cost: float = 0.0

    structure_compensation_cost: float = 0.0

    business_compensation_cost: float = 0.0

    # =====================================================
    # Relocation
    # =====================================================

    relocation_cost: float = 0.0

    utility_relocation_cost: float = 0.0

    # =====================================================
    # Legal & Administrative
    # =====================================================

    legal_cost: float = 0.0

    surveying_cost: float = 0.0

    appraisal_cost: float = 0.0

    permit_cost: float = 0.0

    # =====================================================
    # Miscellaneous
    # =====================================================

    miscellaneous_cost: float = 0.0

    # =====================================================
    # Currency
    # =====================================================

    currency: str = "EGP"

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)

    # =====================================================
    # Read-Only Properties
    # =====================================================

    @property
    def total_cost(self) -> float:
        """
        Returns the total right-of-way cost.
        """
        return (
            self.land_acquisition_cost
            + self.building_compensation_cost
            + self.structure_compensation_cost
            + self.business_compensation_cost
            + self.relocation_cost
            + self.utility_relocation_cost
            + self.legal_cost
            + self.surveying_cost
            + self.appraisal_cost
            + self.permit_cost
            + self.miscellaneous_cost
        )