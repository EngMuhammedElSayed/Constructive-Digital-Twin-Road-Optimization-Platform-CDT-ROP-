"""
ssd.py
======

Stopping Sight Distance (SSD)

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Based on:
AASHTO Green Book

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
class SSDInput:
    """
    Stopping Sight Distance Input

    speed : km/h

    perception_reaction_time : sec

    friction : decimal

    grade : decimal
        +0.03 = +3%
        -0.04 = -4%
    """

    speed: float

    perception_reaction_time: float

    friction: float

    grade: float = 0.0


# ==========================================================
# Calculator
# ==========================================================

class SSDCalculator:

    def __init__(self, data: SSDInput):

        self.data = data

        self._validate()

    # ------------------------------------------------------

    def _validate(self):

        if self.data.speed <= 0:

            raise ValueError(
                "Speed must be greater than zero."
            )

        if self.data.perception_reaction_time <= 0:

            raise ValueError(
                "Perception-reaction time must be greater than zero."
            )

        if self.data.friction <= 0:

            raise ValueError(
                "Friction coefficient must be greater than zero."
            )

        if self.data.grade < -0.15 or self.data.grade > 0.15:

            raise ValueError(
                "Grade should be between -15% and +15%."
            )

    # ------------------------------------------------------

    @property
    def reaction_distance(self) -> float:
        """
        Reaction Distance

        RD = 0.278 × V × t
        """

        return (
            0.278
            * self.data.speed
            * self.data.perception_reaction_time
        )

    # ------------------------------------------------------

    @property
    def braking_distance(self) -> float:
        """
        Braking Distance

        BD = V² / (254(f + G))
        """

        denominator = 254 * (
            self.data.friction
            + self.data.grade
        )

        if denominator <= 0:

            raise ValueError(
                "Invalid braking denominator."
            )

        return (
            self.data.speed ** 2
        ) / denominator

    # ------------------------------------------------------

    @property
    def stopping_sight_distance(self) -> float:

        return (

            self.reaction_distance

            + self.braking_distance

        )

    # ------------------------------------------------------

    @property
    def is_upgrade(self):

        return self.data.grade > 0

    # ------------------------------------------------------

    @property
    def is_downgrade(self):

        return self.data.grade < 0

    # ------------------------------------------------------

    @property
    def grade_percent(self):

        return self.data.grade * 100

    # ------------------------------------------------------

    def summary(self) -> Dict:

        return {

            "speed_kmh": self.data.speed,

            "perception_reaction_time_sec":
                self.data.perception_reaction_time,

            "friction":
                self.data.friction,

            "grade":
                self.data.grade,

            "grade_percent":
                self.grade_percent,

            "reaction_distance":
                self.reaction_distance,

            "braking_distance":
                self.braking_distance,

            "ssd":
                self.stopping_sight_distance

        }