"""
validator.py
============

Excel Validator Interface

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines the validation interface for Excel workbooks.

This module performs no file reading and no Excel library
operations. Concrete implementations belong to the
integration layer.

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List, Any


class ExcelValidator(ABC):
    """
    Abstract interface for validating Excel data.

    Implementations should validate workbook structure,
    worksheets, templates and engineering datasets.
    """

    # =====================================================
    # Workbook Validation
    # =====================================================

    @abstractmethod
    def validate_workbook(self) -> bool:
        """
        Validate workbook structure.
        """
        ...

    # =====================================================
    # Worksheet Validation
    # =====================================================

    @abstractmethod
    def validate_sheet(
        self,
        sheet_name: str
    ) -> bool:
        """
        Validate a worksheet.
        """
        ...

    # =====================================================
    # Template Validation
    # =====================================================

    @abstractmethod
    def validate_template(
        self,
        template_name: str
    ) -> bool:
        """
        Validate workbook against template.
        """
        ...

    # =====================================================
    # Header Validation
    # =====================================================

    @abstractmethod
    def validate_columns(
        self,
        sheet_name: str,
        required_columns: List[str]
    ) -> bool:
        """
        Validate worksheet columns.
        """
        ...

    # =====================================================
    # Required Fields
    # =====================================================

    @abstractmethod
    def validate_required_fields(
        self,
        sheet_name: str
    ) -> bool:
        """
        Validate required fields.
        """
        ...

    # =====================================================
    # Data Types
    # =====================================================

    @abstractmethod
    def validate_data_types(
        self,
        sheet_name: str
    ) -> bool:
        """
        Validate data types.
        """
        ...

    # =====================================================
    # Engineering Units
    # =====================================================

    @abstractmethod
    def validate_units(
        self,
        sheet_name: str
    ) -> bool:
        """
        Validate engineering units.
        """
        ...

    # =====================================================
    # Duplicate IDs
    # =====================================================

    @abstractmethod
    def validate_duplicates(
        self,
        sheet_name: str,
        id_column: str
    ) -> bool:
        """
        Validate duplicate identifiers.
        """
        ...

    # =====================================================
    # Complete Validation
    # =====================================================

    @abstractmethod
    def validate(self) -> Dict[str, Any]:
        """
        Execute full validation process.

        Returns
        -------
        Dict[str, Any]

        Example
        -------
        {
            "valid": True,
            "errors": [],
            "warnings": [],
            "checked_sheets": [
                "Project",
                "Alignment",
                "Traffic"
            ]
        }
        """
        ...