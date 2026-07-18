"""
simulation_settings.py
======================

Simulation Settings Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents simulation configuration used by the
Constructive Digital Twin.

This module contains simulation configuration only.

No simulation engine or execution logic is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class SimulationSettings:
    """
    Represents simulation settings for the Digital Twin.
    """

    # =====================================================
    # General
    # =====================================================

    enabled: bool = False

    simulation_name: str = ""

    simulation_type: str = "Design"

    # =====================================================
    # Simulation Modes
    # =====================================================

    design_simulation: bool = True

    traffic_simulation: bool = False

    earthwork_simulation: bool = False

    pavement_simulation: bool = False

    drainage_simulation: bool = False

    environmental_simulation: bool = False

    cost_simulation: bool = False

    carbon_emission_simulation: bool = False

    # =====================================================
    # Execution
    # =====================================================

    realtime: bool = False

    predictive: bool = False

    historical: bool = False

    iterations: int = 1

    timestep_seconds: float = 1.0

    # =====================================================
    # Performance
    # =====================================================

    enable_parallel_processing: bool = False

    maximum_workers: int = 1

    maximum_runtime_seconds: float = 3600.0

    # =====================================================
    # Output
    # =====================================================

    save_results: bool = True

    save_logs: bool = True

    export_reports: bool = True

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)