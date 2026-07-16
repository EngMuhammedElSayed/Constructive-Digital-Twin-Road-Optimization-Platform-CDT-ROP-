"""
reader.py
=========

Civil 3D Reader Interface

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class Civil3DReader(ABC):
    """
    Abstract interface for reading Civil 3D data.

    This interface defines the reading operations
    required by CDT-ROP.

    It does NOT contain Autodesk API code.
    """

    # =====================================================
    # Project
    # =====================================================

    @abstractmethod
    def read_project(self, project_file: Path) -> Any:
        """
        Read a Civil 3D project.
        """
        ...

    # =====================================================
    # Alignment
    # =====================================================

    @abstractmethod
    def read_alignment(self, source: Path) -> Any:
        """
        Read alignment data.
        """
        ...

    # =====================================================
    # Profile
    # =====================================================

    @abstractmethod
    def read_profile(self, source: Path) -> Any:
        """
        Read profile data.
        """
        ...

    # =====================================================
    # Surface
    # =====================================================

    @abstractmethod
    def read_surface(self, source: Path) -> Any:
        """
        Read surface data.
        """
        ...

    # =====================================================
    # Corridor
    # =====================================================

    @abstractmethod
    def read_corridor(self, source: Path) -> Any:
        """
        Read corridor data.
        """
        ...

    # =====================================================
    # Sample Lines
    # =====================================================

    @abstractmethod
    def read_sample_lines(self, source: Path) -> Any:
        """
        Read sample line data.
        """
        ...

    # =====================================================
    # Cross Sections
    # =====================================================

    @abstractmethod
    def read_cross_sections(self, source: Path) -> Any:
        """
        Read cross section data.
        """
        ...

    # =====================================================
    # Pipe Network
    # =====================================================

    @abstractmethod
    def read_pipe_network(self, source: Path) -> Any:
        """
        Read drainage network data.
        """
        ...

    # =====================================================
    # LandXML
    # =====================================================

    @abstractmethod
    def read_landxml(self, source: Path) -> Any:
        """
        Read LandXML file.
        """
        ...

    # =====================================================
    # Metadata
    # =====================================================

    @abstractmethod
    def read_metadata(self, source: Path) -> dict:
        """
        Read project metadata.
        """
        ...
