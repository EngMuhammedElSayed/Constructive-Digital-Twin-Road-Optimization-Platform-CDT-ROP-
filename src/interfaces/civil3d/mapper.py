"""
mapper.py
=========

Civil 3D Data Mapper

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict


class Civil3DMapper:
    """
    Maps CDT-ROP domain models to Civil 3D
    representations and vice versa.

    This class does not use Autodesk API directly.
    """

    # =====================================================
    # Generic
    # =====================================================

    @staticmethod
    def to_dict(model: Any) -> Dict:
        """
        Convert a dataclass model to dictionary.
        """

        return asdict(model)

    # -----------------------------------------------------

    @staticmethod
    def from_dict(model_class, data: Dict):
        """
        Create a dataclass from dictionary.
        """

        return model_class(**data)

    # =====================================================
    # Alignment
    # =====================================================

    @staticmethod
    def alignment_to_civil3d(model) -> Dict:
        """
        Convert CDT alignment model to
        Civil 3D alignment dictionary.
        """

        return asdict(model)

    @staticmethod
    def alignment_from_civil3d(model_class, data: Dict):
        """
        Convert Civil 3D alignment
        to CDT model.
        """

        return model_class(**data)

    # =====================================================
    # Profile
    # =====================================================

    @staticmethod
    def profile_to_civil3d(model):

        return asdict(model)

    @staticmethod
    def profile_from_civil3d(model_class, data):

        return model_class(**data)

    # =====================================================
    # Surface
    # =====================================================

    @staticmethod
    def surface_to_civil3d(model):

        return asdict(model)

    @staticmethod
    def surface_from_civil3d(model_class, data):

        return model_class(**data)

    # =====================================================
    # Corridor
    # =====================================================

    @staticmethod
    def corridor_to_civil3d(model):

        return asdict(model)

    @staticmethod
    def corridor_from_civil3d(model_class, data):

        return model_class(**data)

    # =====================================================
    # Project
    # =====================================================

    @staticmethod
    def project_to_civil3d(model):

        return asdict(model)

    @staticmethod
    def project_from_civil3d(model_class, data):

        return model_class(**data)
