"""
Geometry Domain Package

CDT-ROP
Constructive Digital Twin Road Optimization Platform

This package contains all geometry-related domain models
used throughout the CDT-ROP platform.

The models represent engineering entities only.

No engineering calculations, optimization algorithms,
or geometry processing logic are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from .alignment import Alignment
from .horizontal_alignment import HorizontalAlignment
from .vertical_alignment import VerticalAlignment

from .profile import Profile
from .profile_pvi import ProfilePVI

from .corridor import Corridor

from .cross_section import CrossSection
from .typical_section import TypicalSection

from .lane import Lane
from .shoulder import Shoulder
from .median import Median
from .curb import Curb
from .sidewalk import Sidewalk

from .surface import Surface
from .tin_surface import TinSurface
from .grid_surface import GridSurface

from .point import Point
from .vector import Vector
from .coordinate_system import CoordinateSystem

from .line import Line
from .arc import Arc
from .spiral import Spiral

from .geometry_extent import GeometryExtent
from .geometry_metadata import GeometryMetadata

__all__ = [
    "Alignment",
    "HorizontalAlignment",
    "VerticalAlignment",
    "Profile",
    "ProfilePVI",
    "Corridor",
    "CrossSection",
    "TypicalSection",
    "Lane",
    "Shoulder",
    "Median",
    "Curb",
    "Sidewalk",
    "Surface",
    "TinSurface",
    "GridSurface",
    "Point",
    "Vector",
    "CoordinateSystem",
    "Line",
    "Arc",
    "Spiral",
    "GeometryExtent",
    "GeometryMetadata",
]