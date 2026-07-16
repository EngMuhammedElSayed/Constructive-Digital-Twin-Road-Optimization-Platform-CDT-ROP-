"""
writer.py
=========

Excel Writer Interface

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines the abstract interface used to export CDT-ROP
data into Excel workbooks.

This module contains no implementation using openpyxl,
xlsxwriter or pandas.

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List


class ExcelWriter(ABC):
    """
    Abstract interface for exporting CDT-ROP data to Excel.

    Concrete implementations are responsible for writing
    workbooks using the selected spreadsheet library.
    """

    # =====================================================
    # Workbook
    # =====================================================

    @abstractmethod
    def create_workbook(self) -> None:
        """
        Create a new workbook.
        """
        ...

    @abstractmethod
    def open_workbook(
        self,
        workbook: Path
    ) -> None:
        """
        Open an existing workbook.
        """
        ...

    @abstractmethod
    def save(
        self,
        destination: Path
    ) -> None:
        """
        Save workbook.
        """
        ...

    @abstractmethod
    def close(self) -> None:
        """
        Close workbook.
        """
        ...

    # =====================================================
    # Worksheet
    # =====================================================

    @abstractmethod
    def create_sheet(
        self,
        sheet_name: str
    ) -> None:
        """
        Create worksheet.
        """
        ...

    @abstractmethod
    def write_sheet(
        self,
        sheet_name: str,
        rows: List[Dict]
    ) -> None:
        """
        Write an entire worksheet.
        """
        ...

    @abstractmethod
    def write_row(
        self,
        sheet_name: str,
        row: Dict
    ) -> None:
        """
        Write one row.
        """
        ...

    @abstractmethod
    def write_cell(
        self,
        sheet_name: str,
        cell_reference: str,
        value: Any
    ) -> None:
        """
        Write one cell.
        """
        ...

    # =====================================================
    # Templates
    # =====================================================

    @abstractmethod
    def export_project_template(
        self,
        data: Any
    ) -> None:
        """
        Export Project template.
        """
        ...

    @abstractmethod
    def export_alignment_template(
        self,
        data: Any
    ) -> None:
        """
        Export Alignment template.
        """
        ...

    @abstractmethod
    def export_traffic_template(
        self,
        data: Any
    ) -> None:
        """
        Export Traffic template.
        """
        ...

    @abstractmethod
    def export_terrain_template(
        self,
        data: Any
    ) -> None:
        """
        Export Terrain template.
        """
        ...

    @abstractmethod
    def export_weather_template(
        self,
        data: Any
    ) -> None:
        """
        Export Weather template.
        """
        ...

    @abstractmethod
    def export_cost_template(
        self,
        data: Any
    ) -> None:
        """
        Export Cost template.
        """
        ...

    @abstractmethod
    def export_optimization_template(
        self,
        data: Any
    ) -> None:
        """
        Export Optimization template.
        """
        ...

    # =====================================================
    # Reports
    # =====================================================

    @abstractmethod
    def export_report(
        self,
        report: Dict
    ) -> None:
        """
        Export engineering report.
        """
        ...

    @abstractmethod
    def export_results(
        self,
        results: Dict
    ) -> None:
        """
        Export optimization results.
        """
        ...

    @abstractmethod
    def export_summary(
        self,
        summary: Dict
    ) -> None:
        """
        Export project summary.
        """
        ...