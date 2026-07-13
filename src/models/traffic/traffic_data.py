"""
Traffic Data Model

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

This module defines the traffic characteristics associated with a
roadway project. The class stores traffic input data only and does
not perform any traffic engineering calculations.

Author:
Eng. Muhammed

Research:
MSc Research
Cairo University
"""

from dataclasses import dataclass


@dataclass
class TrafficData:
    """
    Represents traffic information used by the roadway design,
    safety evaluation, capacity analysis, and optimization engine.
    """

    # ============================================================
    # General
    # ============================================================

    road_name: str = ""

    study_year: int = 2025

    design_year: int = 2045

    # ============================================================
    # Traffic Volumes
    # ============================================================

    AADT: float = 0.0                    # Average Annual Daily Traffic

    DHV: float = 0.0                     # Design Hour Volume

    peak_hour_volume: float = 0.0

    peak_hour_factor: float = 1.0

    directional_distribution: float = 0.50

    lane_distribution_factor: float = 1.00

    # ============================================================
    # Vehicle Composition
    # ============================================================

    heavy_vehicle_percentage: float = 0.0

    bus_percentage: float = 0.0

    truck_percentage: float = 0.0

    motorcycle_percentage: float = 0.0

    # ============================================================
    # Growth
    # ============================================================

    annual_growth_rate: float = 0.0

    growth_factor: float = 1.0

    # ============================================================
    # Capacity Analysis
    # ============================================================

    demand: float = 0.0

    capacity: float = 0.0

    volume_to_capacity_ratio: float = 0.0

    target_LOS: str = "C"

    # ============================================================
    # Speed
    # ============================================================

    posted_speed: float = 90.0

    operating_speed: float = 90.0

    design_speed: float = 90.0

    free_flow_speed: float = 0.0

    # ============================================================
    # Future Digital Twin
    # ============================================================

    real_time_data: bool = False

    traffic_sensor_source: str = ""

    update_interval_seconds: int = 60
