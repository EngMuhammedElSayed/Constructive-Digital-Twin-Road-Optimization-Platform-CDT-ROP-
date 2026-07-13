"""
Project Data Model

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

This module defines the root Project object.
The Project aggregates all engineering models used by the system.

Author:
Eng. Muhammed

Research:
MSc Research
Cairo University
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

# Geometry
from models.geometry.alignment import Alignment
from models.geometry.corridor import Corridor
from models.geometry.surface import Surface
from models.geometry.road_geometry import RoadGeometry

# Traffic
from models.traffic.traffic_data import TrafficData

# Cost
from models.cost.cost_parameters import CostParameters

# Optimization
from models.optimization.optimization_settings import OptimizationSettings

# Standards
from standards.design_criteria import DesignCriteria


@dataclass
class Project:
    """
    Root object representing a complete road project.

    Every engineering module inside the Constructive Digital Twin
    belongs to one Project.
    """

    # ============================================================
    # Project Information
    # ============================================================

    project_name: str

    project_code: str = ""

    description: str = ""

    client: str = ""

    designer: str = ""

    organization: str = ""

    country: str = "Egypt"

    city: str = ""

    coordinate_system: str = ""

    created_date: datetime = field(default_factory=datetime.now)

    last_modified: datetime = field(default_factory=datetime.now)

    # ============================================================
    # Geometry
    # ============================================================

    alignment: Optional[Alignment] = None

    corridor: Optional[Corridor] = None

    road_geometry: Optional[RoadGeometry] = None

    existing_surface: Optional[Surface] = None

    proposed_surface: Optional[Surface] = None

    # ============================================================
    # Traffic
    # ============================================================

    traffic_data: Optional[TrafficData] = None

    # ============================================================
    # Cost
    # ============================================================

    cost_parameters: Optional[CostParameters] = None

    # ============================================================
    # Design Standards
    # ============================================================

    design_criteria: Optional[DesignCriteria] = None

    # ============================================================
    # Optimization
    # ============================================================

    optimization_settings: Optional[OptimizationSettings] = None

    # ============================================================
    # Civil 3D
    # ============================================================

    civil3d_drawing: str = ""

    civil3d_version: str = ""

    # ============================================================
    # Digital Twin
    # ============================================================

    digital_twin_enabled: bool = True

    twin_last_update: Optional[datetime] = None

    # ============================================================
    # Status
    # ============================================================

    status: str = "Draft"
