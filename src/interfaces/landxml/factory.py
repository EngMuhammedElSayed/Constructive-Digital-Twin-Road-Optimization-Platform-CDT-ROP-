"""
factory.py
==========

LandXML Interface Factory

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Creates LandXML interface objects.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from .reader import LandXMLReader
from .writer import LandXMLWriter
from .mapper import LandXMLMapper
from .validator import LandXMLValidator


class LandXMLFactory:
    """
    Factory responsible for creating LandXML interface objects.
    """

    # =====================================================
    # Reader
    # =====================================================

    @staticmethod
    def create_reader() -> LandXMLReader:
        """
        Create a LandXML reader.
        """
        return LandXMLReader()

    # =====================================================
    # Writer
    # =====================================================

    @staticmethod
    def create_writer() -> LandXMLWriter:
        """
        Create a LandXML writer.
        """
        return LandXMLWriter()

    # =====================================================
    # Mapper
    # =====================================================

    @staticmethod
    def create_mapper() -> LandXMLMapper:
        """
        Create a LandXML mapper.
        """
        return LandXMLMapper()

    # =====================================================
    # Validator
    # =====================================================

    @staticmethod
    def create_validator() -> LandXMLValidator:
        """
        Create a LandXML validator.
        """
        return LandXMLValidator()