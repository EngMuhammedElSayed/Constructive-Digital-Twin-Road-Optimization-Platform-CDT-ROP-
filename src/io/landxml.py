"""
landxml.py
==========

LandXML I/O Facade

CDT-ROP
Constructive Digital Twin Road Optimization Platform

High-level access point for importing and exporting
LandXML documents.

This module delegates all operations to the configured
LandXML interface implementation.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from src.interfaces.landxml.factory import LandXMLFactory
from src.interfaces.landxml.reader import LandXMLReader
from src.interfaces.landxml.writer import LandXMLWriter
from src.interfaces.landxml.mapper import LandXMLMapper
from src.interfaces.landxml.validator import LandXMLValidator


class LandXMLIO:
    """
    High-level gateway for LandXML operations.
    """

    def __init__(self) -> None:

        self.reader: LandXMLReader = LandXMLFactory.create_reader()

        self.writer: LandXMLWriter = LandXMLFactory.create_writer()

        self.mapper: LandXMLMapper = LandXMLFactory.create_mapper()

        self.validator: LandXMLValidator = (
            LandXMLFactory.create_validator()
        )

    # =====================================================
    # Import
    # =====================================================

    def import_file(
        self,
        file_path: Path,
    ) -> Dict[str, Any]:
        """
        Import a LandXML document.
        """

        self.reader.open(file_path)

        return self.reader.read_document()

    # =====================================================
    # Export
    # =====================================================

    def export_file(
        self,
        destination: Path,
        data: Dict[str, Any],
    ) -> None:
        """
        Export a LandXML document.
        """

        self.writer.create_document()

        self.writer.write_document(data)

        self.writer.save(destination)

    # =====================================================
    # Validation
    # =====================================================

    def validate(
        self,
        file_path: Path,
    ) -> bool:
        """
        Validate a LandXML document.
        """

        self.reader.open(file_path)

        return self.validator.validate()["valid"]
