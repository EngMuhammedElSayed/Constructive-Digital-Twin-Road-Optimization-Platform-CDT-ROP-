"""
digital_twin_configuration.py
=============================

Digital Twin Configuration Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines the configuration of the Constructive Digital Twin.

This module stores configuration only.
No synchronization or simulation logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class DigitalTwinConfiguration:
    """
    Configuration of the Digital Twin.
    """

    # =====================================================
    # General
    # =====================================================

    twin_name: str = ""

    twin_type: str = "Constructive"

    enabled: bool = True

    version: str = "1.0"

    # =====================================================
    # Synchronization
    # =====================================================

    synchronization_enabled: bool = True

    synchronization_mode: str = "Manual"

    synchronization_interval_sec: int = 300

    automatic_reconnect: bool = True

    # =====================================================
    # Simulation
    # =====================================================

    simulation_enabled: bool = False

    realtime_simulation: bool = False

    historical_simulation: bool = False

    predictive_simulation: bool = False

    # =====================================================
    # Monitoring
    # =====================================================

    monitoring_enabled: bool = True

    logging_enabled: bool = True

    event_tracking_enabled: bool = True

    # =====================================================
    # Storage
    # =====================================================

    save_history: bool = True

    save_snapshots: bool = True

    snapshot_interval_sec: int = 3600

    # =====================================================
    # Security
    # =====================================================

    read_only: bool = False

    authentication_required: bool = False

    encryption_enabled: bool = False

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)