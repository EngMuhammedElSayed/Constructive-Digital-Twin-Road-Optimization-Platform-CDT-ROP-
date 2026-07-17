"""
schema.py
=========

LandXML Schema Definitions

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Centralized definitions for supported LandXML schemas.

This module does not perform XML validation.
Concrete schema validation belongs to the integration layer.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict


# ==========================================================
# Schema Model
# ==========================================================

@dataclass(frozen=True, slots=True)
class LandXMLSchema:
    """
    Represents a supported LandXML schema.
    """

    version: str

    namespace: str

    description: str

    xsd_file: str


# ==========================================================
# Supported Schemas
# ==========================================================

LANDXML_10 = LandXMLSchema(

    version="1.0",

    namespace="http://www.landxml.org/schema/LandXML-1.0",

    description="LandXML Version 1.0",

    xsd_file="LandXML-1.0.xsd",

)

LANDXML_11 = LandXMLSchema(

    version="1.1",

    namespace="http://www.landxml.org/schema/LandXML-1.1",

    description="LandXML Version 1.1",

    xsd_file="LandXML-1.1.xsd",

)

LANDXML_12 = LandXMLSchema(

    version="1.2",

    namespace="http://www.landxml.org/schema/LandXML-1.2",

    description="LandXML Version 1.2",

    xsd_file="LandXML-1.2.xsd",

)


# ==========================================================
# Registry
# ==========================================================

SUPPORTED_SCHEMAS: Dict[str, LandXMLSchema] = {

    "1.0": LANDXML_10,

    "1.1": LANDXML_11,

    "1.2": LANDXML_12,

}


DEFAULT_SCHEMA = LANDXML_12


# ==========================================================
# Helpers
# ==========================================================

def get_schema(version: str) -> LandXMLSchema:
    """
    Return the schema definition for a LandXML version.

    Parameters
    ----------
    version : str
        LandXML version.

    Returns
    -------
    LandXMLSchema
    """

    return SUPPORTED_SCHEMAS.get(version, DEFAULT_SCHEMA)


def is_supported(version: str) -> bool:
    """
    Check whether a LandXML version is supported.
    """

    return version in SUPPORTED_SCHEMAS


def get_xsd_path(
    version: str,
    schemas_directory: Path,
) -> Path:
    """
    Return the expected XSD file path.
    """

    schema = get_schema(version)

    return schemas_directory / schema.xsd_file