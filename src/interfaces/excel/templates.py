"""
templates.py
============

Excel Template Manager

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Centralized management of all Excel templates.

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from .exceptions import TemplateNotFoundError


class ExcelTemplateManager:
    """
    Centralized manager for Excel templates.

    This class knows where templates are stored but
    does not read or write Excel files.
    """

    TEMPLATE_DIRECTORY = (
        Path(__file__).resolve()
        .parents[3]
        / "resources"
        / "templates"
    )

    TEMPLATES: Dict[str, str] = {

        "master": "excel_template.xlsx",

        "project": "project_template.xlsx",

        "alignment": "alignment_template.xlsx",

        "traffic": "traffic_template.xlsx",

        "terrain": "terrain_template.xlsx",

        "weather": "weather_template.xlsx",

        "cost": "cost_template.xlsx",

        "optimization": "optimization_template.xlsx",

    }

    # =====================================================
    # Template Path
    # =====================================================

    @classmethod
    def get_template_path(

        cls,

        template_name: str

    ) -> Path:

        if template_name not in cls.TEMPLATES:

            raise TemplateNotFoundError(

                f"Unknown template: {template_name}"

            )

        path = cls.TEMPLATE_DIRECTORY / cls.TEMPLATES[template_name]

        if not path.exists():

            raise TemplateNotFoundError(

                f"Template not found: {path}"

            )

        return path

    # =====================================================
    # List Templates
    # =====================================================

    @classmethod
    def list_templates(cls) -> List[str]:

        return sorted(cls.TEMPLATES.keys())

    # =====================================================
    # Check Template
    # =====================================================

    @classmethod
    def exists(

        cls,

        template_name: str

    ) -> bool:

        if template_name not in cls.TEMPLATES:

            return False

        return cls.get_template_path(template_name).exists()

    # =====================================================
    # Register Template
    # =====================================================

    @classmethod
    def register(

        cls,

        name: str,

        filename: str

    ) -> None:

        cls.TEMPLATES[name] = filename