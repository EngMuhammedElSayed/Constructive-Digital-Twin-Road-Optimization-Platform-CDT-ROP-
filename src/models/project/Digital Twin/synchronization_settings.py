"""
synchronization_settings.py
===========================

Synchronization Settings Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents synchronization settings for the
Constructive Digital Twin.

This module contains synchronization configuration only.

No synchronization logic or communication with external
systems is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class SynchronizationSettings:
    """
    Represents Digital Twin synchronization settings.
    """

    # =====================================================
    # General
    # =====================================================

    enabled: bool = True

    mode: str = "Manual"

    automatic_reconnect: bool = True

    # =====================================================
    # Timing
    # =====================================================

    synchronization_interval_seconds: int = 300

    timeout_seconds: int = 120

    retry_attempts: int = 3

    retry_delay_seconds: int = 30

    # =====================================================
    # Data Synchronization
    # =====================================================

    synchronize_geometry: bool = True

    synchronize_surfaces: bool = True

    synchronize_alignments: bool = True

    synchronize_profiles: bool = True

    synchronize_corridors: bool = True

    synchronize_cross_sections: bool = True

    synchronize_cost_data: bool = True

    synchronize_traffic_data: bool = True

    synchronize_environmental_data: bool = True

    # =====================================================
    # Conflict Resolution
    # =====================================================

    overwrite_existing_data: bool = False

    keep_history: bool = True

    validate_before_import: bool = True

    # =====================================================
    # Monitoring
    # =====================================================

    log_synchronization: bool = True

    notify_on_failure: bool = True

    notify_on_success: bool = False

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)