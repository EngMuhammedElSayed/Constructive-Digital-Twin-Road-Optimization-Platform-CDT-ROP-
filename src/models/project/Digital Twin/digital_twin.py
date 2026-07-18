"""
digital_twin.py
===============

Digital Twin Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the Constructive Digital Twin.

This module aggregates all Digital Twin components.

No synchronization, simulation, API integration,
or business logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List
from uuid import uuid4

from .digital_twin_configuration import DigitalTwinConfiguration
from .data_source import DataSource


@dataclass(slots=True)
class DigitalTwin:
    """
    Represents the Constructive Digital Twin.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""

    description: str = ""

    # =====================================================
    # General
    # =====================================================

    enabled: bool = True

    version: str = "1.0.0"

    lifecycle_stage: str = "Design"

    # =====================================================
    # Configuration
    # =====================================================

    configuration: DigitalTwinConfiguration = field(
        default_factory=DigitalTwinConfiguration
    )

    # =====================================================
    # Data Sources
    # =====================================================

    data_sources: List[DataSource] = field(
        default_factory=list
    )

    # =====================================================
    # Synchronization
    # =====================================================

    synchronization_enabled: bool = True

    last_synchronization: datetime | None = None

    synchronization_status: str = "NotStarted"

    # =====================================================
    # Simulation
    # =====================================================

    simulation_enabled: bool = False

    realtime_enabled: bool = False

    prediction_enabled: bool = False

    # =====================================================
    # Monitoring
    # =====================================================

    monitoring_enabled: bool = True

    health_status: str = "Healthy"

    # =====================================================
    # Metadata
    # =====================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    properties: Dict[str, str] = field(default_factory=dict)

    # =====================================================
    # Helper Properties
    # =====================================================

    @property
    def data_source_count(self) -> int:
        return len(self.data_sources)

    @property
    def is_synchronized(self) -> bool:
        return self.synchronization_status == "Synchronized"

    @property
    def is_operational(self) -> bool:
        return self.enabled and self.health_status == "Healthy"