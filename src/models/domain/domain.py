"""
domain.py
=========

Base Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Defines the common base class for all domain models.

This module contains no engineering calculations.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any, Dict
from uuid import uuid4


@dataclass(slots=True)
class DomainModel:
    """
    Base class for all CDT-ROP domain models.
    """

    # =====================================================
    # Identity
    # =====================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""

    description: str = ""

    # =====================================================
    # Metadata
    # =====================================================

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    version: str = "1.0.0"

    # =====================================================
    # Custom Properties
    # =====================================================

    properties: Dict[str, Any] = field(default_factory=dict)

    # =====================================================
    # Helper Methods
    # =====================================================

    def update_timestamp(self) -> None:
        """
        Update the modification timestamp.
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the domain model to a dictionary.
        """
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """
        Create a domain model from a dictionary.
        """
        return cls(**data)