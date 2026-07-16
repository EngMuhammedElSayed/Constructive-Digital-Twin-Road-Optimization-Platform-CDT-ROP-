"""
hso.py
======

Horizontal Sightline Offset (HSO)

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Based on:
AASHTO Green Book

Author : CDT-ROP Team
Version: 2.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, radians


# ==========================================================
# Input Model
# ==========================================================

@dataclass(slots=True)
class HSOInput:
    """
    Horizontal Sightline Offset Input

    Parameters
    ----------
    curve_radius : float
        Radius of horizontal curve (m)

    curve_length : float
        Length of horizontal curve (m)

    sight_distance : float
        Required sight distance (SSD / PSD / DSD) (m)

    central_angle : float
        Curve central angle (degree)
    """

    curve_radius: float

    curve_length: float

    sight_distance: float

    central_angle: float


# ==========================================================
# Calculator
# ==========================================================

class HSOCalculator:

    def __init__(self, data: HSOInput):

        self.data = data

    # ------------------------------------------------------

    @property
    def radius(self):

        return self.data.curve_radius

    # ------------------------------------------------------

    @property
    def length(self):

        return self.data.curve_length

    # ------------------------------------------------------

    @property
    def sight_distance(self):

        return self.data.sight_distance

    # ------------------------------------------------------

    @property
    def central_angle_rad(self):

        return radians(self.data.central_angle)

    # ------------------------------------------------------

    @property
    def case(self):

        """
        Determine AASHTO case.
        """

        if self.sight_distance <= self.length:

            return "S <= L"

        return "S > L"

    # ------------------------------------------------------

    @property
    def required_hso(self):

        """
        Horizontal Sightline Offset

        Case 1
        -------
        S <= L

        M = R (1 - cos(S / 2R))

        Case 2
        -------
        S > L

        M = R (1 - cos((L / 2R) * (1 - (S - L)/S)))
        """

        R = self.radius

        S = self.sight_distance

        L = self.length

        if S <= L:

            theta = S / R

            return R * (1 - cos(theta / 2))

        theta = (L / R) * (1 - ((S - L) / S))

        return R * (1 - cos(theta / 2))

    # ------------------------------------------------------

    def summary(self):

        return {

            "curve_radius": self.radius,

            "curve_length": self.length,

            "central_angle": self.data.central_angle,

            "sight_distance": self.sight_distance,

            "case": self.case,

            "required_hso": self.required_hso

        }