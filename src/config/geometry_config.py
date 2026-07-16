"""
geometry_config.py
==================

Geometry Engine Configuration

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


# ==========================================================
# Geometry Configuration
# ==========================================================

@dataclass(slots=True)
class GeometryConfig:
    """
    Geometry engine configuration.

    NOTE:
    This file contains ONLY configuration settings.

    Design criteria (SSD, Radius, Superelevation,
    Grades, etc.) are supplied by the active
    Standards Provider (AASHTO, Egypt, Saudi, UAE...).
    """

    # ------------------------------------------------------
    # Units
    # ------------------------------------------------------

    length_unit: str = "m"

    station_unit: str = "m"

    angle_unit: str = "degree"

    slope_unit: str = "percent"

    speed_unit: str = "km/h"

    # ------------------------------------------------------
    # Alignment
    # ------------------------------------------------------

    enable_horizontal_alignment: bool = True

    enable_vertical_alignment: bool = True

    enable_station_equations: bool = True

    enable_spirals: bool = True

    # ------------------------------------------------------
    # Cross Section
    # ------------------------------------------------------

    enable_cross_sections: bool = True

    enable_corridor_model: bool = True

    enable_daylight_lines: bool = True

    # ------------------------------------------------------
    # Earthwork
    # ------------------------------------------------------

    enable_cut_fill: bool = True

    enable_mass_haul: bool = True

    # ------------------------------------------------------
    # Geometry Calculations
    # ------------------------------------------------------

    calculate_ssd: bool = True

    calculate_psd: bool = True

    calculate_hso: bool = True

    calculate_superelevation: bool = True

    calculate_curve_radius: bool = True

    calculate_vertical_curves: bool = True

    calculate_cross_slope: bool = True

    # ------------------------------------------------------
    # Precision
    # ------------------------------------------------------

    coordinate_precision: int = 4

    station_precision: int = 3

    elevation_precision: int = 3

    angle_precision: int = 6

    # ------------------------------------------------------
    # Import / Export
    # ------------------------------------------------------

    allow_landxml: bool = True

    allow_ifc: bool = True

    allow_csv: bool = True

    allow_json: bool = True

    # ------------------------------------------------------
    # Reports
    # ------------------------------------------------------

    generate_geometry_report: bool = True

    export_alignment_tables: bool = True

    export_cross_sections: bool = True

    # ------------------------------------------------------
    # Working Directories
    # ------------------------------------------------------

    geometry_cache_directory: Path = Path(
        "cache/geometry"
    )

    report_directory: Path = Path(
        "output/reports/geometry"
    )


# ==========================================================
# Default Configuration
# ==========================================================

GEOMETRY_CONFIG = GeometryConfig()
