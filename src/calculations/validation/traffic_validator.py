"""
traffic_validator.py
====================

Traffic Validation Engine

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
# Traffic Validator
# ==========================================================

class TrafficValidator:

    """
    Validate traffic engineering inputs using
    the active traffic standards provider.
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

    def validate_non_negative(

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

        if value < 0:

            result.add_error(
                f"{name} cannot be negative."
            )

    # ------------------------------------------------------

    def validate_aadt(

        self,

        aadt: float,

        result: ValidationResult

    ):

        self.validate_positive(

            "AADT",

            aadt,

            result

        )

        maximum = self.std.maximum_aadt()

        if aadt > maximum:

            result.add_warning(

                f"AADT exceeds recommended value "
                f"({maximum:.0f})."

            )

    # ------------------------------------------------------

    def validate_design_speed(

        self,

        speed: float,

        result: ValidationResult

    ):

        self.validate_positive(

            "Design Speed",

            speed,

            result

        )

        maximum = self.std.maximum_design_speed()

        if speed > maximum:

            result.add_warning(

                f"Design speed exceeds "
                f"{maximum:.0f} km/h."

            )

    # ------------------------------------------------------

    def validate_peak_hour_factor(

        self,

        phf: float,

        result: ValidationResult

    ):

        if phf <= 0 or phf > 1:

            result.add_error(

                "Peak Hour Factor must be between 0 and 1."

            )

    # ------------------------------------------------------

    def validate_heavy_vehicle_percentage(

        self,

        hv: float,

        result: ValidationResult

    ):

        if hv < 0 or hv > 100:

            result.add_error(

                "Heavy vehicle percentage must be between 0 and 100."

            )

    # ------------------------------------------------------

    def validate_lane_count(

        self,

        lanes: int,

        result: ValidationResult

    ):

        if lanes <= 0:

            result.add_error(

                "Number of lanes must be greater than zero."

            )

    # ------------------------------------------------------

    def validate_lane_width(

        self,

        width: float,

        result: ValidationResult

    ):

        minimum = self.std.minimum_lane_width()

        maximum = self.std.maximum_lane_width()

        if width < minimum:

            result.add_error(

                f"Lane width is below "
                f"{minimum:.2f} m."

            )

        if width > maximum:

            result.add_warning(

                f"Lane width exceeds "
                f"{maximum:.2f} m."

            )

    # ------------------------------------------------------

    def validate_capacity(

        self,

        capacity: float,

        result: ValidationResult

    ):

        self.validate_positive(

            "Capacity",

            capacity,

            result

        )

    # ------------------------------------------------------

    def validate_volume(

        self,

        volume: float,

        result: ValidationResult

    ):

        self.validate_non_negative(

            "Traffic Volume",

            volume,

            result

        )

    # ------------------------------------------------------

    def validate_vc_ratio(

        self,

        ratio: float,

        result: ValidationResult

    ):

        if ratio < 0:

            result.add_error(

                "V/C ratio cannot be negative."

            )

        if ratio > 1:

            result.add_warning(

                "V/C ratio is greater than 1.0 "
                "(oversaturated condition)."

            )

    # ------------------------------------------------------

    def validate_level_of_service(

        self,

        los: str,

        result: ValidationResult

    ):

        allowed = ["A", "B", "C", "D", "E", "F"]

        if los not in allowed:

            result.add_error(

                "Invalid Level of Service."

            )
