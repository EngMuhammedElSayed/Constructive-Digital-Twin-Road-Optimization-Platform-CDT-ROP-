"""
Right-of-Way (ROW) Cost Calculation

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

This module calculates the Right-of-Way (ROW) acquisition cost
based on roadway geometry and land acquisition unit prices.

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
class ROWCostResult:
    """
    Stores Right-of-Way cost calculation results.
    """

    row_width: float

    row_area: float

    land_cost: float

    compensation_cost: float

    total_row_cost: float


class ROWCostCalculator:
    """
    Calculates Right-of-Way acquisition cost.
    """

    def __init__(
        self,
        geometry: RoadGeometry,
        cost: CostParameters,
    ):

        self.geometry = geometry
        self.cost = cost

    def calculate(self, road_length: float) -> ROWCostResult:

        # ------------------------------------------
        # Total Right-of-Way Width
        # ------------------------------------------

        row_width = (
            self.geometry.lanes_per_direction * 2
            * self.geometry.lane_width
            + 2 * self.geometry.shoulder_width
            + self.geometry.median_width
            + 2 * self.geometry.clear_zone_width
        )

        # ------------------------------------------
        # Area
        # ------------------------------------------

        row_area = row_width * road_length

        # ------------------------------------------
        # Costs
        # ------------------------------------------

        land_cost = (
            row_area
            * self.cost.row_cost_per_m2
        )

        compensation_cost = self.cost.compensation_cost

        total_cost = (
            land_cost
            + compensation_cost
        )

        return ROWCostResult(
            row_width=row_width,
            row_area=row_area,
            land_cost=land_cost,
            compensation_cost=compensation_cost,
            total_row_cost=total_cost,
        )
