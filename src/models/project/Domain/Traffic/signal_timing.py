"""
signal_timing.py
================

Traffic Signal Timing Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents traffic signal timing information.

This module stores signal timing parameters only.

No signal optimization algorithms, Webster equations,
or HCM signal timing calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class SignalTiming:
    """
    Represents traffic signal timing settings.
    """

    # =====================================================
    # Identity
    # =====================================================

    signal_timing_id: str = ""

    signal_controller_id: str = ""

    intersection_id: str = ""

    # =====================================================
    # Cycle
    # =====================================================

    cycle_length_sec: float = 0.0

    offset_sec: float = 0.0

    lost_time_sec: float = 0.0

    intergreen_time_sec: float = 0.0

    # =====================================================
    # Phase Times
    # =====================================================

    total_green_time_sec: float = 0.0

    total_yellow_time_sec: float = 0.0

    total_all_red_time_sec: float = 0.0

    pedestrian_clearance_time_sec: float = 0.0

    # =====================================================
    # Operation
    # =====================================================

    control_mode: str = ""
    # Fixed Time
    # Actuated
    # Semi-Actuated
    # Adaptive

    coordination_enabled: bool = False

    transit_priority_enabled: bool = False

    emergency_preemption_enabled: bool = False

    # =====================================================
    # Analysis
    # =====================================================

    analysis_period: str = ""
    # AM Peak
    # PM Peak
    # Off Peak
    # Daily

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