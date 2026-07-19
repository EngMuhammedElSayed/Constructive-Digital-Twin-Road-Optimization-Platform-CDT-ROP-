"""
Optimization Domain Package
===========================

CDT-ROP
Constructive Digital Twin Road Optimization Platform

This package contains the domain models that describe
optimization problems, variables, objectives,
constraints, solutions, and optimization results.

The package contains data models only.

No optimization algorithms or numerical solvers are
implemented here.

Author : CDT-ROP Team
Version : 3.0.0
"""

from .algorithm_configuration import AlgorithmConfiguration
from .constraint_definition import ConstraintDefinition
from .design_variable import DesignVariable
from .evaluation_settings import EvaluationSettings
from .objective_function import ObjectiveFunction
from .optimization_constraint import OptimizationConstraint
from .optimization_history import OptimizationHistory
from .optimization_metadata import OptimizationMetadata
from .optimization_objective import OptimizationObjective
from .optimization_problem import OptimizationProblem
from .optimization_result import OptimizationResult
from .optimization_settings import OptimizationSettings
from .optimization_solution import OptimizationSolution
from .optimization_statistics import OptimizationStatistics
from .optimization_variable import OptimizationVariable
from .pareto_front import ParetoFront
from .stopping_criteria import StoppingCriteria
from .convergence_status import ConvergenceStatus

__all__ = [
    "AlgorithmConfiguration",
    "ConstraintDefinition",
    "ConvergenceStatus",
    "DesignVariable",
    "EvaluationSettings",
    "ObjectiveFunction",
    "OptimizationConstraint",
    "OptimizationHistory",
    "OptimizationMetadata",
    "OptimizationObjective",
    "OptimizationProblem",
    "OptimizationResult",
    "OptimizationSettings",
    "OptimizationSolution",
    "OptimizationStatistics",
    "OptimizationVariable",
    "ParetoFront",
    "StoppingCriteria",
]