"""
design_vehicle.py
=================

Design Vehicle Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the governing design vehicle used during
roadway geometric design.

The design vehicle defines the minimum geometric
requirements used for roadway layout according to
recognized highway design standards.

This module stores vehicle characteristics only.

No swept path analysis, off-tracking calculations,
or vehicle simulation algorithms are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class DesignVehicle:
    """
    Represents a roadway design vehicle.
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
    # P
    # SU
    # BUS
    # WB-12
    # WB-15
    # WB-19
    # WB-20
    # WB-30
    # Custom

    vehicle_category: str = ""
    # Passenger Car
    # Bus
    # Single Unit Truck
    # Semi-Trailer
    # Multi-Trailer

    # =====================================================
    # Dimensions
    # =====================================================

    overall_length_m: float = 0.0

    overall_width_m: float = 0.0

    overall_height_m: float = 0.0

    wheelbase_m: float = 0.0

    front_overhang_m: float = 0.0

    rear_overhang_m: float = 0.0

    # =====================================================
    # Steering Characteristics
    # =====================================================

    minimum_turning_radius_m: float = 0.0

    inside_turning_radius_m: float = 0.0

    outside_turning_radius_m: float = 0.0

    maximum_offtracking_m: float = 0.0

    # =====================================================
    # Axles
    # =====================================================

    axle_count: int = 2

    trailer_count: int = 0

    # =====================================================
    # Usage
    # =====================================================

    governing_design_vehicle: bool = True

    design_standard: str = ""

    standard_version: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)