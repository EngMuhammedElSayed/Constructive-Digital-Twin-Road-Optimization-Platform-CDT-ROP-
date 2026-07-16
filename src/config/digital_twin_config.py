"""
digital_twin_config.py
======================

Digital Twin Configuration

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


# ==========================================================
# Digital Twin Configuration
# ==========================================================

@dataclass(slots=True)
class DigitalTwinConfig:
    """
    Digital Twin system configuration.

    This file stores only configuration values.
    """

    # ------------------------------------------------------
    # General
    # ------------------------------------------------------

    enabled: bool = True

    twin_name: str = "Constructive Digital Twin"

    twin_version: str = "1.0"

    twin_type: str = "Constructive"

    # ------------------------------------------------------
    # Synchronization
    # ------------------------------------------------------

    auto_sync: bool = True

    sync_interval_seconds: int = 300

    incremental_update: bool = True

    keep_history: bool = True

    history_limit: int = 1000

    # ------------------------------------------------------
    # BIM Integration
    # ------------------------------------------------------

    enable_bim: bool = True

    bim_source: str = "Civil3D"

    enable_ifc: bool = True

    enable_cobie: bool = False

    # ------------------------------------------------------
    # GIS Integration
    # ------------------------------------------------------

    enable_gis: bool = True

    gis_format: str = "GeoJSON"

    coordinate_system: str = "WGS84"

    # ------------------------------------------------------
    # IoT Integration
    # ------------------------------------------------------

    enable_iot: bool = False

    sensor_update_interval: int = 60

    # ------------------------------------------------------
    # Database
    # ------------------------------------------------------

    enable_database: bool = True

    database_type: str = "SQLite"

    database_file: Path = Path("database/digital_twin.db")

    # ------------------------------------------------------
    # Cache
    # ------------------------------------------------------

    enable_cache: bool = True

    cache_directory: Path = Path("cache/digital_twin")

    cache_size_mb: int = 512

    # ------------------------------------------------------
    # Logging
    # ------------------------------------------------------

    enable_logging: bool = True

    log_changes: bool = True

    log_directory: Path = Path("logs/digital_twin")

    # ------------------------------------------------------
    # Export
    # ------------------------------------------------------

    enable_export: bool = True

    export_json: bool = True

    export_ifc: bool = True

    export_landxml: bool = True

    export_csv: bool = True


# ==========================================================
# Default Configuration
# ==========================================================

DIGITAL_TWIN_CONFIG = DigitalTwinConfig()
