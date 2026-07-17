"""
writer.py
=========

LandXML Writer Interface

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines the abstract interface for exporting engineering
data into LandXML documents.

This module contains no XML serialization logic.
Concrete implementations belong to the integration layer.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List


class LandXMLWriter(ABC):
    """
    Abstract interface for writing LandXML documents.
    """

    # =====================================================
    # Document
    # =====================================================

    @abstractmethod
    def create_document(self) -> None:
        """
        Create a new LandXML document.
        """
        ...

    @abstractmethod
    def save(
        self,
        destination: Path
    ) -> None:
        """
        Save the LandXML document.
        """
        ...

    @abstractmethod
    def close(self) -> None:
        """
        Close the document.
        """
        ...

    # =====================================================
    # Metadata
    # =====================================================

    @abstractmethod
    def write_metadata(
        self,
        metadata: Dict[str, Any]
    ) -> None:
        """
        Write document metadata.
        """
        ...

    @abstractmethod
    def write_units(
        self,
        units: Dict[str, Any]
    ) -> None:
        """
        Write engineering units.
        """
        ...

    @abstractmethod
    def write_coordinate_system(
        self,
        coordinate_system: Dict[str, Any]
    ) -> None:
        """
        Write coordinate reference system.
        """
        ...

    # =====================================================
    # Geometry
    # =====================================================

    @abstractmethod
    def write_alignments(
        self,
        alignments: List[Dict[str, Any]]
    ) -> None:
        """
        Write horizontal alignments.
        """
        ...

    @abstractmethod
    def write_profiles(
        self,
        profiles: List[Dict[str, Any]]
    ) -> None:
        """
        Write profiles.
        """
        ...

    @abstractmethod
    def write_surfaces(
        self,
        surfaces: List[Dict[str, Any]]
    ) -> None:
        """
        Write terrain surfaces.
        """
        ...

    @abstractmethod
    def write_corridors(
        self,
        corridors: List[Dict[str, Any]]
    ) -> None:
        """
        Write corridor definitions.
        """
        ...

    @abstractmethod
    def write_cross_sections(
        self,
        cross_sections: List[Dict[str, Any]]
    ) -> None:
        """
        Write cross sections.
        """
        ...

    @abstractmethod
    def write_cogo_points(
        self,
        points: List[Dict[str, Any]]
    ) -> None:
        """
        Write COGO points.
        """
        ...

    @abstractmethod
    def write_pipe_networks(
        self,
        pipe_networks: List[Dict[str, Any]]
    ) -> None:
        """
        Write pipe networks.
        """
        ...

    # =====================================================
    # Generic
    # =====================================================

    @abstractmethod
    def write_element(
        self,
        element_name: str,
        data: Dict[str, Any]
    ) -> None:
        """
        Write a generic LandXML element.
        """
        ...

    @abstractmethod
    def write_document(
        self,
        data: Dict[str, Any]
    ) -> None:
        """
        Write a complete LandXML document.
        """
        ...