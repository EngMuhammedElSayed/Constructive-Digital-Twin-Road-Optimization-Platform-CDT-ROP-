"""
cost_parameters.py
==================

Cost Parameters Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines the engineering cost parameters used by the
cost calculation modules.

This module contains data only.
No cost calculations are performed here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


# ==========================================================
# Earthwork Costs
# ==========================================================

@dataclass(slots=True)
class EarthworkCostParameters:

    excavation_cost_per_m3: float = 0.0

    embankment_cost_per_m3: float = 0.0

    disposal_cost_per_m3: float = 0.0


# ==========================================================
# Pavement Costs
# ==========================================================

@dataclass(slots=True)
class PavementCostParameters:

    subgrade_cost_per_m2: float = 0.0

    subbase_cost_per_m2: float = 0.0

    base_cost_per_m2: float = 0.0

    asphalt_cost_per_m2: float = 0.0


# ==========================================================
# Structures
# ==========================================================

@dataclass(slots=True)
class StructureCostParameters:

    bridge_cost_per_m: float = 0.0

    culvert_cost_per_unit: float = 0.0

    retaining_wall_cost_per_m2: float = 0.0


# ==========================================================
# Drainage
# ==========================================================

@dataclass(slots=True)
class DrainageCostParameters:

    pipe_cost_per_m: float = 0.0

    manhole_cost_per_unit: float = 0.0

    inlet_cost_per_unit: float = 0.0


# ==========================================================
# Utilities
# ==========================================================

@dataclass(slots=True)
class UtilityCostParameters:

    relocation_cost_per_m: float = 0.0

    protection_cost_per_m: float = 0.0


# ==========================================================
# Traffic
# ==========================================================

@dataclass(slots=True)
class TrafficCostParameters:

    marking_cost_per_m2: float = 0.0

    sign_cost_per_unit: float = 0.0

    signal_cost_per_unit: float = 0.0

    lighting_cost_per_unit: float = 0.0


# ==========================================================
# Maintenance
# ==========================================================

@dataclass(slots=True)
class MaintenanceCostParameters:

    annual_maintenance_cost: float = 0.0

    rehabilitation_cost: float = 0.0

    overlay_cost_per_m2: float = 0.0


# ==========================================================
# Environmental
# ==========================================================

@dataclass(slots=True)
class EnvironmentalCostParameters:

    carbon_cost_per_ton: float = 0.0

    mitigation_cost: float = 0.0


# ==========================================================
# Cost Parameters
# ==========================================================

@dataclass(slots=True)
class CostParameters:
    """
    Complete cost parameter model.
    """

    currency: str = "EGP"

    earthwork: EarthworkCostParameters = field(
        default_factory=EarthworkCostParameters
    )

    pavement: PavementCostParameters = field(
        default_factory=PavementCostParameters
    )

    structures: StructureCostParameters = field(
        default_factory=StructureCostParameters
    )

    drainage: DrainageCostParameters = field(
        default_factory=DrainageCostParameters
    )

    utilities: UtilityCostParameters = field(
        default_factory=UtilityCostParameters
    )

    traffic: TrafficCostParameters = field(
        default_factory=TrafficCostParameters
    )

    maintenance: MaintenanceCostParameters = field(
        default_factory=MaintenanceCostParameters
    )

    environmental: EnvironmentalCostParameters = field(
        default_factory=EnvironmentalCostParameters
    )

    additional_costs: Dict[str, float] = field(
        default_factory=dict
    )