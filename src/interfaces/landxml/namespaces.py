"""
namespaces.py
=============

LandXML Namespaces

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Centralized XML namespace definitions used throughout
the LandXML interface.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations


# ==========================================================
# Official LandXML Namespaces
# ==========================================================

LANDXML_10 = "http://www.landxml.org/schema/LandXML-1.0"

LANDXML_11 = "http://www.landxml.org/schema/LandXML-1.1"

LANDXML_12 = "http://www.landxml.org/schema/LandXML-1.2"


# ==========================================================
# Default Namespace
# ==========================================================

DEFAULT_NAMESPACE = LANDXML_12


# ==========================================================
# Namespace Dictionary
# ==========================================================

NAMESPACES = {

    "lx10": LANDXML_10,

    "lx11": LANDXML_11,

    "lx12": LANDXML_12,

    "lx": DEFAULT_NAMESPACE,

}


# ==========================================================
# Supported Versions
# ==========================================================

SUPPORTED_NAMESPACES = {

    LANDXML_10,

    LANDXML_11,

    LANDXML_12,

}


# ==========================================================
# Utility
# ==========================================================

def get_namespace(version: str) -> str:
    """
    Return the namespace URI for a LandXML version.

    Parameters
    ----------
    version : str

        LandXML version.

    Returns
    -------
    str
    """

    mapping = {

        "1.0": LANDXML_10,

        "1.1": LANDXML_11,

        "1.2": LANDXML_12,

    }

    return mapping.get(version, DEFAULT_NAMESPACE)