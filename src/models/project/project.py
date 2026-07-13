"""
Project Model

Root object of the CDT-ROP platform.
"""

from dataclasses import dataclass, field

from models.project.project_metadata import ProjectMetadata
from models.project.project_settings import ProjectSettings

from models.geometry.road_geometry import RoadGeometry
from models.geometry.surface import Surface
from models.geometry.corridor import Corridor
from models.geometry.alignment import Alignment
from models.geometry.profile import Profile
from models.geometry.design_criteria import DesignCriteria

from models.traffic.traffic_data import TrafficData

from models.cost.cost_parameters import CostParameters

from models.optimization.optimization_settings import OptimizationSettings


@dataclass
class Project:
    """
    Root project object.

    Every module in the software receives a Project object.
    """

    metadata: ProjectMetadata = field(default_factory=ProjectMetadata)

    settings: ProjectSettings = field(default_factory=ProjectSettings)

    geometry: RoadGeometry = field(default_factory=RoadGeometry)

    alignment: Alignment = field(default_factory=Alignment)

    profile: Profile = field(default_factory=Profile)

    surface: Surface = field(default_factory=Surface)

    corridor: Corridor = field(default_factory=Corridor)

    design_criteria: DesignCriteria = field(default_factory=DesignCriteria)

    traffic: TrafficData = field(default_factory=TrafficData)

    cost: CostParameters = field(default_factory=CostParameters)

    optimization: OptimizationSettings = field(default_factory=OptimizationSettings)
