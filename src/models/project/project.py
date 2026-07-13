"""
===============================================================================
Project Model
===============================================================================

Constructive Digital Twin Road Optimization Platform (CDT-ROP)

Description
-----------
Root Aggregate of the CDT-ROP system.

The Project object represents a complete roadway engineering project and is
the primary object exchanged between all software modules.

Subsystems

- Engineering Calculations
- Optimization Engine
- Civil 3D Add-in
- Digital Twin
- Reporting
- Visualization

The Project model stores ONLY project data.

No engineering calculations shall be implemented in this module.

Author:
Eng. Muhammed

Research:
MSc Research
Cairo University
===============================================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

# =============================================================================
# Project Models
# =============================================================================

from models.project.project_metadata import ProjectMetadata
from models.project.project_settings import ProjectSettings

# =============================================================================
# Domain Model
# =============================================================================

from models.domain.domain import Domain

# =============================================================================
# Results
# =============================================================================

from models.results.project_results import ProjectResults

# =============================================================================
# Civil 3D
# =============================================================================

from models.civil3d.civil3d_project import Civil3DProject

# =============================================================================
# Reports
# =============================================================================

from models.reports.report_settings import ReportSettings


# =============================================================================
# Project
# =============================================================================

@dataclass
class Project:
    """
    Root Aggregate of the CDT-ROP Platform.
    """

    # -------------------------------------------------------------------------
    # Identity
    # -------------------------------------------------------------------------

    project_id: str = field(default_factory=lambda: str(uuid4()))

    version: str = "1.0.0"

    # -------------------------------------------------------------------------
    # Time Information
    # -------------------------------------------------------------------------

    created_at: datetime = field(default_factory=datetime.now)

    last_modified: datetime = field(default_factory=datetime.now)

    # -------------------------------------------------------------------------
    # Metadata
    # -------------------------------------------------------------------------

    metadata: ProjectMetadata = field(
        default_factory=ProjectMetadata
    )

    settings: ProjectSettings = field(
        default_factory=ProjectSettings
    )

    # -------------------------------------------------------------------------
    # Engineering Domain
    # -------------------------------------------------------------------------

    domain: Domain = field(
        default_factory=Domain
    )

    # -------------------------------------------------------------------------
    # Outputs
    # -------------------------------------------------------------------------

    results: ProjectResults = field(
        default_factory=ProjectResults
    )

    reports: ReportSettings = field(
        default_factory=ReportSettings
    )

    civil3d: Civil3DProject = field(
        default_factory=Civil3DProject
    )

    # -------------------------------------------------------------------------
    # Status Flags
    # -------------------------------------------------------------------------

    is_valid: bool = False

    is_saved: bool = False

    is_optimized: bool = False

    is_synced: bool = False

    # -------------------------------------------------------------------------
    # Project State
    # -------------------------------------------------------------------------

    def touch(self) -> None:
        """
        Updates the modification timestamp.
        """
        self.last_modified = datetime.now()

    def mark_modified(self) -> None:
        """
        Marks the project as modified.
        """
        self.is_saved = False
        self.touch()

    def mark_saved(self) -> None:
        """
        Marks the project as saved.
        """
        self.is_saved = True
        self.touch()

    def mark_optimized(self) -> None:
        """
        Marks the project as optimized.
        """
        self.is_optimized = True
        self.touch()

    def mark_synchronized(self) -> None:
        """
        Marks the project as synchronized with the Digital Twin.
        """
        self.is_synced = True
        self.touch()

    def validate(self) -> bool:
        """
        Placeholder for project validation.

        Returns
        -------
        bool
        """

        self.is_valid = True

        return self.is_valid

    def summary(self) -> dict:
        """
        Returns a lightweight project summary.
        """

        return {

            "Project ID": self.project_id,

            "Project Name": self.metadata.project_name,

            "Project Number": self.metadata.project_number,

            "Client": self.metadata.client,

            "Designer": self.metadata.designer,

            "Country": self.metadata.country,

            "Design Standard": self.metadata.design_standard,

            "Coordinate System": self.metadata.coordinate_system,

            "Units": self.metadata.units,

            "Version": self.version,

            "Created": self.created_at,

            "Last Modified": self.last_modified,

            "Valid": self.is_valid,

            "Saved": self.is_saved,

            "Optimized": self.is_optimized,

            "Synchronized": self.is_synced

        }

    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        """

        return (
            f"Project("
            f"name='{self.metadata.project_name}', "
            f"id='{self.project_id}', "
            f"version='{self.version}')"
        )

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return self.metadata.project_name
