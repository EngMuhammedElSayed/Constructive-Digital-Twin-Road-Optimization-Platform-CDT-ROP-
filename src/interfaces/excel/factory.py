"""
factory.py
==========

Excel Interface Factory

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Creates Excel interface objects.

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from .reader import ExcelReader
from .writer import ExcelWriter
from .mapper import ExcelMapper
from .validator import ExcelValidator
from .templates import ExcelTemplateManager


class ExcelFactory:
    """
    Factory responsible for creating Excel interface objects.
    """

    # =====================================================
    # Reader
    # =====================================================

    @staticmethod
    def create_reader() -> ExcelReader:
        """
        Create an Excel reader.
        """

        return ExcelReader()

    # =====================================================
    # Writer
    # =====================================================

    @staticmethod
    def create_writer() -> ExcelWriter:
        """
        Create an Excel writer.
        """

        return ExcelWriter()

    # =====================================================
    # Mapper
    # =====================================================

    @staticmethod
    def create_mapper() -> ExcelMapper:
        """
        Create an Excel mapper.
        """

        return ExcelMapper()

    # =====================================================
    # Validator
    # =====================================================

    @staticmethod
    def create_validator() -> ExcelValidator:
        """
        Create an Excel validator.
        """

        return ExcelValidator()

    # =====================================================
    # Template Manager
    # =====================================================

    @staticmethod
    def create_template_manager() -> ExcelTemplateManager:
        """
        Create an Excel template manager.
        """

        return ExcelTemplateManager()