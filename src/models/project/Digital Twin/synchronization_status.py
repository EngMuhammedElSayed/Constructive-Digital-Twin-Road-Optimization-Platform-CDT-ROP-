"""
synchronization_status.py
=========================

Synchronization Status Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the current synchronization state of the
Constructive Digital Twin.

This module stores synchronization status only.

No synchronization logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict
from uuid import uuid4


@dataclass(slots=True)
class SynchronizationStatus:
    """
    Represents the current synchronization status.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    # =====================================================
    # Current State
    # =====================================================

    status: str = "NotStarted"

    running: bool = False

    progress_percent: float = 0.0

    # =====================================================
    # Timing
    # =====================================================

    started_at: datetime | None = None

    finished_at: datetime | None = None

    last_successful_sync: datetime | None = None

    duration_seconds: float = 0.0

    # =====================================================
    # Statistics
    # =====================================================

    synchronized_objects: int = 0

    skipped_objects: int = 0

    failed_objects: int = 0

    # =====================================================
    # Errors
    # =====================================================

    has_errors: bool = False

    error_message: str = ""

    warning_message: str = ""

    # =====================================================
    # Source
    # =====================================================

    source_name: str = ""

    destination_name: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)