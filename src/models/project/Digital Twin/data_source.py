"""
data_source.py
==============

Digital Twin Data Source Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a data source connected to the Constructive
Digital Twin.

This module stores metadata only.

No file reading, database access, or API calls are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict
from uuid import uuid4


@dataclass(slots=True)
class DataSource:
    """
    Represents one Digital Twin data source.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""

    description: str = ""

    # =====================================================
    # Source Information
    # =====================================================

    source_type: str = ""

    provider: str = ""

    version: str = ""

    path: str = ""

    # =====================================================
    # Connection
    # =====================================================

    enabled: bool = True

    read_only: bool = True

    auto_refresh: bool = False

    refresh_interval_sec: int = 60

    # =====================================================
    # Status
    # =====================================================

    status: str = "Disconnected"

    last_update: datetime | None = None

    last_successful_sync: datetime | None = None

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)