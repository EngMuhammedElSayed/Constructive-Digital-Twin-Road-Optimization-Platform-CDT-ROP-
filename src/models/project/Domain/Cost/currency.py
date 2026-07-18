"""
currency.py
===========

Currency Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents currency information used for project cost
estimation.

This module stores currency data only.

No exchange-rate retrieval or currency conversion logic
is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass(slots=True)
class Currency:
    """
    Represents a project currency.
    """

    # =====================================================
    # Currency Identity
    # =====================================================

    code: str = "EGP"

    name: str = "Egyptian Pound"

    symbol: str = "E£"

    # =====================================================
    # Exchange Information
    # =====================================================

    exchange_rate: float = 1.0

    base_currency: str = "EGP"

    exchange_rate_date: datetime | None = None

    # =====================================================
    # Formatting
    # =====================================================

    decimal_places: int = 2

    thousands_separator: str = ","

    decimal_separator: str = "."

    # =====================================================
    # Status
    # =====================================================

    active: bool = True

    remarks: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)