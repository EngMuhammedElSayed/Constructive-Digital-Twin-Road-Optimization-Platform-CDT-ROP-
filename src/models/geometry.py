from dataclasses import dataclass

@dataclass
class RoadGeometry:
    """
    Stores geometric design variables.
    """

    radius: float
    grade: float
    lane_width: float
    shoulder_width: float
    median_width: float
    superelevation: float
