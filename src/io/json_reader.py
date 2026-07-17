"""
json_reader.py
==============

JSON Reader Facade

CDT-ROP
Constructive Digital Twin Road Optimization Platform

High-level access point for reading JSON resources.

This module delegates all reading operations to the
configured JSON interface implementation.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from src.interfaces.json.factory import JsonFactory
from src.interfaces.json.reader import JsonReader


class JsonResourceReader:
    """
    High-level JSON reader facade.
    """

    def __init__(self) -> None:
        self._reader: JsonReader = JsonFactory.create_reader()

    def open(self, file_path: Path) -> None:
        self._reader.open(file_path)

    def close(self) -> None:
        self._reader.close()

    def read(self) -> Dict[str, Any]:
        return self._reader.read()

    def read_object(self, key: str) -> Dict[str, Any]:
        return self._reader.read_object(key)

    def read_array(self, key: str) -> List[Any]:
        return self._reader.read_array(key)

    def read_value(self, key: str) -> Any:
        return self._reader.read_value(key)

    def metadata(self) -> Dict[str, Any]:
        return self._reader.metadata()
