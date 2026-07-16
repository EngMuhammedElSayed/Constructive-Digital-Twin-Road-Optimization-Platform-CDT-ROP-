"""
geometry_validator.py
=====================

Geometry Validation Engine

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


# ==========================================================
# Validation Result
# ==========================================================

@dataclass(slots=True)
class ValidationResult:

    valid: bool = True

    errors: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    def add_error(self, message: str):

        self.valid = False
        self.errors.append(message)

    def add_warning(self, message: str):

        self.warnings.append(message)


# ==========================================================
# Geometry Validator
# ==========================================================

class GeometryValidator:

    """
    Validate roadway geometry using the active
    design standard provider.
    """

    def __init__(self, standards):

        self.std = standards

    # ------------------------------------------------------

    @staticmethod
    def _is_number(value):

        return isinstance(value, (int, float))

    # ------------------------------------------------------

    def validate_positive(

        self,

        name: str,

        value: Any,

        result: ValidationResult

    ):

        if value is None:

            result.add_error(f"{name} is missing.")
            return

        if not self._is_number(value):

            result.add_error(f"{name} must be numeric.")
            return

        if value <= 0:

            result.add_error(
                f"{name} must be greater than zero."
            )

    # ------------------------------------------------------

    def validate_speed(

        self,

        speed: float,

        result: ValidationResult

    ):

        self.validate_positive(

            "Design Speed",

            speed,

            result

        )

        max_speed = self.std.maximum_design_speed()

        if speed > max_speed:

            result.add_warning(

                f"Design speed exceeds "

                f"{max_speed} km/h."

            )

    # ------------------------------------------------------

    def validate_radius(

        self,

        radius: float,

        speed: float,

        result: ValidationResult

    ):

        self.validate_positive(

            "Horizontal Radius",

            radius,

            result

        )

        minimum = self.std.minimum_radius(speed)

        if radius < minimum:

            result.add_error(

                f"Radius is smaller than "

                f"minimum allowable "

                f"({minimum:.2f} m)."

            )

    # ------------------------------------------------------

    def validate_grade(

        self,

        grade: float,

        result: ValidationResult

    ):

        maximum = self.std.maximum_grade()

        minimum = self.std.minimum_grade()

        if grade > maximum:

            result.add_error(

                f"Grade exceeds "

                f"{maximum*100:.1f}%."

            )

        if grade < minimum:

            result.add_error(

                f"Grade is smaller than "

                f"{minimum*100:.1f}%."

            )

    # ------------------------------------------------------

    def validate_lane_width(

        self,

        width: float,

        result: ValidationResult

    ):

        self.validate_positive(

            "Lane Width",

            width,

            result

        )

        minimum = self.std.minimum_lane_width()

        maximum = self.std.maximum_lane_width()

        if width < minimum:

            result.add_error(

                f"Lane width smaller than "

                f"{minimum:.2f} m."

            )

        if width > maximum:

            result.add_warning(

                f"Lane width exceeds "

                f"{maximum:.2f} m."

            )

    # ------------------------------------------------------

    def validate_shoulder_width(

        self,

        width: float,

        result: ValidationResult

    ):

        minimum = self.std.minimum_shoulder_width()

        if width < minimum:

            result.add_warning(

                f"Shoulder width is below "

                f"{minimum:.2f} m."

            )

    # ------------------------------------------------------

    def validate_superelevation(

        self,

        e: float,

        result: ValidationResult

    ):

        maximum = self.std.maximum_superelevation()

        if e < 0:

            result.add_error(

                "Superelevation cannot be negative."

            )

        if e > maximum:

            result.add_error(

                f"Superelevation exceeds "

                f"{maximum:.3f}."

            )

    # ------------------------------------------------------

    def validate_cross_slope(

        self,

        slope: float,

        result: ValidationResult

    ):

        maximum = self.std.maximum_cross_slope()

        if abs(slope) > maximum:

            result.add_warning(

                f"Cross slope exceeds "

                f"{maximum:.3f}."

            )

    # ------------------------------------------------------

    def validate_station(

        self,

        station: float,

        result: ValidationResult

    ):

        if station < 0:

            result.add_error(

                "Station cannot be negative."

            )

    # ------------------------------------------------------

    def validate_alignment_length(

        self,

        length: float,

        result: ValidationResult

    ):

        self.validate_positive(

            "Alignment Length",

            length,

            result

        )
