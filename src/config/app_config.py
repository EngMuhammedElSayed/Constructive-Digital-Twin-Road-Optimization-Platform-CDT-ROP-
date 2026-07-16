"""
app_config.py
=============

Application Configuration

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


# ==========================================================
# Paths
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

DATASETS_DIR = ROOT_DIR / "datasets"

RESOURCES_DIR = ROOT_DIR / "resources"

SRC_DIR = ROOT_DIR / "src"

OUTPUT_DIR = ROOT_DIR / "output"

LOG_DIR = ROOT_DIR / "logs"

CACHE_DIR = ROOT_DIR / "cache"

TEMP_DIR = ROOT_DIR / "temp"


# ==========================================================
# Application Configuration
# ==========================================================

@dataclass(slots=True)
class AppConfig:

    # ------------------------------------------------------
    # General
    # ------------------------------------------------------

    application_name: str = "CDT-ROP"

    application_version: str = "3.0.0"

    organization: str = "CDT-ROP Team"

    # ------------------------------------------------------
    # Design Standard
    # ------------------------------------------------------

    design_standard: str = "AASHTO"

    country: str = "Egypt"

    language: str = "en"

    currency: str = "EGP"

    # ------------------------------------------------------
    # Units
    # ------------------------------------------------------

    length_unit: str = "m"

    area_unit: str = "m²"

    volume_unit: str = "m³"

    speed_unit: str = "km/h"

    # ------------------------------------------------------
    # Performance
    # ------------------------------------------------------

    max_threads: int = 8

    enable_cache: bool = True

    debug: bool = False

    # ------------------------------------------------------
    # Optimization
    # ------------------------------------------------------

    optimization_algorithm: str = "NSGA-II"

    random_seed: int = 42

    # ------------------------------------------------------
    # Paths
    # ------------------------------------------------------

    root_directory: Path = ROOT_DIR

    datasets_directory: Path = DATASETS_DIR

    resources_directory: Path = RESOURCES_DIR

    output_directory: Path = OUTPUT_DIR

    log_directory: Path = LOG_DIR

    cache_directory: Path = CACHE_DIR

    temp_directory: Path = TEMP_DIR


# ==========================================================
# Default Configuration
# ==========================================================

APP_CONFIG = AppConfig()
