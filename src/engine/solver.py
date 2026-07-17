"""
solver.py
=========

Optimization Solver Manager

CDT-ROP
Constructive Digital Twin Road Optimization Platform

Provides a unified interface for optimization solvers.

Author : CDT-ROP Team
Version : 3.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


# ==========================================================
# Abstract Solver
# ==========================================================

class OptimizationSolver(ABC):
    """
    Base interface for all optimization algorithms.
    """

    @abstractmethod
    def solve(
        self,
        problem: Any
    ) -> Dict:
        """
        Solve an optimization problem.

        Parameters
        ----------
        problem
            Optimization problem.

        Returns
        -------
        Dict
            Optimization results.
        """
        ...


# ==========================================================
# Solver Manager
# ==========================================================

class SolverManager:
    """
    Registers and executes optimization solvers.
    """

    def __init__(self) -> None:

        self._solvers: Dict[str, OptimizationSolver] = {}

    # ------------------------------------------------------

    def register(
        self,
        name: str,
        solver: OptimizationSolver
    ) -> None:
        """
        Register a solver.
        """

        self._solvers[name.lower()] = solver

    # ------------------------------------------------------

    def available(self):

        """
        Return registered solvers.
        """

        return sorted(self._solvers.keys())

    # ------------------------------------------------------

    def get(
        self,
        name: str
    ) -> OptimizationSolver:

        """
        Return a registered solver.
        """

        name = name.lower()

        if name not in self._solvers:

            raise ValueError(

                f"Unknown solver: {name}"

            )

        return self._solvers[name]

    # ------------------------------------------------------

    def solve(
        self,
        name: str,
        problem: Any
    ) -> Dict:
        """
        Execute the selected solver.
        """

        solver = self.get(name)

        return solver.solve(problem)