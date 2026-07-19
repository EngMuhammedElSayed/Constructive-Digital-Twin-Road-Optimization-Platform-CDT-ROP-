"""
check_vehicle.py
================

Check Vehicle Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a roadway check vehicle used to verify that
the proposed roadway geometry accommodates vehicle
movements safely.

A check vehicle is not necessarily the governing design
vehicle.

This module stores vehicle characteristics only.

No swept path analysis or vehicle simulation is
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class CheckVehicle:
    """
    Represents a roadway check vehicle.
    """

    # =====================================================
    # Identity
    # =====================================================

    vehicle_id: str = ""

    name: str = ""

    description: str = ""

    # =====================================================
    # Classification
    # =====================================================

    vehicle_code: str = ""
    # SU
    # BUS
    # WB-12
    # WB-15
    # WB-19
    # WB-20
    # Emergency
    # Custom

    vehicle_type: str = ""
    # Passenger Car
    # Bus
    # Single Unit Truck
    # Semi Trailer
    # Fire Truck
    # Service Vehicle

    # =====================================================
    # Dimensions
    # =====================================================

    overall_length_m: float = 0.0

    overall_width_m: float = 0.0

    overall_height_m: float = 0.0

    wheelbase_m: float = 0.0

    front_overhang_m: float = 0.0

    rear_overhang_m: float = 0.0

    minimum_turning_radius_m: float = 0.0

    # =====================================================
    # Usage
    # =====================================================

    governing_vehicle: bool = False

    check_only: bool = True

    # =====================================================
    # References
    # =====================================================

    design_standard: str = ""

    source: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)