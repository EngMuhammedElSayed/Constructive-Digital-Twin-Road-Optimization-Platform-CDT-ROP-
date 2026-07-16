"""
CDT-ROP Cost Calculation Package
================================

This package contains all cost calculation engines used by the
Constructive Digital Twin Road Optimization Platform.

Available Modules
-----------------
- Earthwork Cost
- Cost Database

Author:
    CDT-ROP Development Team

Version:
    1.0.0
"""

# ==========================================================
# Earthwork Cost Engine
# ==========================================================

from .earthwork_cost import (
    EarthworkQuantities,
    CostFactors,
    EarthworkCostCalculator,
)

# ==========================================================
# Cost Database
# ==========================================================

from .cost_database import CostDatabase

# ==========================================================
# Package Metadata
# ==========================================================

__version__ = "1.0.0"

__author__ = "CDT-ROP Development Team"

# ==========================================================
# Public API
# ==========================================================

__all__ = [

    # Database
    "CostDatabase",

    # Earthwork
    "EarthworkQuantities",
    "CostFactors",
    "EarthworkCostCalculator",

]