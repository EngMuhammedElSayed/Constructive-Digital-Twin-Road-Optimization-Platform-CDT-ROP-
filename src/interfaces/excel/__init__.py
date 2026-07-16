"""
Excel Interface Package

CDT-ROP
Constructive Digital Twin Road Optimization Platform

This package defines the public interfaces used for
Excel integration within the CDT-ROP platform.

It provides abstract readers, writers, mappers,
validators and template managers.

Author : CDT-ROP Team
Version: 3.0.0
"""

from .reader import ExcelReader
from .writer import ExcelWriter
from .mapper import ExcelMapper
from .validator import ExcelValidator
from .templates import ExcelTemplateManager

__all__ = [
    "ExcelReader",
    "ExcelWriter",
    "ExcelMapper",
    "ExcelValidator",
    "ExcelTemplateManager",
]