"""
demand_forecast.py
==================

Traffic Demand Forecast Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents forecasted traffic demand information for a
roadway facility.

This model stores forecast data only.

No forecasting algorithms, statistical models, or
machine learning methods are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class DemandForecast:
    """
    Represents forecasted traffic demand.
    """

    # =====================================================
    # Identity
    # =====================================================

    forecast_id: str = ""

    project_id: str = ""

    roadway_id: str = ""

    scenario_id: str = ""

    # =====================================================
    # Forecast Information
    # =====================================================

    base_year: int = 0

    forecast_year: int = 0

    forecast_horizon_years: int = 0

    # =====================================================
    # Traffic Demand
    # =====================================================

    base_aadt: float = 0.0

    forecast_aadt: float = 0.0

    peak_hour_volume: float = 0.0

    design_hour_volume: float = 0.0

    # =====================================================
    # Growth
    # =====================================================

    annual_growth_rate_percent: float = 0.0

    cumulative_growth_percent: float = 0.0

    # =====================================================
    # Vehicle Composition
    # =====================================================

    passenger_car_percentage: float = 0.0

    heavy_vehicle_percentage: float = 0.0

    bus_percentage: float = 0.0

    motorcycle_percentage: float = 0.0

    # =====================================================
    # Forecast Method
    # =====================================================

    forecast_method: str = ""
    # Historical Trend
    # Growth Factor
    # Regression
    # Four-Step Model
    # Machine Learning
    # User Defined

    # =====================================================
    # References
    # =====================================================

    source: str = ""

    design_standard: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)