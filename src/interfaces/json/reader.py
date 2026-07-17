"""
reader.py
=========

JSON Reader Interface

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines the abstract interface used to read JSON files.

This module contains no implementation using the Python
json module or any third-party libraries.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List


class JsonReader(ABC):
    """
    Abstract interface for reading JSON files.

    Implementations are responsible for loading JSON
    documents and converting them into Python objects.
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
        Open a JSON file.
        """
        ...

    @abstractmethod
    def close(self) -> None:
        """
        Close the current JSON document.
        """
        ...

    # =====================================================
    # Read
    # =====================================================

    @abstractmethod
    def read(self) -> Dict:
        """
        Read the complete JSON document.
        """
        ...

    @abstractmethod
    def read_object(
        self,
        key: str
    ) -> Dict:
        """
        Read one JSON object.
        """
        ...

    @abstractmethod
    def read_array(
        self,
        key: str
    ) -> List:
        """
        Read one JSON array.
        """
        ...

    @abstractmethod
    def read_value(
        self,
        key: str
    ) -> Any:
        """
        Read one JSON value.
        """
        ...

    # =====================================================
    # Project Files
    # =====================================================

    @abstractmethod
    def read_project(self) -> Dict:
        """
        Read project configuration.
        """
        ...

    @abstractmethod
    def read_alignment(self) -> Dict:
        """
        Read alignment data.
        """
        ...

    @abstractmethod
    def read_terrain(self) -> Dict:
        """
        Read terrain data.
        """
        ...

    @abstractmethod
    def read_traffic(self) -> Dict:
        """
        Read traffic data.
        """
        ...

    @abstractmethod
    def read_weather(self) -> Dict:
        """
        Read weather data.
        """
        ...

    @abstractmethod
    def read_cost(self) -> Dict:
        """
        Read cost data.
        """
        ...

    @abstractmethod
    def read_optimization(self) -> Dict:
        """
        Read optimization settings.
        """
        ...

    @abstractmethod
    def read_digital_twin(self) -> Dict:
        """
        Read Digital Twin state.
        """
        ...

    # =====================================================
    # Metadata
    # =====================================================

    @abstractmethod
    def metadata(self) -> Dict:
        """
        Return JSON document metadata.
        """
        ...