"""
Project Metadata Model

Stores general information about the engineering project.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProjectMetadata:
    """
    General project information.
    """

    project_name: str = ""

    project_number: str = ""

    client: str = ""

    consultant: str = ""

    designer: str = ""

    organization: str = ""

    country: str = "Egypt"

    city: str = ""

    coordinate_system: str = ""

    units: str = "Metric"

    design_standard: str = "AASHTO"

    created_date: datetime = datetime.now()

    last_modified: datetime = datetime.now()

    description: str = ""
