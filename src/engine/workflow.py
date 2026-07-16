"""
workflow.py
===========

Workflow Manager

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List


# ==========================================================
# Workflow Step
# ==========================================================

@dataclass(slots=True)
class WorkflowStep:
    """
    Represents one execution step in the CDT-ROP workflow.
    """

    name: str

    action: Callable

    enabled: bool = True


# ==========================================================
# Workflow Manager
# ==========================================================

class Workflow:
    """
    Controls the execution order of the CDT-ROP platform.

    This class contains no engineering calculations.
    It only executes registered workflow steps.
    """

    def __init__(self):

        self.steps: List[WorkflowStep] = []

    # ------------------------------------------------------

    def add_step(

        self,

        name: str,

        action: Callable,

        enabled: bool = True

    ):

        self.steps.append(

            WorkflowStep(

                name=name,

                action=action,

                enabled=enabled

            )

        )

    # ------------------------------------------------------

    def remove_step(

        self,

        name: str

    ):

        self.steps = [

            step

            for step in self.steps

            if step.name != name

        ]

    # ------------------------------------------------------

    def run(self):

        """
        Execute all enabled workflow steps.
        """

        for step in self.steps:

            if not step.enabled:

                continue

            print(f"Running: {step.name}")

            step.action()

    # ------------------------------------------------------

    def summary(self):

        return [

            {

                "name": step.name,

                "enabled": step.enabled

            }

            for step in self.steps

        ]