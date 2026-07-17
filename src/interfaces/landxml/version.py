"""
version.py
==========

LandXML Version Definitions

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Centralized definitions for supported LandXML versions.

This module contains version metadata only.
Validation logic belongs to the validator implementation.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple


# ==========================================================
# Version Model
# ==========================================================

@dataclass(frozen=True, slots=True)
class LandXMLVersion:
    """
    Represents a LandXML specification version.
    """

    version: str

    namespace: str

    description: str

    supported: bool = True


# ==========================================================
# Supported Versions
# ==========================================================

LANDXML_10 = LandXMLVersion(
    version="1.0",
    namespace="http://www.landxml.org/schema/LandXML-1.0",
    description="LandXML Version 1.0",
)

LANDXML_11 = LandXMLVersion(
    version="1.1",
    namespace="http://www.landxml.org/schema/LandXML-1.1",
    description="LandXML Version 1.1",
)

LANDXML_12 = LandXMLVersion(
    version="1.2",
    namespace="http://www.landxml.org/schema/LandXML-1.2",
    description="LandXML Version 1.2",
)


# ==========================================================
# Registry
# ==========================================================

SUPPORTED_VERSIONS: Dict[str, LandXMLVersion] = {
    "1.0": LANDXML_10,
    "1.1": LANDXML_11,
    "1.2": LANDXML_12,
}

DEFAULT_VERSION = LANDXML_12


# ==========================================================
# Helper Functions
# ==========================================================

def get_version(version: str) -> LandXMLVersion:
    """
    Return a LandXML version definition.
    """

    return SUPPORTED_VERSIONS.get(version, DEFAULT_VERSION)


def is_supported(version: str) -> bool:
    """
    Check whether a LandXML version is supported.
    """

    return version in SUPPORTED_VERSIONS


def supported_versions() -> Tuple[str, ...]:
    """
    Return all supported version numbers.
    """

    return tuple(SUPPORTED_VERSIONS.keys())


def latest_version() -> LandXMLVersion:
    """
    Return the latest supported LandXML version.
    """

    return DEFAULT_VERSION