"""
exceptions.py
=============

LandXML Exceptions

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Custom exceptions used by the LandXML interface.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations


# ==========================================================
# Base Exception
# ==========================================================

class LandXMLError(Exception):
    """
    Base exception for all LandXML interface errors.
    """
    pass


# ==========================================================
# File Errors
# ==========================================================

class LandXMLFileNotFoundError(LandXMLError):
    """
    LandXML file does not exist.
    """
    pass


class InvalidLandXMLFileError(LandXMLError):
    """
    Invalid or corrupted LandXML file.
    """
    pass


class LandXMLPermissionError(LandXMLError):
    """
    Unable to access LandXML file.
    """
    pass


# ==========================================================
# XML Structure Errors
# ==========================================================

class InvalidXMLStructureError(LandXMLError):
    """
    Invalid XML structure.
    """
    pass


class MissingElementError(LandXMLError):
    """
    Required XML element is missing.
    """
    pass


class InvalidAttributeError(LandXMLError):
    """
    Invalid XML attribute.
    """
    pass


# ==========================================================
# Schema Errors
# ==========================================================

class LandXMLSchemaError(LandXMLError):
    """
    LandXML schema validation failed.
    """
    pass


class UnsupportedVersionError(LandXMLError):
    """
    Unsupported LandXML version.
    """
    pass


class NamespaceError(LandXMLError):
    """
    Invalid XML namespace.
    """
    pass


# ==========================================================
# Geometry Errors
# ==========================================================

class AlignmentError(LandXMLError):
    """
    Invalid alignment definition.
    """
    pass


class ProfileError(LandXMLError):
    """
    Invalid profile definition.
    """
    pass


class SurfaceError(LandXMLError):
    """
    Invalid surface definition.
    """
    pass


class CorridorError(LandXMLError):
    """
    Invalid corridor definition.
    """
    pass


class CogoPointError(LandXMLError):
    """
    Invalid COGO point.
    """
    pass


# ==========================================================
# Units
# ==========================================================

class UnitValidationError(LandXMLError):
    """
    Invalid engineering units.
    """
    pass


class CoordinateSystemError(LandXMLError):
    """
    Invalid coordinate system.
    """
    pass


# ==========================================================
# Mapping
# ==========================================================

class LandXMLMappingError(LandXMLError):
    """
    Error while mapping LandXML objects
    to CDT-ROP domain models.
    """
    pass


# ==========================================================
# Import / Export
# ==========================================================

class LandXMLImportError(LandXMLError):
    """
    Failed to import LandXML file.
    """
    pass


class LandXMLExportError(LandXMLError):
    """
    Failed to export LandXML file.
    """
    pass


# ==========================================================
# Validation
# ==========================================================

class LandXMLValidationError(LandXMLError):
    """
    LandXML validation failed.
    """
    pass


# ==========================================================
# Metadata
# ==========================================================

class MetadataError(LandXMLError):
    """
    Invalid LandXML metadata.
    """
    pass