"""
sensor_configuration.py
=======================

Sensor Configuration Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents sensor configuration used by the Constructive
Digital Twin.

This module stores sensor configuration only.

No hardware communication or IoT logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict
from uuid import uuid4


@dataclass(slots=True)
class SensorConfiguration:
    """
    Represents one Digital Twin sensor configuration.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""

    description: str = ""

    # =====================================================
    # Sensor Information
    # =====================================================

    sensor_type: str = ""

    manufacturer: str = ""

    model: str = ""

    serial_number: str = ""

    # =====================================================
    # Location
    # =====================================================

    station: float = 0.0

    offset: float = 0.0

    elevation: float = 0.0

    # =====================================================
    # Operation
    # =====================================================

    enabled: bool = True

    sampling_interval_sec: int = 60

    transmission_interval_sec: int = 60

    realtime_enabled: bool = True

    # =====================================================
    # Communication
    # =====================================================

    protocol: str = ""

    endpoint: str = ""

    # =====================================================
    # Status
    # =====================================================

    status: str = "Offline"

    health_status: str = "Unknown"

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)