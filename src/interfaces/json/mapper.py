"""
mapper.py
=========

JSON Data Mapper

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Maps JSON data to CDT-ROP domain models and converts
domain models back to JSON-compatible dictionaries.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import asdict, is_dataclass
from typing import Any, Dict, List


class JsonMapper:
    """
    Maps JSON dictionaries to CDT-ROP domain models
    and vice versa.

    This class performs no file I/O.
    """

    # =====================================================
    # Model → Dict
    # =====================================================

    @staticmethod
    def model_to_dict(model: Any) -> Dict:
        """
        Convert a dataclass model into a JSON dictionary.
        """

        if not is_dataclass(model):
            raise TypeError("Input must be a dataclass.")

        return asdict(model)

    # =====================================================
    # Dict → Model
    # =====================================================

    @staticmethod
    def dict_to_model(
        model_class,
        data: Dict
    ):
        """
        Convert a JSON dictionary into a model.
        """

        return model_class(**data)

    # =====================================================
    # List → Models
    # =====================================================

    @staticmethod
    def list_to_models(
        model_class,
        data: List[Dict]
    ):
        """
        Convert a JSON array into a list of models.
        """

        return [

            model_class(**item)

            for item in data

        ]

    # =====================================================
    # Models → List
    # =====================================================

    @staticmethod
    def models_to_list(
        models: List[Any]
    ) -> List[Dict]:
        """
        Convert a list of models into JSON dictionaries.
        """

        return [

            JsonMapper.model_to_dict(model)

            for model in models

        ]

    # =====================================================
    # Generic Mapping
    # =====================================================

    @staticmethod
    def apply_mapping(
        data: Dict,
        mapping: Dict
    ) -> Dict:
        """
        Apply field mapping.

        Parameters
        ----------
        data
            Source JSON dictionary.

        mapping
            Dictionary describing field mappings.

        Returns
        -------
        Dict
        """

        mapped = {}

        for source, target in mapping.items():

            mapped[target] = data.get(source)

        return mapped

    # =====================================================
    # Reverse Mapping
    # =====================================================

    @staticmethod
    def reverse_mapping(
        data: Dict,
        mapping: Dict
    ) -> Dict:
        """
        Convert model fields back to JSON fields.
        """

        reverse = {

            value: key

            for key, value in mapping.items()

        }

        result = {}

        for field, value in data.items():

            json_field = reverse.get(field, field)

            result[json_field] = value

        return result