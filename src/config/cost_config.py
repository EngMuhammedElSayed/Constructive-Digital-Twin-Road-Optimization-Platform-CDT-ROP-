"""
cost_config.py
==============

Cost System Configuration

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


# ==========================================================
# Cost Configuration
# ==========================================================

@dataclass(slots=True)
class CostConfig:
    """
    Cost calculation configuration.

    This file contains only system settings.

    No unit prices or project costs are stored here.
    """

    # ------------------------------------------------------
    # Currency
    # ------------------------------------------------------

    default_currency: str = "EGP"

    enable_currency_conversion: bool = True

    exchange_rate_file: Path = Path(
        "datasets/cost/exchange_rates.csv"
    )

    # ------------------------------------------------------
    # Cost Database
    # ------------------------------------------------------

    cost_dataset_directory: Path = Path(
        "datasets/cost"
    )

    country_directory: str = "egypt"

    template_directory: Path = Path(
        "datasets/cost/templates"
    )

    # ------------------------------------------------------
    # Supported Sources
    # ------------------------------------------------------

    allow_excel: bool = True

    allow_csv: bool = True

    allow_json: bool = True

    allow_database: bool = True

    # ------------------------------------------------------
    # Cost Modules
    # ------------------------------------------------------

    enable_earthwork: bool = True

    enable_pavement: bool = True

    enable_bridge: bool = True

    enable_drainage: bool = True

    enable_traffic: bool = True

    enable_utility: bool = True

    enable_environmental: bool = True

    enable_land_acquisition: bool = True

    enable_maintenance: bool = True

    enable_lifecycle: bool = True

    # ------------------------------------------------------
    # Reporting
    # ------------------------------------------------------

    generate_summary: bool = True

    generate_detailed_report: bool = True

    export_excel: bool = True

    export_pdf: bool = True

    export_json: bool = True

    # ------------------------------------------------------
    # Validation
    # ------------------------------------------------------

    validate_before_calculation: bool = True

    stop_on_validation_error: bool = True

    # ------------------------------------------------------
    # Optimization
    # ------------------------------------------------------

    use_parallel_processing: bool = True

    cache_cost_database: bool = True


# ==========================================================
# Default Configuration
# ==========================================================

COST_CONFIG = CostConfig()
