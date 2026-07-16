"""
currency.py
===========

Currency Management Module

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass


# ==========================================================
# Currency Model
# ==========================================================

@dataclass(slots=True)
class Currency:

    code: str
    symbol: str
    name: str

    exchange_rate: float = 1.0
    decimal_places: int = 2


# ==========================================================
# Currency Manager
# ==========================================================

class CurrencyManager:

    def __init__(self):

        self._currencies = {}

        self._current = None

    # ------------------------------------------------------

    def register(self, currency: Currency):

        self._currencies[currency.code] = currency

        if self._current is None:

            self._current = currency.code

    # ------------------------------------------------------

    def set_current(self, code: str):

        if code not in self._currencies:

            raise ValueError(f"Currency '{code}' is not registered.")

        self._current = code

    # ------------------------------------------------------

    @property
    def current(self) -> Currency:

        return self._currencies[self._current]

    # ------------------------------------------------------

    def convert(

        self,

        value: float,

        from_code: str,

        to_code: str

    ) -> float:

        if from_code not in self._currencies:

            raise ValueError(from_code)

        if to_code not in self._currencies:

            raise ValueError(to_code)

        base = value / self._currencies[from_code].exchange_rate

        return base * self._currencies[to_code].exchange_rate

    # ------------------------------------------------------

    def format(

        self,

        value: float,

        code: str | None = None

    ) -> str:

        if code is None:

            code = self._current

        currency = self._currencies[code]

        return (
            f"{currency.symbol}"
            f"{value:,.{currency.decimal_places}f}"
        )

    # ------------------------------------------------------

    def list_currencies(self):

        return list(self._currencies.keys())