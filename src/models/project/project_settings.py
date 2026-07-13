"""
Project Settings Model
"""

from dataclasses import dataclass


@dataclass
class ProjectSettings:
    """
    Application settings for the project.
    """

    enable_civil3d: bool = True

    enable_digital_twin: bool = False

    enable_optimization: bool = True

    enable_reports: bool = True

    enable_visualization: bool = True

    autosave: bool = True

    autosave_interval: int = 10

    debug_mode: bool = False

    project_folder: str = ""

    output_folder: str = ""

    temporary_folder: str = ""
