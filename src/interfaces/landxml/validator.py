"""
validator.py
============

LandXML Validator Interface

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines the abstract interface for validating
LandXML documents.

This module contains no XML validation logic.
Concrete implementations belong to the integration layer.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict


class LandXMLValidator(ABC):
    """
    Abstract interface for validating LandXML documents.
    """

    # =====================================================
    # File Validation
    # =====================================================

    @abstractmethod
    def validate_file(
        self,
        file_path: Path
    ) -> bool:
        """
        Validate a LandXML file.
        """
        ...

    # =====================================================
    # XML Structure
    # =====================================================

    @abstractmethod
    def validate_xml(self) -> bool:
        """
        Validate XML syntax.
        """
        ...

    @abstractmethod
    def validate_schema(self) -> bool:
        """
        Validate against the supported LandXML schema.
        """
        ...

    @abstractmethod
    def validate_namespace(self) -> bool:
        """
        Validate XML namespace.
        """
        ...

    @abstractmethod
    def validate_version(self) -> bool:
        """
        Validate LandXML version.
        """
        ...

    # =====================================================
    # Metadata
    # =====================================================

    @abstractmethod
    def validate_metadata(self) -> bool:
        """
        Validate project metadata.
        """
        ...

    @abstractmethod
    def validate_units(self) -> bool:
        """
        Validate engineering units.
        """
        ...

    @abstractmethod
    def validate_coordinate_system(self) -> bool:
        """
        Validate coordinate reference system.
        """
        ...

    # =====================================================
    # Geometry
    # =====================================================

    @abstractmethod
    def validate_alignments(self) -> bool:
        """
        Validate horizontal alignments.
        """
        ...

    @abstractmethod
    def validate_profiles(self) -> bool:
        """
        Validate profiles.
        """
        ...

    @abstractmethod
    def validate_surfaces(self) -> bool:
        """
        Validate terrain surfaces.
        """
        ...

    @abstractmethod
    def validate_corridors(self) -> bool:
        """
        Validate corridor definitions.
        """
        ...

    @abstractmethod
    def validate_cross_sections(self) -> bool:
        """
        Validate cross sections.
        """
        ...

    @abstractmethod
    def validate_cogo_points(self) -> bool:
        """
        Validate COGO points.
        """
        ...

    @abstractmethod
    def validate_pipe_networks(self) -> bool:
        """
        Validate pipe networks.
        """
        ...

    # =====================================================
    # Complete Validation
    # =====================================================

    @abstractmethod
    def validate(self) -> Dict[str, Any]:
        """
        Execute complete validation.

        Returns
        -------
        Dict[str, Any]

        Example
        -------
        {
            "valid": True,
            "errors": [],
            "warnings": [],
            "schema": "LandXML 1.2"
        }
        """
        ...