"""
mapper.py
=========

Excel Data Mapper

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Maps Excel worksheet data to CDT-ROP domain models
and converts domain models back to Excel-compatible
structures.

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from dataclasses import asdict, is_dataclass
from typing import Any, Dict, List


class ExcelMapper:
    """
    Maps Excel worksheet data to CDT-ROP models
    and vice versa.

    This class performs no file I/O.
    """

    # =====================================================
    # Generic Mapping
    # =====================================================

    @staticmethod
    def model_to_dict(model: Any) -> Dict:
        """
        Convert a dataclass model to a dictionary.
        """

        if not is_dataclass(model):
            raise TypeError("Input must be a dataclass.")

        return asdict(model)

    # -----------------------------------------------------

    @staticmethod
    def dict_to_model(model_class, data: Dict):
        """
        Convert dictionary to dataclass model.
        """

        return model_class(**data)

    # =====================================================
    # Excel Row Mapping
    # =====================================================

    @staticmethod
    def row_to_model(model_class, row: Dict):
        """
        Convert one Excel row into a model.
        """

        return model_class(**row)

    # -----------------------------------------------------

    @staticmethod
    def model_to_row(model: Any) -> Dict:
        """
        Convert model to Excel row.
        """

        return ExcelMapper.model_to_dict(model)

    # =====================================================
    # Worksheet Mapping
    # =====================================================

    @staticmethod
    def worksheet_to_models(
        model_class,
        worksheet: List[Dict]
    ):
        """
        Convert worksheet rows into model list.
        """

        return [

            model_class(**row)

            for row in worksheet

        ]

    # -----------------------------------------------------

    @staticmethod
    def models_to_worksheet(
        models: List[Any]
    ) -> List[Dict]:
        """
        Convert model list into worksheet rows.
        """

        return [

            ExcelMapper.model_to_dict(model)

            for model in models

        ]

    # =====================================================
    # Template Mapping
    # =====================================================

    @staticmethod
    def map_template(
        worksheet: List[Dict],
        mapping: Dict
    ) -> List[Dict]:
        """
        Apply template field mapping.

        Parameters
        ----------
        worksheet
            Worksheet rows.

        mapping
            Mapping dictionary loaded from
            import_mapping.json.

        Returns
        -------
        List[Dict]
        """

        mapped_rows = []

        for row in worksheet:

            mapped = {}

            for excel_field, model_field in mapping.items():

                mapped[model_field] = row.get(excel_field)

            mapped_rows.append(mapped)

        return mapped_rows

    # =====================================================
    # Reverse Mapping
    # =====================================================

    @staticmethod
    def reverse_map(
        worksheet: List[Dict],
        mapping: Dict
    ) -> List[Dict]:
        """
        Convert model fields back to Excel fields.
        """

        reverse = {

            value: key

            for key, value in mapping.items()

        }

        rows = []

        for row in worksheet:

            excel_row = {}

            for model_field, value in row.items():

                excel_field = reverse.get(

                    model_field,

                    model_field

                )

                excel_row[excel_field] = value

            rows.append(excel_row)

        return rows