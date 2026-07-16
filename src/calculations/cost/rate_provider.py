"""
rate_provider.py
================

Rate Provider Abstraction

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 2.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .cost_database import CostDatabase


# ==========================================================
# Abstract Interface
# ==========================================================

class RateProvider(ABC):
    """
    Base interface for all unit-rate providers.

    Different implementations may read rates from:

    - CSV
    - Excel
    - SQL Database
    - REST API
    - BIM Database
    - Digital Twin
    """

    @abstractmethod
    def get_rate(
        self,
        category: str,
        item: str
    ) -> float:
        pass


# ==========================================================
# Cost Database Provider
# ==========================================================

class CostDatabaseProvider(RateProvider):
    """
    Uses CostDatabase as the source of unit rates.
    """

    def __init__(
        self,
        database: CostDatabase
    ):

        self.database = database

    def get_rate(
        self,
        category: str,
        item: str
    ) -> float:

        return self.database.get_rate(
            category,
            item
        )