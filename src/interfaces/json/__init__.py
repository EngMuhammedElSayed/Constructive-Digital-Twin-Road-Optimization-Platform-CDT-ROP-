"""
JSON Interface Package

CDT-ROP
Constructive Digital Twin Road Optimization Platform

This package defines the public interfaces used for
JSON integration within the CDT-ROP platform.

It provides abstract readers, writers, mappers,
validators and factories.

Author : CDT-ROP Team
Version : 3.0.0
"""

from .reader import JsonReader
from .writer import JsonWriter
from .mapper import JsonMapper
from .validator import JsonValidator
from .factory import JsonFactory

__all__ = [
    "JsonReader",
    "JsonWriter",
    "JsonMapper",
    "JsonValidator",
    "JsonFactory",
]