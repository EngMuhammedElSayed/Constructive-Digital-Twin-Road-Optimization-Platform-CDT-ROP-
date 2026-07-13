"""
Pavement Cost Calculation

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

This module calculates pavement construction cost using
roadway geometric data and unit prices.

Author:
Eng. Muhammed

Research:
MSc Research
Cairo University
"""

from dataclasses import dataclass

from models.cost.cost_parameters import CostParameters
from models.geometry.road_geometry import RoadGeometry


@dataclass
class PavementCostResult:
    """
    Stores pavement cost calculation results.
    """

    pavement_area: float

    pavement_cost: float


class PavementCostCalculator:
    """
    Calculates pavement construction cost.

    This class calculates the total paved area using the roadway
    geometry and multiplies it by the pavement unit cost.
    """

    def __init__(self, geometry: RoadGeometry, cost: CostParameters):

        self.geometry = geometry
        self.cost = cost

    def calculate(self, road_length: float) -> PavementCostResult:

        pavement_width = (
            self.geometry.lanes_per_direction
            * 2
            * self.geometry.lane_width
            + 2 * self.geometry.shoulder_width
        )

        pavement_area = pavement_width * road_length

        pavement_cost = (
            pavement_area
            * self.cost.pavement_cost_per_m2
        )

        return PavementCostResult(
            pavement_area=pavement_area,
            pavement_cost=pavement_cost
        )
