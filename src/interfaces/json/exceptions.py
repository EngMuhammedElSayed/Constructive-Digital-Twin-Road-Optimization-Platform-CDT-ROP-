"""
exceptions.py
=============

JSON Exceptions

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Custom exceptions used by the JSON interface.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations


# ==========================================================
# Base Exception
# ==========================================================

class JsonError(Exception):
    """
    Base exception for all JSON interface errors.
    """
    pass


# ==========================================================
# File Errors
# ==========================================================

class JsonFileNotFoundError(JsonError):
    """
    JSON file does not exist.
    """
    pass


class InvalidJsonFileError(JsonError):
    """
    Invalid or corrupted JSON file.
    """
    pass


class JsonPermissionError(JsonError):
    """
    Unable to access JSON file.
    """
    pass


# ==========================================================
# Schema Errors
# ==========================================================

class JsonSchemaError(JsonError):
    """
    JSON schema validation failed.
    """
    pass


class MissingKeyError(JsonSchemaError):
    """
    Required key is missing.
    """
    pass


class InvalidKeyError(JsonSchemaError):
    """
    Invalid key detected.
    """
    pass


class DuplicateKeyError(JsonSchemaError):
    """
    Duplicate key detected.
    """
    pass


# ==========================================================
# Value Errors
# ==========================================================

class InvalidValueError(JsonError):
    """
    Invalid JSON value.
    """
    pass


class InvalidDataTypeError(JsonError):
    """
    Invalid data type.
    """
    pass


class EmptyValueError(JsonError):
    """
    Required value is empty.
    """
    pass


# ==========================================================
# Mapping Errors
# ==========================================================

class JsonMappingError(JsonError):
    """
    Error while mapping JSON to domain models.
    """
    pass


# ==========================================================
# Validation Errors
# ==========================================================

class JsonValidationError(JsonError):
    """
    JSON validation failed.
    """
    pass


class VersionMismatchError(JsonValidationError):
    """
    Unsupported JSON version.
    """
    pass


class UnitValidationError(JsonValidationError):
    """
    Invalid engineering unit.
    """
    pass


# ==========================================================
# Import / Export Errors
# ==========================================================

class JsonImportError(JsonError):
    """
    Failed to import JSON data.
    """
    pass


class JsonExportError(JsonError):
    """
    Failed to export JSON data.
    """
    pass


# ==========================================================
# Configuration Errors
# ==========================================================

class JsonConfigurationError(JsonError):
    """
    JSON configuration error.
    """
    pass