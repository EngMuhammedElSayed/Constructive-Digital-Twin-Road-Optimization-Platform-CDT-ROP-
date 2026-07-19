"""
peak_hour_factor.py
===================

Peak Hour Factor (PHF) Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents Peak Hour Factor (PHF) information used for
traffic engineering analysis.

Peak Hour Factor describes the variation of traffic flow
within the peak hour.

This module stores PHF data only.

No Highway Capacity Manual (HCM) calculations are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class PeakHourFactor:
    """
    Represents Peak Hour Factor (PHF).
    """

    # =====================================================
    # Identity
    # =====================================================

    phf_id: str = ""

    roadway_id: str = ""

    segment_id: str = ""

    # =====================================================
    # Traffic Volumes
    # =====================================================

    hourly_volume_veh_per_hr: float = 0.0

    peak_15_min_volume_veh: float = 0.0

    # =====================================================
    # Peak Hour Factor
    # =====================================================

    peak_hour_factor: float = 1.0

    # =====================================================
    # Analysis
    # =====================================================

    analysis_period_minutes: float = 60.0

    peak_interval_minutes: float = 15.0

    peak_type: str = ""
    # AM Peak
    # PM Peak
    # Daily Peak
    # Weekend Peak

    # =====================================================
    # References
    # =====================================================

    design_standard: str = ""

    hcm_edition: str = ""

    source: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    remarks: str = ""

    properties: Dict[str, str] = field(default_factory=dict)