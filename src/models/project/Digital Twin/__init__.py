"""
Digital Twin Project Models

CDT-ROP
Constructive Digital Twin Road Optimization Platform

This package contains domain models related to the
Constructive Digital Twin.

The package contains data models only.

No synchronization, simulation, API, or business logic
should be implemented here.
"""

from .digital_twin import DigitalTwin
from .digital_twin_configuration import DigitalTwinConfiguration
from .synchronization_settings import SynchronizationSettings
from .synchronization_status import SynchronizationStatus
from .sensor_configuration import SensorConfiguration
from .data_source import DataSource
from .update_policy import UpdatePolicy
from .simulation_settings import SimulationSettings
from .version_control import VersionControl
from .twin_metadata import TwinMetadata

__all__ = [
    "DigitalTwin",
    "DigitalTwinConfiguration",
    "SynchronizationSettings",
    "SynchronizationStatus",
    "SensorConfiguration",
    "DataSource",
    "UpdatePolicy",
    "SimulationSettings",
    "VersionControl",
    "TwinMetadata",
]