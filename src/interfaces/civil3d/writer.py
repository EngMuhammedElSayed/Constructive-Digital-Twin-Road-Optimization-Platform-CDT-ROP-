"""
writer.py
=========

Civil 3D Writer Interface

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class Civil3DWriter(ABC):
    """
    Abstract interface for writing CDT-ROP data
    to Autodesk Civil 3D.

    This interface defines what any Civil 3D writer
    implementation must support.

    It contains no Autodesk API code.
    """

    # =====================================================
    # Project
    # =====================================================

    @abstractmethod
    def write_project(
        self,
        project: Any,
        destination: Path
    ) -> None:
        """
        Write project data.
        """
        ...

    # =====================================================
    # Alignment
    # =====================================================

    @abstractmethod
    def write_alignment(
        self,
        alignment: Any,
        destination: Path
    ) -> None:
        """
        Export alignment.
        """
        ...

    # =====================================================
    # Profile
    # =====================================================

    @abstractmethod
    def write_profile(
        self,
        profile: Any,
        destination: Path
    ) -> None:
        """
        Export profile.
        """
        ...

    # =====================================================
    # Surface
    # =====================================================

    @abstractmethod
    def write_surface(
        self,
        surface: Any,
        destination: Path
    ) -> None:
        """
        Export surface.
        """
        ...

    # =====================================================
    # Corridor
    # =====================================================

    @abstractmethod
    def write_corridor(
        self,
        corridor: Any,
        destination: Path
    ) -> None:
        """
        Export corridor.
        """
        ...

    # =====================================================
    # Sample Lines
    # =====================================================

    @abstractmethod
    def write_sample_lines(
        self,
        sample_lines: Any,
        destination: Path
    ) -> None:
        """
        Export sample lines.
        """
        ...

    # =====================================================
    # Cross Sections
    # =====================================================

    @abstractmethod
    def write_cross_sections(
        self,
        sections: Any,
        destination: Path
    ) -> None:
        """
        Export cross sections.
        """
        ...

    # =====================================================
    # Pipe Network
    # =====================================================

    @abstractmethod
    def write_pipe_network(
        self,
        network: Any,
        destination: Path
    ) -> None:
        """
        Export drainage network.
        """
        ...

    # =====================================================
    # LandXML
    # =====================================================

    @abstractmethod
    def write_landxml(
        self,
        project: Any,
        destination: Path
    ) -> None:
        """
        Export LandXML.
        """
        ...

    # =====================================================
    # Reports
    # =====================================================

    @abstractmethod
    def write_report(
        self,
        report: Any,
        destination: Path
    ) -> None:
        """
        Export Civil 3D report.
        """
        ...

    # =====================================================
    # Synchronization
    # =====================================================

    @abstractmethod
    def synchronize(
        self,
        project: Any
    ) -> None:
        """
        Synchronize CDT-ROP data with Civil 3D.
        """
        ...
