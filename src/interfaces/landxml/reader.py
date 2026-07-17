"""
reader.py
=========

LandXML Reader Interface

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines the abstract interface for reading LandXML files.

This module contains no XML parsing implementation.
Concrete implementations belong to the integration layer.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List


class LandXMLReader(ABC):
    """
    Abstract interface for reading LandXML documents.
    """

    # =====================================================
    # File
    # =====================================================

    @abstractmethod
    def open(
        self,
        file_path: Path
    ) -> None:
        """
        Open a LandXML document.
        """
        ...

    @abstractmethod
    def close(self) -> None:
        """
        Close the current document.
        """
        ...

    # =====================================================
    # General
    # =====================================================

    @abstractmethod
    def read_document(self) -> Dict[str, Any]:
        """
        Read the complete LandXML document.
        """
        ...

    @abstractmethod
    def read_metadata(self) -> Dict[str, Any]:
        """
        Read LandXML metadata.
        """
        ...

    @abstractmethod
    def read_units(self) -> Dict[str, Any]:
        """
        Read engineering units.
        """
        ...

    @abstractmethod
    def read_coordinate_system(self) -> Dict[str, Any]:
        """
        Read coordinate reference system.
        """
        ...

    # =====================================================
    # Geometry
    # =====================================================

    @abstractmethod
    def read_alignments(self) -> List[Dict[str, Any]]:
        """
        Read horizontal alignments.
        """
        ...

    @abstractmethod
    def read_profiles(self) -> List[Dict[str, Any]]:
        """
        Read profiles.
        """
        ...

    @abstractmethod
    def read_profile_views(self) -> List[Dict[str, Any]]:
        """
        Read profile views.
        """
        ...

    @abstractmethod
    def read_surfaces(self) -> List[Dict[str, Any]]:
        """
        Read terrain surfaces.
        """
        ...

    @abstractmethod
    def read_corridors(self) -> List[Dict[str, Any]]:
        """
        Read corridor definitions.
        """
        ...

    @abstractmethod
    def read_cross_sections(self) -> List[Dict[str, Any]]:
        """
        Read cross sections.
        """
        ...

    # =====================================================
    # Survey
    # =====================================================

    @abstractmethod
    def read_cogo_points(self) -> List[Dict[str, Any]]:
        """
        Read COGO points.
        """
        ...

    @abstractmethod
    def read_parcels(self) -> List[Dict[str, Any]]:
        """
        Read parcels.
        """
        ...

    # =====================================================
    # Pipe Networks
    # =====================================================

    @abstractmethod
    def read_pipe_networks(self) -> List[Dict[str, Any]]:
        """
        Read pipe networks.
        """
        ...

    # =====================================================
    # Generic
    # =====================================================

    @abstractmethod
    def exists(
        self,
        element_name: str
    ) -> bool:
        """
        Check whether an element exists.
        """
        ...

    @abstractmethod
    def read_element(
        self,
        element_name: str
    ) -> List[Dict[str, Any]]:
        """
        Read any LandXML element.
        """
        ...