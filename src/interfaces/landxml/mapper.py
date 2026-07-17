"""
mapper.py
=========

LandXML Data Mapper

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Maps LandXML entities to CDT-ROP domain models and
vice versa.

This module performs no XML parsing or file I/O.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List


class LandXMLMapper(ABC):
    """
    Abstract interface for mapping LandXML entities
    to CDT-ROP domain models.
    """

    # =====================================================
    # Generic Mapping
    # =====================================================

    @abstractmethod
    def map_to_model(
        self,
        data: Dict[str, Any],
        model_class: type
    ) -> Any:
        """
        Map LandXML data to a domain model.
        """
        ...

    @abstractmethod
    def map_from_model(
        self,
        model: Any
    ) -> Dict[str, Any]:
        """
        Convert a domain model into LandXML-compatible data.
        """
        ...

    # =====================================================
    # Alignment
    # =====================================================

    @abstractmethod
    def map_alignment(
        self,
        alignment: Dict[str, Any]
    ) -> Any:
        """
        Map Alignment data.
        """
        ...

    # =====================================================
    # Profile
    # =====================================================

    @abstractmethod
    def map_profile(
        self,
        profile: Dict[str, Any]
    ) -> Any:
        """
        Map Profile data.
        """
        ...

    # =====================================================
    # Surface
    # =====================================================

    @abstractmethod
    def map_surface(
        self,
        surface: Dict[str, Any]
    ) -> Any:
        """
        Map Surface data.
        """
        ...

    # =====================================================
    # Corridor
    # =====================================================

    @abstractmethod
    def map_corridor(
        self,
        corridor: Dict[str, Any]
    ) -> Any:
        """
        Map Corridor data.
        """
        ...

    # =====================================================
    # COGO Points
    # =====================================================

    @abstractmethod
    def map_cogo_points(
        self,
        points: List[Dict[str, Any]]
    ) -> List[Any]:
        """
        Map COGO points.
        """
        ...

    # =====================================================
    # Metadata
    # =====================================================

    @abstractmethod
    def map_metadata(
        self,
        metadata: Dict[str, Any]
    ) -> Any:
        """
        Map LandXML metadata.
        """
        ...

    # =====================================================
    # Units
    # =====================================================

    @abstractmethod
    def map_units(
        self,
        units: Dict[str, Any]
    ) -> Any:
        """
        Map engineering units.
        """
        ...