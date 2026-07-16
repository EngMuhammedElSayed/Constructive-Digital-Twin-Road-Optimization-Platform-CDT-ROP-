"""
reader.py
=========

Excel Reader Interface

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines the abstract interface used to read Excel
workbooks and worksheets.

No openpyxl or pandas code should be placed here.

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List


class ExcelReader(ABC):
    """
    Abstract interface for reading Excel files.

    Implementations are responsible for reading Excel
    workbooks and converting them into generic Python
    structures suitable for mapping to CDT-ROP models.
    """

    # =====================================================
    # Workbook
    # =====================================================

    @abstractmethod
    def open_workbook(
        self,
        workbook: Path
    ) -> None:
        """
        Open an Excel workbook.
        """
        ...

    @abstractmethod
    def close_workbook(self) -> None:
        """
        Close the current workbook.
        """
        ...

    # =====================================================
    # Worksheet
    # =====================================================

    @abstractmethod
    def list_sheets(self) -> List[str]:
        """
        Return workbook sheet names.
        """
        ...

    @abstractmethod
    def read_sheet(
        self,
        sheet_name: str
    ) -> List[Dict]:
        """
        Read an entire worksheet.

        Returns
        -------
        List[Dict]
            One dictionary per row.
        """
        ...

    @abstractmethod
    def read_row(
        self,
        sheet_name: str,
        row_number: int
    ) -> Dict:
        """
        Read one worksheet row.
        """
        ...

    @abstractmethod
    def read_column(
        self,
        sheet_name: str,
        column_name: str
    ) -> List[Any]:
        """
        Read one worksheet column.
        """
        ...

    @abstractmethod
    def read_cell(
        self,
        sheet_name: str,
        cell_reference: str
    ) -> Any:
        """
        Read one Excel cell.
        """
        ...

    # =====================================================
    # Templates
    # =====================================================

    @abstractmethod
    def read_project_template(self):
        """
        Read project_template.xlsx
        """
        ...

    @abstractmethod
    def read_alignment_template(self):
        """
        Read alignment_template.xlsx
        """
        ...

    @abstractmethod
    def read_traffic_template(self):
        """
        Read traffic_template.xlsx
        """
        ...

    @abstractmethod
    def read_terrain_template(self):
        """
        Read terrain_template.xlsx
        """
        ...

    @abstractmethod
    def read_weather_template(self):
        """
        Read weather_template.xlsx
        """
        ...

    @abstractmethod
    def read_cost_template(self):
        """
        Read cost_template.xlsx
        """
        ...

    @abstractmethod
    def read_optimization_template(self):
        """
        Read optimization_template.xlsx
        """
        ...

    # =====================================================
    # Metadata
    # =====================================================

    @abstractmethod
    def workbook_metadata(self) -> Dict:
        """
        Return workbook metadata.
        """
        ...