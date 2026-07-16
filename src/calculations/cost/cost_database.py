"""
cost_database.py
================

Central Cost Database Manager

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 2.0.0
"""

from __future__ import annotations

from pathlib import Path
import csv
from typing import Dict


class CostDatabase:
    """
    Reads cost items from project CSV files.

    Expected CSV Format
    -------------------
    Category,Item,Unit,Unit Rate
    earthwork,Excavation,m3,8.50
    earthwork,Embankment,m3,6.30
    """

    def __init__(self):

        self._rates: Dict[str, Dict[str, float]] = {}

        self.currency = "Undefined"

    # =========================================================
    # Load CSV
    # =========================================================

    def load_csv(

        self,

        category: str,

        csv_file: str | Path

    ) -> None:

        csv_file = Path(csv_file)

        if not csv_file.exists():

            raise FileNotFoundError(csv_file)

        if category not in self._rates:

            self._rates[category] = {}

        with open(

            csv_file,

            newline="",

            encoding="utf-8-sig"

        ) as f:

            reader = csv.DictReader(f)

            for row in reader:

                item = row["Item"].strip()

                rate = row["Unit Rate"].strip()

                if rate == "":

                    rate = 0.0

                else:

                    rate = float(rate)

                self._rates[category][item] = rate

    # =========================================================
    # Get Rate
    # =========================================================

    def get_rate(

        self,

        category: str,

        item: str

    ) -> float:

        try:

            return self._rates[category][item]

        except KeyError:

            raise KeyError(

                f"Cost item '{item}' "

                f"was not found "

                f"in category '{category}'."

            )

    # =========================================================
    # Set Rate
    # =========================================================

    def set_rate(

        self,

        category: str,

        item: str,

        rate: float

    ):

        if category not in self._rates:

            self._rates[category] = {}

        self._rates[category][item] = float(rate)

    # =========================================================
    # Update Currency
    # =========================================================

    def set_currency(

        self,

        currency: str

    ):

        self.currency = currency

    # =========================================================
    # Information
    # =========================================================

    @property
    def categories(self):

        return list(self._rates.keys())

    def items(

        self,

        category: str

    ):

        return self._rates.get(category, {})

    def clear(self):

        self._rates.clear()

    def __len__(self):

        return sum(

            len(v)

            for v in self._rates.values()

        )

    def __repr__(self):

        return (

            f"<CostDatabase "

            f"categories={len(self._rates)} "

            f"items={len(self)}>"

        )