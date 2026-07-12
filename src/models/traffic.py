from dataclasses import dataclass

@dataclass
class TrafficData:
    """
    Stores traffic characteristics.
    """

    demand: float
    capacity: float
    peak_hour_factor: float
    heavy_vehicle_percentage: float
