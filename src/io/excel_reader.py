"""
excel_reader.py
===============

Excel Reader Interface

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines the abstract interface used to read engineering
data from Microsoft Excel workbooks.

This module contains no Excel library implementation.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List


class ExcelReader(ABC):
    """
    Abstract interface for reading Excel workbooks.
    """

    # =====================================================
    # Workbook
    # =====================================================

    @abstractmethod
    def open(self, workbook_path: Path) -> None:
        """
        Open an Excel workbook.
        """
        ...

    @abstractmethod
    def close(self) -> None:
        """
        Close the workbook.
        """
        ...

    # =====================================================
    # Worksheets
    # =====================================================

    @abstractmethod
    def sheet_names(self) -> List[str]:
        """
        Return all worksheet names.
        """
        ...

    @abstractmethod
    def read_sheet(
        self,
        sheet_name: str
    ) -> List[Dict[str, Any]]:
        """
        Read an entire worksheet.
        """
        ...

    # =====================================================
    # Cells
    # =====================================================

    @abstractmethod
    def read_cell(
        self,
        sheet_name: str,
        cell: str
    ) -> Any:
        """
        Read a single cell.
        """
        ...

    @abstractmethod
    def read_range(
        self,
        sheet_name: str,
        cell_range: str
    ) -> List[List[Any]]:
        """
        Read a range of cells.
        """
        ...

    # =====================================================
    # Tables
    # =====================================================

    @abstractmethod
    def read_table(
        self,
        sheet_name: str,
        table_name: str
    ) -> List[Dict[str, Any]]:
        """
        Read an Excel table.
        """
        ...

    # =====================================================
    # Metadata
    # =====================================================

    @abstractmethod
    def workbook_metadata(self) -> Dict[str, Any]:
        """
        Return workbook metadata.
        """
        ...
