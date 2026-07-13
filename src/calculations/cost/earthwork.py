"""
Earthwork Cost Calculation

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

This module calculates earthwork costs using previously computed
earthwork quantities.

Author:
Eng. Muhammed

Research:
MSc Research
Cairo University
"""

from dataclasses import dataclass

from models.cost.cost_parameters import CostParameters


@dataclass
class EarthworkCostResult:
    """
    Stores earthwork cost calculation results.
    """

    cut_cost: float

    fill_cost: float

    borrow_cost: float

    unsuitable_material_cost: float

    haul_cost: float

    total_cost: float


class EarthworkCostCalculator:
    """
    Calculates total earthwork cost.

    This class assumes that all earthwork volumes have already been
    computed by the Earthwork Volume Engine.
    """

    def __init__(self, cost: CostParameters):

        self.cost = cost

    def calculate(
        self,
        cut_volume: float,
        fill_volume: float,
        borrow_volume: float = 0.0,
        unsuitable_volume: float = 0.0,
        haul_distance_km: float = 0.0,
    ) -> EarthworkCostResult:

        cut_cost = cut_volume * self.cost.cut_cost_per_m3

        fill_cost = fill_volume * self.cost.fill_cost_per_m3

        borrow_cost = borrow_volume * self.cost.borrow_material_cost_per_m3

        unsuitable_cost = (
            unsuitable_volume *
            self.cost.unsuitable_material_cost_per_m3
        )

        haul_cost = (
            cut_volume *
            haul_distance_km *
            self.cost.haul_cost_per_m3_km
        )

        total = (
            cut_cost +
            fill_cost +
            borrow_cost +
            unsuitable_cost +
            haul_cost
        )

        return EarthworkCostResult(
            cut_cost=cut_cost,
            fill_cost=fill_cost,
            borrow_cost=borrow_cost,
            unsuitable_material_cost=unsuitable_cost,
            haul_cost=haul_cost,
            total_cost=total
        )
