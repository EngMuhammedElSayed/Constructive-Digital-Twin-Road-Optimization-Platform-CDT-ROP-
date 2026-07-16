"""
exceptions.py
=============

Excel Exceptions

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Custom exceptions used by the Excel interface.

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations


# ==========================================================
# Base Exception
# ==========================================================

class ExcelError(Exception):
    """
    Base exception for all Excel interface errors.
    """

    pass


# ==========================================================
# File Errors
# ==========================================================

class ExcelFileNotFoundError(ExcelError):
    """
    Excel file does not exist.
    """

    pass


class InvalidExcelFileError(ExcelError):
    """
    Unsupported or corrupted Excel file.
    """

    pass


class ExcelPermissionError(ExcelError):
    """
    Unable to access Excel file.
    """

    pass


# ==========================================================
# Worksheet Errors
# ==========================================================

class WorksheetNotFoundError(ExcelError):
    """
    Required worksheet is missing.
    """

    pass


class DuplicateWorksheetError(ExcelError):
    """
    Duplicate worksheet detected.
    """

    pass


class InvalidWorksheetError(ExcelError):
    """
    Worksheet structure is invalid.
    """

    pass


# ==========================================================
# Column Errors
# ==========================================================

class MissingColumnError(ExcelError):
    """
    Required column is missing.
    """

    pass


class DuplicateColumnError(ExcelError):
    """
    Duplicate column detected.
    """

    pass


class InvalidColumnError(ExcelError):
    """
    Invalid column definition.
    """

    pass


# ==========================================================
# Cell Errors
# ==========================================================

class InvalidCellValueError(ExcelError):
    """
    Cell value is invalid.
    """

    pass


class EmptyRequiredCellError(ExcelError):
    """
    Required cell is empty.
    """

    pass


class InvalidDataTypeError(ExcelError):
    """
    Cell data type is invalid.
    """

    pass


# ==========================================================
# Template Errors
# ==========================================================

class TemplateNotFoundError(ExcelError):
    """
    Excel template cannot be found.
    """

    pass


class TemplateMismatchError(ExcelError):
    """
    Workbook does not match expected template.
    """

    pass


class TemplateVersionError(ExcelError):
    """
    Unsupported template version.
    """

    pass


# ==========================================================
# Mapping Errors
# ==========================================================

class MappingError(ExcelError):
    """
    Error during Excel-to-model mapping.
    """

    pass


class ImportMappingError(ExcelError):
    """
    Invalid import_mapping.json configuration.
    """

    pass


# ==========================================================
# Validation Errors
# ==========================================================

class ValidationError(ExcelError):
    """
    Excel validation failed.
    """

    pass


class UnitValidationError(ValidationError):
    """
    Invalid engineering unit.
    """

    pass


class RequiredFieldError(ValidationError):
    """
    Required field is missing.
    """

    pass


class DuplicateIDError(ValidationError):
    """
    Duplicate identifier detected.
    """

    pass


# ==========================================================
# Import / Export Errors
# ==========================================================

class ImportError(ExcelError):
    """
    Failed to import Excel data.
    """

    pass


class ExportError(ExcelError):
    """
    Failed to export Excel data.
    """

    pass


# ==========================================================
# Configuration Errors
# ==========================================================

class ConfigurationError(ExcelError):
    """
    Excel configuration error.
    """

    pass