"""
civil3d_config.py
=================

Autodesk Civil 3D Configuration

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


# ==========================================================
# Civil 3D Configuration
# ==========================================================

@dataclass(slots=True)
class Civil3DConfig:
    """
    Autodesk Civil 3D configuration.

    This file stores only configuration values.

    It DOES NOT communicate with Civil 3D.
    """

    # ------------------------------------------------------
    # Software
    # ------------------------------------------------------

    application_name: str = "Autodesk Civil 3D"

    autocad_version: str = "2025"

    civil3d_version: str = "2025"

    executable_path: str | None = None

    # ------------------------------------------------------
    # Project Units
    # ------------------------------------------------------

    drawing_units: str = "Meters"

    coordinate_system: str = "WGS84 / UTM"

    station_format: str = "0+000"

    landxml_version: str = "1.2"

    # ------------------------------------------------------
    # Import Options
    # ------------------------------------------------------

    import_alignments: bool = True

    import_profiles: bool = True

    import_corridors: bool = True

    import_surfaces: bool = True

    import_sample_lines: bool = True

    import_assemblies: bool = True

    # ------------------------------------------------------
    # Export Options
    # ------------------------------------------------------

    export_landxml: bool = True

    export_ifc: bool = False

    export_csv: bool = True

    export_json: bool = True

    export_shapefile: bool = False

    # ------------------------------------------------------
    # BIM
    # ------------------------------------------------------

    enable_bim_attributes: bool = True

    enable_cobie_export: bool = False

    preserve_object_ids: bool = True

    # ------------------------------------------------------
    # Temporary Workspace
    # ------------------------------------------------------

    working_directory: Path = Path("temp/civil3d")

    backup_directory: Path = Path("backup/civil3d")


# ==========================================================
# Default Configuration
# ==========================================================

CIVIL3D_CONFIG = Civil3DConfig()
