"""
signal_phase.py
===============

Traffic Signal Phase Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents a single traffic signal phase.

This module stores signal phase information only.

No signal timing optimization, Webster equations,
or HCM signal analysis are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class SignalPhase:
    """
    Represents a traffic signal phase.
    """

    # =====================================================
    # Identity
    # =====================================================

    phase_id: str = ""

    signal_controller_id: str = ""

    intersection_id: str = ""

    phase_number: int = 1

    # =====================================================
    # Phase Information
    # =====================================================

    phase_name: str = ""

    movement_type: str = ""
    # Through
    # Left Turn
    # Right Turn
    # Pedestrian
    # Protected Left
    # Permissive Left

    direction: str = ""
    # Northbound
    # Southbound
    # Eastbound
    # Westbound

    # =====================================================
    # Timing
    # =====================================================

    green_time_sec: float = 0.0

    yellow_time_sec: float = 0.0

    all_red_time_sec: float = 0.0

    pedestrian_time_sec: float = 0.0

    minimum_green_sec: float = 0.0

    maximum_green_sec: float = 0.0

    # =====================================================
    # Operation
    # =====================================================

    protected_phase: bool = False

    pedestrian_crossing: bool = False

    flashing_green: bool = False

    # =====================================================
    # References
    # =====================================================

    design_standard: str = ""

    source: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)