"""
defaults.py
===========

Global Default Values

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from pathlib import Path


# ==========================================================
# Application
# ==========================================================

APP_NAME = "CDT-ROP"

APP_VERSION = "3.0.0"

ORGANIZATION = "CDT-ROP Team"


# ==========================================================
# Localization
# ==========================================================

DEFAULT_LANGUAGE = "en"

DEFAULT_COUNTRY = "Egypt"

DEFAULT_CURRENCY = "EGP"

DEFAULT_TIMEZONE = "Africa/Cairo"


# ==========================================================
# Units
# ==========================================================

LENGTH_UNIT = "m"

AREA_UNIT = "m²"

VOLUME_UNIT = "m³"

SPEED_UNIT = "km/h"

ANGLE_UNIT = "degree"

MASS_UNIT = "ton"

TEMPERATURE_UNIT = "°C"


# ==========================================================
# Coordinate System
# ==========================================================

DEFAULT_COORDINATE_SYSTEM = "WGS84"

DEFAULT_STATION_FORMAT = "0+000"


# ==========================================================
# BIM
# ==========================================================

DEFAULT_LOD = 300

DEFAULT_COBIE = False

DEFAULT_IFC_VERSION = "IFC4"


# ==========================================================
# GIS
# ==========================================================

DEFAULT_LANDXML_VERSION = "1.2"

DEFAULT_EPSG = 4326


# ==========================================================
# Optimization
# ==========================================================

DEFAULT_OPTIMIZATION_ALGORITHM = "NSGA-II"

DEFAULT_RANDOM_SEED = 42

DEFAULT_MAX_ITERATIONS = 200

DEFAULT_POPULATION_SIZE = 100


# ==========================================================
# Performance
# ==========================================================

DEFAULT_MAX_THREADS = 8

ENABLE_CACHE = True

ENABLE_LOGGING = True

DEBUG_MODE = False


# ==========================================================
# Reports
# ==========================================================

DEFAULT_REPORT_LANGUAGE = "en"

DEFAULT_REPORT_FORMAT = "pdf"


# ==========================================================
# Directories
# ==========================================================

OUTPUT_FOLDER = Path("output")

TEMP_FOLDER = Path("temp")

CACHE_FOLDER = Path("cache")

LOG_FOLDER = Path("logs")
