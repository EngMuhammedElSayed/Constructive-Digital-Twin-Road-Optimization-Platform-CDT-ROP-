"""
traffic_data.py
===============

Traffic Data Aggregate Root

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the complete traffic dataset associated with
a roadway project or roadway segment.

This class acts as the aggregate root of the Traffic
Domain and references all traffic-related entities.

No traffic calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict

from .traffic_composition import TrafficComposition
from .origin_destination import OriginDestination
from .peak_hour_factor import PeakHourFactor
from .level_of_service import LevelOfService
from .capacity import Capacity
from .delay import Delay
from .queue import Queue
from .operating_speed import OperatingSpeed
from .design_speed import DesignSpeed
from .speed_limit import SpeedLimit
from .growth_factor import GrowthFactor
from .esal import ESAL
from .safety_indicator import SafetyIndicator


@dataclass(slots=True)
class TrafficData:
    """
    Aggregate root for all traffic-related information.
    """

    # =====================================================
    # Identity
    # =====================================================

    traffic_data_id: str = ""

    project_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    scenario_name: str = ""

    # =====================================================
    # Analysis
    # =====================================================

    analysis_year: int = 0

    design_year: int = 0

    source: str = ""

    # =====================================================
    # Traffic Domain Objects
    # =====================================================

    traffic_composition: TrafficComposition | None = None

    operating_speed: OperatingSpeed | None = None

    design_speed: DesignSpeed | None = None

    speed_limit: SpeedLimit | None = None

    peak_hour_factor: PeakHourFactor | None = None

    growth_factor: GrowthFactor | None = None

    esal: ESAL | None = None

    capacity: Capacity | None = None

    delay: Delay | None = None

    queue: Queue | None = None

    level_of_service: LevelOfService | None = None

    safety_indicator: SafetyIndicator | None = None

    origin_destination: List[OriginDestination] = field(default_factory=list)

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)