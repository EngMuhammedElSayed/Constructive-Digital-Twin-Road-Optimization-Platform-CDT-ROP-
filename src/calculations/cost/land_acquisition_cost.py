"""
land_acquisition_cost.py
========================

Land Acquisition Cost Calculation Engine

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
class LandAcquisitionQuantities:
    """
    Land acquisition quantities.
    """

    urban_land_area: float = 0.0          # m²

    rural_land_area: float = 0.0          # m²

    agricultural_land_area: float = 0.0  # m²

    industrial_land_area: float = 0.0    # m²

    residential_buildings: int = 0

    commercial_buildings: int = 0

    utility_relocation_count: int = 0

    legal_cases: int = 0


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

class LandAcquisitionCostCalculator:

    def __init__(

        self,

        quantities: LandAcquisitionQuantities,

        cost_database: CostDatabase,

        factors: CostFactors | None = None

    ):

        self.quantities = quantities
        self.db = cost_database
        self.factors = factors or CostFactors()

    # ========================================================
    # Rates
    # ========================================================

    @property
    def urban_land_rate(self):
        return self.db.get_rate("land", "Urban Land")

    @property
    def rural_land_rate(self):
        return self.db.get_rate("land", "Rural Land")

    @property
    def agricultural_land_rate(self):
        return self.db.get_rate("land", "Agricultural Land")

    @property
    def industrial_land_rate(self):
        return self.db.get_rate("land", "Industrial Land")

    @property
    def residential_building_rate(self):
        return self.db.get_rate("land", "Residential Building")

    @property
    def commercial_building_rate(self):
        return self.db.get_rate("land", "Commercial Building")

    @property
    def utility_relocation_rate(self):
        return self.db.get_rate("land", "Utility Relocation")

    @property
    def legal_case_rate(self):
        return self.db.get_rate("land", "Legal Case")

    # ========================================================
    # Cost Items
    # ========================================================

    @property
    def urban_land_cost(self):
        return self.quantities.urban_land_area * self.urban_land_rate

    @property
    def rural_land_cost(self):
        return self.quantities.rural_land_area * self.rural_land_rate

    @property
    def agricultural_land_cost(self):
        return (
            self.quantities.agricultural_land_area
            * self.agricultural_land_rate
        )

    @property
    def industrial_land_cost(self):
        return (
            self.quantities.industrial_land_area
            * self.industrial_land_rate
        )

    @property
    def residential_building_cost(self):
        return (
            self.quantities.residential_buildings
            * self.residential_building_rate
        )

    @property
    def commercial_building_cost(self):
        return (
            self.quantities.commercial_buildings
            * self.commercial_building_rate
        )

    @property
    def utility_relocation_cost(self):
        return (
            self.quantities.utility_relocation_count
            * self.utility_relocation_rate
        )

    @property
    def legal_cost(self):
        return (
            self.quantities.legal_cases
            * self.legal_case_rate
        )

    # ========================================================
    # Totals
    # ========================================================

    @property
    def direct_cost(self):

        return (

            self.urban_land_cost

            + self.rural_land_cost

            + self.agricultural_land_cost

            + self.industrial_land_cost

            + self.residential_building_cost

            + self.commercial_building_cost

            + self.utility_relocation_cost

            + self.legal_cost

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

            "urban_land_cost": self.urban_land_cost,

            "rural_land_cost": self.rural_land_cost,

            "agricultural_land_cost": self.agricultural_land_cost,

            "industrial_land_cost": self.industrial_land_cost,

            "residential_building_cost": self.residential_building_cost,

            "commercial_building_cost": self.commercial_building_cost,

            "utility_relocation_cost": self.utility_relocation_cost,

            "legal_cost": self.legal_cost,

            "direct_cost": self.direct_cost,

            "indirect_cost": self.indirect_cost,

            "tax": self.tax,

            "total_cost": self.total_cost

        }