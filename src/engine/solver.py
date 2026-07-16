"""
solver.py
=========

Optimization Solver Manager

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Author : CDT-ROP Team
Version: 3.0.0
"""

from __future__ import annotations

from typing import Any


class Solver:
    """
    Generic optimization solver interface.

    This class acts as a facade between the
    application engine and optimization algorithms.

    It does NOT implement optimization algorithms.
    """

    def __init__(self, algorithm):

        self.algorithm = algorithm

    # =====================================================
    # Solve
    # =====================================================

    def solve(

        self,

        problem: Any

    ):

        """
        Execute optimization.

        Parameters
        ----------
        problem
            Optimization problem instance.

        Returns
        -------
        Optimization Result
        """

        return self.algorithm.solve(problem)

    # =====================================================
    # Information
    # =====================================================

    @property
    def name(self):

        return getattr(

            self.algorithm,

            "name",

            self.algorithm.__class__.__name__

        )

    @property
    def version(self):

        return getattr(

            self.algorithm,

            "version",

            "Unknown"

        )

    # =====================================================
    # Summary
    # =====================================================

    def summary(self):

        return {

            "solver": self.name,

            "version": self.version

        }
