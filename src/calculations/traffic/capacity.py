"""
Traffic Capacity Calculator

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

This module calculates the roadway capacity using a simplified
capacity model. The implementation is intentionally modular so it
can later be replaced by the full HCM methodology.

Author:
Eng. Muhammed

Research:
MSc Research
Cairo University
"""

from dataclasses import dataclass

from models.geometry.road_geometry import RoadGeometry
from models.traffic.traffic_data import TrafficData


@dataclass
class CapacityResult:
    """
    Stores traffic capacity calculation results.
    """

    demand: float

    capacity: float

    volume_to_capacity_ratio: float

    satisfies_constraint: bool


class CapacityCalculator:
    """
    Calculates roadway capacity.

    Current implementation uses a simplified model.

    Future versions will implement the complete HCM methodology.
    """

    def __init__(
        self,
        geometry: RoadGeometry,
        traffic: TrafficData,
    ):

        self.geometry = geometry
        self.traffic = traffic

    def calculate(self) -> CapacityResult:

        # ----------------------------------------
        # Simplified Capacity Model
        # ----------------------------------------

        lane_factor = (
            self.geometry.lane_width / 3.60
        )

        capacity = (
            2200
            * lane_factor
            * self.geometry.lanes_per_direction
        )

        demand = self.traffic.demand

        vc_ratio = demand / capacity

        satisfies = vc_ratio <= 0.90

        return CapacityResult(
            demand=demand,
            capacity=capacity,
            volume_to_capacity_ratio=vc_ratio,
            satisfies_constraint=satisfies,
        )
