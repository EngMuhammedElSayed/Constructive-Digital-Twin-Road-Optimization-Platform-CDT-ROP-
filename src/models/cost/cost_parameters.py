"""
Cost Parameters Data Model

This module defines all economic parameters used by the
Constructive Digital Twin Road Optimization Platform (CDT-ROP).

The class stores only cost-related inputs.
No engineering calculations are implemented here.
"""

from dataclasses import dataclass


@dataclass
class CostParameters:
    """
    Stores all cost parameters used by the optimization engine.

    These values are supplied by the user or imported from
    Civil 3D, Excel, JSON, or external databases.
    """

    # -------------------------------------------------
    # General Information
    # -------------------------------------------------

    currency: str = "USD"

    analysis_period: int = 20

    discount_rate: float = 0.05

    contingency_factor: float = 0.10

    # -------------------------------------------------
    # Earthwork Cost
    # -------------------------------------------------

    cut_cost_per_m3: float = 0.0

    fill_cost_per_m3: float = 0.0

    unsuitable_material_cost_per_m3: float = 0.0

    borrow_material_cost_per_m3: float = 0.0

    haul_cost_per_m3_km: float = 0.0

    # -------------------------------------------------
    # Pavement Cost
    # -------------------------------------------------

    pavement_cost_per_m2: float = 0.0

    asphalt_cost_per_ton: float = 0.0

    base_course_cost_per_m3: float = 0.0

    subbase_cost_per_m3: float = 0.0

    shoulder_cost_per_m2: float = 0.0

    # -------------------------------------------------
    # Right-of-Way (ROW)
    # -------------------------------------------------

    row_cost_per_m2: float = 0.0

    land_acquisition_cost_per_m2: float = 0.0

    compensation_cost: float = 0.0

    # -------------------------------------------------
    # Future Extensions
    # -------------------------------------------------

    maintenance_cost_per_year: float = 0.0

    operation_cost_per_year: float = 0.0
