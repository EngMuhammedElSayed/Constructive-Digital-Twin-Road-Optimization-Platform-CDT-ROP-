"""
capacity.py
===========

Traffic Capacity Calculation Engine

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Based on:
Highway Capacity Manual (HCM)

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


# ==========================================================
# Input Model
# ==========================================================

@dataclass(slots=True)
class CapacityInput:
    """
    Roadway characteristics only.

    All HCM adjustment factors are obtained
    automatically from the Standards Provider.
    """

    road_type: str

    terrain_type: str

    number_of_lanes: int

    lane_width: float

    shoulder_width: float

    median_type: str

    access_point_density: float

    heavy_vehicle_percentage: float

    peak_hour_factor: float

    grade: float

    driver_population: str = "commuter"


# ==========================================================
# Capacity Calculator
# ==========================================================

class CapacityCalculator:

    def __init__(

        self,

        data: CapacityInput,

        standards

    ):

        self.data = data

        self.std = standards

        self._validate()

    # ------------------------------------------------------

    def _validate(self):

        if self.data.number_of_lanes <= 0:

            raise ValueError(
                "Number of lanes must be greater than zero."
            )

        if self.data.lane_width <= 0:

            raise ValueError(
                "Lane width must be greater than zero."
            )

    # ------------------------------------------------------
    # Factors
    # ------------------------------------------------------

    @property
    def base_capacity(self):

        return self.std.base_capacity(

            self.data.road_type

        )

    @property
    def lane_width_factor(self):

        return self.std.lane_width_factor(

            self.data.lane_width

        )

    @property
    def shoulder_factor(self):

        return self.std.shoulder_factor(

            self.data.shoulder_width

        )

    @property
    def heavy_vehicle_factor(self):

        return self.std.heavy_vehicle_factor(

            self.data.heavy_vehicle_percentage,

            self.data.grade,

            self.data.terrain_type

        )

    @property
    def driver_population_factor(self):

        return self.std.driver_population_factor(

            self.data.driver_population

        )

    @property
    def access_factor(self):

        return self.std.access_density_factor(

            self.data.access_point_density

        )

    # ------------------------------------------------------

    @property
    def adjustment_factor(self):

        return (

            self.data.peak_hour_factor

            * self.lane_width_factor

            * self.shoulder_factor

            * self.heavy_vehicle_factor

            * self.driver_population_factor

            * self.access_factor

        )

    # ------------------------------------------------------

    @property
    def lane_capacity(self):

        return (

            self.base_capacity

            * self.adjustment_factor

        )

    # ------------------------------------------------------

    @property
    def roadway_capacity(self):

        return (

            self.lane_capacity

            * self.data.number_of_lanes

        )

    # ------------------------------------------------------

    def summary(self):

        return {

            "road_type":
                self.data.road_type,

            "terrain_type":
                self.data.terrain_type,

            "number_of_lanes":
                self.data.number_of_lanes,

            "base_capacity":
                self.base_capacity,

            "adjustment_factor":
                self.adjustment_factor,

            "lane_capacity":
                self.lane_capacity,

            "roadway_capacity":
                self.roadway_capacity

        }