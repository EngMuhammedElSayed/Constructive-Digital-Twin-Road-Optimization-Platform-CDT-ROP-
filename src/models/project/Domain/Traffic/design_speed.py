"""
design_speed.py
===============

Design Speed Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents roadway design speed information.

The design speed is a selected speed used to determine
the geometric design features of a roadway according to
recognized engineering standards.

This module stores design speed information only.

No roadway geometric calculations are implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class DesignSpeed:
    """
    Represents roadway design speed.
    """

    # =====================================================
    # Identity
    # =====================================================

    design_speed_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    # =====================================================
    # Speed
    # =====================================================

    design_speed_kmh: float = 0.0

    design_speed_mph: float = 0.0

    # =====================================================
    # Road Classification
    # =====================================================

    road_classification: str = ""
    # Freeway
    # Expressway
    # Arterial
    # Collector
    # Local Road

    terrain_type: str = ""
    # Level
    # Rolling
    # Mountainous

    area_type: str = ""
    # Urban
    # Rural

    # =====================================================
    # Governing Standard
    # =====================================================

    design_standard: str = ""
    # AASHTO
    # DMRB
    # RTA
    # MOT
    # Custom

    standard_version: str = ""

    # =====================================================
    # Design Status
    # =====================================================

    governing_speed: bool = True

    verified: bool = False

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)