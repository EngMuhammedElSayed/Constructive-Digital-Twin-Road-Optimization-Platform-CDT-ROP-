"""
Project Data Model

This module defines the root project object used throughout the
Constructive Digital Twin Road Optimization Platform (CDT-ROP).

Author:
Eng. Muhammed

Research:
MSc Research - Cairo University
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Project:
    """
    Represents a complete road optimization project.

    This is the root object that contains all project information.
    Other engineering models such as Alignment, Surface,
    Corridor, TrafficData, and CostParameters will be linked here.
    """

    # -------------------------------------------------
    # Basic Project Information
    # -------------------------------------------------

    project_name: str
    project_code: str

    client: str
    designer: str

    country: str
    design_standard: str

    coordinate_system: str

    description: str = ""

    created_date: datetime = datetime.now()

    # -------------------------------------------------
    # Engineering Models
    # -------------------------------------------------

    surface: Optional[object] = None

    alignment: Optional[object] = None

    corridor: Optional[object] = None

    road_geometry: Optional[object] = None

    traffic_data: Optional[object] = None

    cost_parameters: Optional[object] = None

    optimization_settings: Optional[object] = None
