"""
civil3d.py
==========

Civil 3D I/O Interface

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines the abstract interface used by the platform to
exchange data with Autodesk Civil 3D.

This module contains no Autodesk API implementation.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict


class Civil3DIO(ABC):
    """
    Abstract interface for Civil 3D input/output.
    """

    # =====================================================
    # Project
    # =====================================================

    @abstractmethod
    def open_project(self, project_path: Path) -> None:
        """
        Open a Civil 3D project.
        """
        ...

    @abstractmethod
    def save_project(self) -> None:
        """
        Save the current Civil 3D project.
        """
        ...

    @abstractmethod
    def close_project(self) -> None:
        """
        Close the current project.
        """
        ...

    # =====================================================
    # Import
    # =====================================================

    @abstractmethod
    def import_alignment(self) -> Dict[str, Any]:
        """
        Import alignment data.
        """
        ...

    @abstractmethod
    def import_surface(self) -> Dict[str, Any]:
        """
        Import surface data.
        """
        ...

    @abstractmethod
    def import_corridor(self) -> Dict[str, Any]:
        """
        Import corridor data.
        """
        ...

    @abstractmethod
    def import_assembly(self) -> Dict[str, Any]:
        """
        Import assembly data.
        """
        ...

    # =====================================================
    # Export
    # =====================================================

    @abstractmethod
    def export_alignment(self, data: Dict[str, Any]) -> None:
        """
        Export alignment.
        """
        ...

    @abstractmethod
    def export_surface(self, data: Dict[str, Any]) -> None:
        """
        Export surface.
        """
        ...

    @abstractmethod
    def export_corridor(self, data: Dict[str, Any]) -> None:
        """
        Export corridor.
        """
        ...

    @abstractmethod
    def export_results(self, results: Dict[str, Any]) -> None:
        """
        Export optimization results to Civil 3D.
        """
        ...
