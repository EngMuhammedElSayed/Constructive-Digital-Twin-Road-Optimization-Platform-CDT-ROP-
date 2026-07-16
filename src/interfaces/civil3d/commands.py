"""
commands.py
===========

Civil 3D Command Interface

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class Civil3DCommands(ABC):
    """
    Abstract interface for Autodesk Civil 3D operations.

    This interface defines the operations that any
    Civil 3D implementation must provide.

    No Autodesk API code should be placed here.
    """

    # =====================================================
    # Project
    # =====================================================

    @abstractmethod
    def open_project(self, project_file: Path):

        """
        Open a Civil 3D project.
        """

        ...

    @abstractmethod
    def save_project(self):

        """
        Save current project.
        """

        ...

    @abstractmethod
    def close_project(self):

        """
        Close current project.
        """

        ...

    # =====================================================
    # Alignment
    # =====================================================

    @abstractmethod
    def import_alignment(self, file: Path):

        """
        Import alignment.
        """

        ...

    @abstractmethod
    def export_alignment(self, file: Path):

        """
        Export alignment.
        """

        ...

    # =====================================================
    # Surface
    # =====================================================

    @abstractmethod
    def import_surface(self, file: Path):

        ...

    @abstractmethod
    def export_surface(self, file: Path):

        ...

    # =====================================================
    # Corridor
    # =====================================================

    @abstractmethod
    def create_corridor(self):

        ...

    @abstractmethod
    def export_corridor(self, file: Path):

        ...

    # =====================================================
    # Profile
    # =====================================================

    @abstractmethod
    def import_profile(self, file: Path):

        ...

    @abstractmethod
    def export_profile(self, file: Path):

        ...

    # =====================================================
    # Sample Lines
    # =====================================================

    @abstractmethod
    def generate_sample_lines(self):

        ...

    # =====================================================
    # Earthwork
    # =====================================================

    @abstractmethod
    def compute_earthwork(self):

        ...

    # =====================================================
    # LandXML
    # =====================================================

    @abstractmethod
    def import_landxml(self, file: Path):

        ...

    @abstractmethod
    def export_landxml(self, file: Path):

        ...

    # =====================================================
    # Reports
    # =====================================================

    @abstractmethod
    def export_report(self, file: Path):

        ...

    # =====================================================
    # Synchronization
    # =====================================================

    @abstractmethod
    def synchronize(self):

        """
        Synchronize CDT-ROP with Civil 3D.
        """

        ...
