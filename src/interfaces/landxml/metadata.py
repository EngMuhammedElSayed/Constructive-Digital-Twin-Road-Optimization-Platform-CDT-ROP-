"""
metadata.py
===========

LandXML Metadata Models

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines metadata models used by the LandXML interface.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


# ==========================================================
# Application
# ==========================================================

@dataclass(slots=True)
class ApplicationMetadata:
    """
    Information about the software that generated
    the LandXML file.
    """

    name: str = ""
    manufacturer: str = ""
    version: str = ""


# ==========================================================
# Project
# ==========================================================

@dataclass(slots=True)
class ProjectMetadata:
    """
    Project information.
    """

    name: str = ""
    description: str = ""


# ==========================================================
# Units
# ==========================================================

@dataclass(slots=True)
class UnitsMetadata:
    """
    Engineering units.
    """

    linear: str = "meter"
    area: str = "squareMeter"
    volume: str = "cubicMeter"
    temperature: str = "celsius"
    pressure: str = "pascal"


# ==========================================================
# Coordinate System
# ==========================================================

@dataclass(slots=True)
class CoordinateSystemMetadata:
    """
    Coordinate reference system.
    """

    name: str = ""
    epsg: Optional[int] = None
    datum: str = ""
    projection: str = ""


# ==========================================================
# Author
# ==========================================================

@dataclass(slots=True)
class AuthorMetadata:
    """
    Author information.
    """

    name: str = ""
    organization: str = ""
    email: str = ""


# ==========================================================
# LandXML Metadata
# ==========================================================

@dataclass(slots=True)
class LandXMLMetadata:
    """
    Complete metadata model for a LandXML document.
    """

    version: str = "1.2"

    date: str = ""

    language: str = "en"

    application: ApplicationMetadata = ApplicationMetadata()

    project: ProjectMetadata = ProjectMetadata()

    units: UnitsMetadata = UnitsMetadata()

    coordinate_system: CoordinateSystemMetadata = CoordinateSystemMetadata()

    author: AuthorMetadata = AuthorMetadata()