"""
===============================================================================
Highway Capacity Manual (HCM)
===============================================================================

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

Description
-----------
This module provides engineering reference values based on the
Highway Capacity Manual (HCM).

The module contains ONLY traffic engineering reference values.

No engineering calculations should be implemented here.

Supported Future Modules
------------------------

- Capacity Analysis
- Level of Service (LOS)
- Delay Analysis
- Queue Analysis
- Freeway Analysis
- Multilane Highway Analysis
- Two-Lane Highway Analysis
- Urban Street Analysis
- Roundabout Analysis
- Signalized Intersection Analysis
- Unsignalized Intersection Analysis

Author:
Eng. Muhammed

Research:
MSc Research
Cairo University
===============================================================================
"""

from dataclasses import dataclass
from typing import Dict


# =============================================================================
# Freeway Standards
# =============================================================================

@dataclass(frozen=True)
class FreewayCriteria:
    """
    Freeway operational criteria.
    """

    base_lane_capacity: float = 2200.0      # pcphpl

    default_free_flow_speed: float = 120.0  # km/h

    maximum_vc_ratio: float = 0.90


# =============================================================================
# Multilane Highway
# =============================================================================

@dataclass(frozen=True)
class MultilaneCriteria:
    """
    Multilane highway criteria.
    """

    base_lane_capacity: float = 2000.0

    default_free_flow_speed: float = 100.0

    maximum_vc_ratio: float = 0.90


# =============================================================================
# Two-Lane Highway
# =============================================================================

@dataclass(frozen=True)
class TwoLaneCriteria:
    """
    Two-lane highway criteria.
    """

    base_directional_capacity: float = 1700.0

    default_speed: float = 90.0


# =============================================================================
# Urban Street
# =============================================================================

@dataclass(frozen=True)
class UrbanStreetCriteria:
    """
    Urban street criteria.
    """

    default_speed: float = 60.0

    saturation_flow_rate: float = 1900.0


# =============================================================================
# Signalized Intersections
# =============================================================================

@dataclass(frozen=True)
class SignalizedIntersectionCriteria:
    """
    Signalized intersection criteria.
    """

    base_saturation_flow: float = 1900.0

    startup_lost_time: float = 2.0

    clearance_lost_time: float = 2.0


# =============================================================================
# Heavy Vehicles
# =============================================================================

@dataclass(frozen=True)
class HeavyVehicleCriteria:
    """
    Heavy vehicle adjustment factors.
    """

    default_truck_pce: float = 2.0

    default_bus_pce: float = 2.0

    default_rv_pce: float = 1.2


# =============================================================================
# Peak Hour
# =============================================================================

@dataclass(frozen=True)
class PeakHourCriteria:
    """
    Peak hour factors.
    """

    default_phf: float = 0.92


# =============================================================================
# Level of Service
# =============================================================================

@dataclass(frozen=True)
class LOSCriteria:
    """
    Generic Level of Service limits.
    """

    A: float = 0.35

    B: float = 0.54

    C: float = 0.77

    D: float = 0.93

    E: float = 1.00

    F: float = 9.99


# =============================================================================
# Main HCM Standard
# =============================================================================

class HCM:
    """
    Central access point for HCM reference values.
    """

    freeway = FreewayCriteria()

    multilane = MultilaneCriteria()

    two_lane = TwoLaneCriteria()

    urban = UrbanStreetCriteria()

    signalized = SignalizedIntersectionCriteria()

    heavy_vehicle = HeavyVehicleCriteria()

    peak_hour = PeakHourCriteria()

    los = LOSCriteria()

    @staticmethod
    def determine_los(vc_ratio: float) -> str:
        """
        Determine Level of Service from V/C ratio.

        Parameters
        ----------
        vc_ratio : float

        Returns
        -------
        str
        """

        if vc_ratio <= HCM.los.A:
            return "A"

        elif vc_ratio <= HCM.los.B:
            return "B"

        elif vc_ratio <= HCM.los.C:
            return "C"

        elif vc_ratio <= HCM.los.D:
            return "D"

        elif vc_ratio <= HCM.los.E:
            return "E"

        else:
            return "F"

    @staticmethod
    def summary() -> Dict:
        """
        Returns all HCM criteria.
        """

        return {

            "freeway": HCM.freeway,

            "multilane": HCM.multilane,

            "two_lane": HCM.two_lane,

            "urban": HCM.urban,

            "signalized": HCM.signalized,

            "heavy_vehicle": HCM.heavy_vehicle,

            "peak_hour": HCM.peak_hour,

            "los": HCM.los,
        }
