"""
cost_validator.py
=================

Cost Data Validation Engine

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 2.0.0
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
# Cost Validator
# ==========================================================

class CostValidator:

    """
    Validate cost quantities and unit rates before calculations.
    """

    # ------------------------------------------------------

    @staticmethod
    def validate_quantity(

        name: str,

        value: Any,

        result: ValidationResult

    ):

        if value is None:

            result.add_error(

                f"{name} is missing."

            )

            return

        if not isinstance(value, (int, float)):

            result.add_error(

                f"{name} must be numeric."

            )

            return

        if value < 0:

            result.add_error(

                f"{name} cannot be negative."

            )

    # ------------------------------------------------------

    @staticmethod
    def validate_rate(

        name: str,

        value: Any,

        result: ValidationResult

    ):

        if value is None:

            result.add_error(

                f"Unit rate '{name}' is missing."

            )

            return

        if not isinstance(value, (int, float)):

            result.add_error(

                f"Unit rate '{name}' must be numeric."

            )

            return

        if value < 0:

            result.add_error(

                f"Unit rate '{name}' cannot be negative."

            )

    # ------------------------------------------------------

    @staticmethod
    def validate_currency(

        currency: str,

        result: ValidationResult

    ):

        if currency is None:

            result.add_error(

                "Currency is missing."

            )

            return

        if currency.strip() == "":

            result.add_error(

                "Currency cannot be empty."

            )

    # ------------------------------------------------------

    @staticmethod
    def validate_dictionary(

        values: dict,

        result: ValidationResult

    ):

        if len(values) == 0:

            result.add_error(

                "Input dictionary is empty."

            )

    # ------------------------------------------------------

    @staticmethod
    def validate_cost_database(

        database,

    ) -> ValidationResult:

        result = ValidationResult()

        if database is None:

            result.add_error(

                "Cost database is missing."

            )

            return result

        CostValidator.validate_currency(

            database.currency,

            result

        )

        return result
