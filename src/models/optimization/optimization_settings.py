"""
Optimization Settings Data Model

This module defines the optimization configuration used by the
Constructive Digital Twin Road Optimization Platform (CDT-ROP).

The class stores optimization parameters only.
No optimization algorithm is implemented here.

Author:
Eng. Muhammed

Research:
MSc Research - Cairo University
"""

from dataclasses import dataclass


@dataclass
class OptimizationSettings:
    """
    Stores the optimization configuration for the project.

    These parameters control the optimization engine and are
    independent of the selected optimization algorithm.
    """
    # -------------------------------------------------
    # Design Variables
    # -------------------------------------------------

    optimize_horizontal_radius: bool = True

    optimize_longitudinal_grade: bool = True

    optimize_lane_width: bool = True

    optimize_shoulder_width: bool = True

    optimize_median_width: bool = True

    optimize_superelevation: bool = True
    # -------------------------------------------------
    # General
    # -------------------------------------------------

    algorithm: str = "NSGA-II"

    random_seed: int = 1

    verbose: bool = True

    save_history: bool = True

    # -------------------------------------------------
    # Population
    # -------------------------------------------------

    population_size: int = 100

    number_of_generations: int = 200

    number_of_offspring: int = 100

    # -------------------------------------------------
    # Genetic Operators
    # -------------------------------------------------

    crossover_probability: float = 0.90

    crossover_eta: float = 15.0

    mutation_probability: float = 0.10

    mutation_eta: float = 20.0

    # -------------------------------------------------
    # Constraints
    # -------------------------------------------------

    eliminate_duplicates: bool = True

    repair_infeasible_solutions: bool = False

    # -------------------------------------------------
    # Multi-objective Settings
    # -------------------------------------------------

objective_names = (
    "Construction Cost",
    "Safety Index",
)

constraint_names = (
    "Minimum Curve Radius",
    "Horizontal Sightline Offset",
    "Traffic Capacity",
    "Minimum Grade",
)

    # -------------------------------------------------
    # Stopping Criteria
    # -------------------------------------------------

    termination_type: str = "n_gen"

    termination_value: int = 200

    # -------------------------------------------------
    # Output
    # -------------------------------------------------

    export_pareto_front: bool = True

    export_history: bool = True

    create_plots: bool = True

    export_reports: bool = True
