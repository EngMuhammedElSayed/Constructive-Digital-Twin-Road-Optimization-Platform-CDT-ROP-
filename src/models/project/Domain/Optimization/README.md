# Optimization Domain

## Overview

The **Optimization Domain** contains the core domain models that describe the optimization process used by the Constructive Digital Twin Road Optimization Platform (CDT-ROP).

These models define the optimization problem, objectives, constraints, decision variables, solutions, execution history, and results without implementing any optimization algorithms.

This package follows **Domain-Driven Design (DDD)** and **Clean Architecture** principles.

---

# Responsibilities

The Optimization Domain is responsible for representing:

- Optimization Problems
- Decision Variables
- Objective Definitions
- Engineering Constraints
- Optimization Solutions
- Pareto Fronts
- Optimization History
- Optimization Results
- Optimization Statistics
- Optimization Configuration
- Convergence Criteria
- Stopping Criteria

This package **does not implement** optimization algorithms.

---

# Folder Structure

```text
Optimization/

├── __init__.py

├── algorithm_settings.py
├── convergence_criteria.py
├── convergence_status.py

├── constraint_definition.py
├── constraint_violation.py

├── decision_variable.py
├── design_variable.py

├── evaluation_result.py
├── evaluation_settings.py

├── fitness.py

├── objective_function.py
├── objective_weight.py

├── optimization_configuration.py
├── optimization_constraint.py
├── optimization_history.py
├── optimization_iteration.py
├── optimization_metadata.py
├── optimization_objective.py
├── optimization_problem.py
├── optimization_result.py
├── optimization_settings.py
├── optimization_solution.py
├── optimization_statistics.py

├── pareto_front.py

├── stopping_criteria.py

└── README.md
```

---

# Domain Relationships

```text
OptimizationProblem
        │
        ├── DecisionVariable
        ├── OptimizationObjective
        ├── OptimizationConstraint
        ├── OptimizationSettings
        ├── AlgorithmSettings
        ├── EvaluationSettings
        ├── ConvergenceCriteria
        └── StoppingCriteria
                │
                ▼
OptimizationSolution
                │
                ▼
EvaluationResult
                │
                ▼
OptimizationIteration
                │
                ├── ParetoFront
                ├── OptimizationStatistics
                └── ConvergenceStatus
                        │
                        ▼
OptimizationHistory
                        │
                        ▼
OptimizationResult
```

---

# Design Principles

The Optimization Domain is based on:

- Domain-Driven Design (DDD)
- Clean Architecture
- SOLID Principles
- Separation of Concerns
- Single Responsibility Principle

---

# Scope

This package contains **domain entities only**.

No optimization algorithms are implemented here.

Examples of algorithms implemented elsewhere include:

- NSGA-II
- NSGA-III
- Genetic Algorithms
- Particle Swarm Optimization (PSO)
- Simulated Annealing
- Differential Evolution
- Mixed Integer Linear Programming (MILP)

---

# Implementation Location

Optimization algorithms belong to:

```text
src/optimization/
```

Engineering calculations belong to:

```text
src/calculations/
```

Input/Output processing belongs to:

```text
src/io/
```

The models in this package remain independent from any optimization library, including:

- pymoo
- DEAP
- PyGAD
- Pyomo
- Platypus
