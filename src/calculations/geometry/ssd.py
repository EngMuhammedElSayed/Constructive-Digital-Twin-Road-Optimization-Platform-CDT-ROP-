"""
Stopping Sight Distance (SSD) Calculator

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

This module calculates the required Stopping Sight Distance (SSD)
according to the AASHTO Green Book.

Author:
Eng. Muhammed

Research:
MSc Research
Cairo University
"""

from dataclasses import dataclass


@dataclass
class SSDResult:
    """
    Stores SSD calculation results.
    """

    design_speed: float

    grade: float

    perception_reaction_time: float

    comfortable_deceleration: float

    stopping_sight_distance: float


class SSDCalculator:
    """
    Calculates the required Stopping Sight Distance (SSD)
    using the AASHTO equation.
    """

    def calculate(
        self,
        design_speed: float,
        grade: float,
        perception_reaction_time: float = 2.5,
        comfortable_deceleration: float = 3.4,
    ) -> SSDResult:

        # ------------------------------------------
        # Perception-Reaction Distance
        # ------------------------------------------

        reaction_distance = (
            0.278
            * design_speed
            * perception_reaction_time
        )

        # ------------------------------------------
        # Braking Distance
        # ------------------------------------------

        braking_distance = (
            design_speed ** 2
        ) / (
            254
            * (
                comfortable_deceleration / 9.81
                + grade / 100
            )
        )

        # ------------------------------------------
        # Total SSD
        # ------------------------------------------

        ssd = reaction_distance + braking_distance

        return SSDResult(
            design_speed=design_speed,
            grade=grade,
            perception_reaction_time=perception_reaction_time,
            comfortable_deceleration=comfortable_deceleration,
            stopping_sight_distance=ssd,
        )
