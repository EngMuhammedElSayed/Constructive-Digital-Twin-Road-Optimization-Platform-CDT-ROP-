"""
update_policy.py
================

Digital Twin Update Policy Domain Model

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Represents the update policy used by the Constructive
Digital Twin.

This module stores update policy configuration only.

No synchronization, scheduling, or execution logic
is implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class UpdatePolicy:
    """
    Defines how the Digital Twin should be updated.
    """

    # =====================================================
    # General
    # =====================================================

    enabled: bool = True

    policy_name: str = "Default"

    description: str = ""

    # =====================================================
    # Update Mode
    # =====================================================

    mode: str = "Manual"

    automatic_updates: bool = False

    # =====================================================
    # Schedule
    # =====================================================

    update_interval_seconds: int = 300

    update_on_startup: bool = True

    update_on_project_open: bool = False

    update_on_file_change: bool = False

    update_after_optimization: bool = True

    # =====================================================
    # Validation
    # =====================================================

    validate_before_update: bool = True

    backup_before_update: bool = True

    rollback_on_failure: bool = True

    # =====================================================
    # Performance
    # =====================================================

    incremental_update: bool = True

    parallel_update: bool = False

    maximum_retry_attempts: int = 3

    # =====================================================
    # Logging
    # =====================================================

    log_updates: bool = True

    notify_on_failure: bool = True

    notify_on_success: bool = False

    # =====================================================
    # Metadata
    # =====================================================

    properties: Dict[str, str] = field(default_factory=dict)