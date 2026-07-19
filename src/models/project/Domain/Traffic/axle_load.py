"""
axle_load.py
============

Axle Load Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents an axle load associated with a vehicle.

This model stores axle loading information used in
traffic engineering and pavement design.

No ESAL calculations or pavement design algorithms are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class AxleLoad:
    """
    Represents a vehicle axle load.
    """

    # =====================================================
    # Identity
    # =====================================================

    axle_load_id: str = ""

    vehicle_class_id: str = ""

    # =====================================================
    # Axle Information
    # =====================================================

    axle_number: int = 1

    axle_type: str = ""
    # Single
    # Tandem
    # Tridem
    # Quad

    axle_configuration: str = ""

    # =====================================================
    # Load Information
    # =====================================================

    axle_load_kN: float = 0.0

    axle_load_ton: float = 0.0

    axle_load_lb: float = 0.0

    # =====================================================
    # Geometry
    # =====================================================

    axle_spacing_m: float = 0.0

    tire_count: int = 2

    tire_pressure_kPa: float = 0.0

    # =====================================================
    # Traffic
    # =====================================================

    repetitions: int = 0

    traffic_percentage: float = 0.0

    # =====================================================
    # References
    # =====================================================

    standard_reference: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)