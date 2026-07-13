"""
Horizontal Sightline Offset (HSO) Calculator

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

This module calculates the required Horizontal Sightline Offset (HSO)
for horizontal curves according to the AASHTO Green Book.

Author:
Eng. Muhammed

Research:
MSc Research
Cairo University
"""

from dataclasses import dataclass
import math


@dataclass
class HSOResult:
    """
    Stores Horizontal Sightline Offset calculation results.
    """

    radius: float

    stopping_sight_distance: float

    horizontal_sightline_offset: float

    satisfies_requirement: bool


class HSOCalculator:
    """
    Calculates the required Horizontal Sightline Offset (HSO).
    """

    def calculate(
        self,
        radius: float,
        stopping_sight_distance: float,
        available_offset: float,
    ) -> HSOResult:

        # Central angle (degrees)
        theta = 28.65 * stopping_sight_distance / radius

        # Convert to radians
        theta_rad = math.radians(theta)

        # AASHTO Equation
        hso = radius * (1 - math.cos(theta_rad))

        satisfies = available_offset >= hso

        return HSOResult(
            radius=radius,
            stopping_sight_distance=stopping_sight_distance,
            horizontal_sightline_offset=hso,
            satisfies_requirement=satisfies,
        )
