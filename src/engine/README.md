# CDT-ROP Engine

## Overview

The **Engine** is the orchestration layer of the Constructive Digital Twin Road Optimization Platform (CDT-ROP).

It coordinates the complete engineering workflow from project loading to optimization, report generation, and result export.

The engine **does not implement engineering equations** or optimization algorithms directly. Instead, it coordinates specialized modules across the platform.

---

# Responsibilities

The engine is responsible for:

- Loading project data
- Initializing the platform
- Validating project inputs
- Executing engineering calculations
- Running optimization algorithms
- Updating the Digital Twin
- Managing workflow execution
- Generating engineering reports
- Exporting final results

---

# Engine Architecture

```text
                User
                  │
                  ▼
         CDTRoadOptimizationEngine
                  │
                  ▼
             Workflow Manager
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 Validation   Calculations  Optimization
     │            │            │
     └────────────┼────────────┘
                  ▼
          Digital Twin Update
                  │
                  ▼
             Report Generator
                  │
                  ▼
             Result Exporter
```

---

# Package Structure

```text
engine/

├── engine.py
├── solver.py
├── workflow.py
└── README.md
```

---

# Module Description

## engine.py

Main platform entry point.

Responsibilities:

- Load project
- Coordinate execution
- Control workflow
- Return results

---

## workflow.py

Defines the execution sequence.

Typical workflow:

1. Load project
2. Validate inputs
3. Run calculations
4. Run optimization
5. Update Digital Twin
6. Generate reports
7. Export outputs

---

## solver.py

Provides access to optimization solvers.

Future supported algorithms include:

- NSGA-II
- Genetic Algorithm
- Particle Swarm Optimization
- Simulated Annealing
- MILP
- Custom optimization methods

---

# Engine Workflow

```text
Project
   │
   ▼
Load
   │
   ▼
Validation
   │
   ▼
Engineering Calculations
   │
   ▼
Optimization
   │
   ▼
Digital Twin Update
   │
   ▼
Reports
   │
   ▼
Export
```

---

# Dependencies

The Engine coordinates the following modules:

```text
src/config/

src/models/

src/interfaces/

src/calculations/

src/optimization/

src/reporting/

src/validation/

src/utils/
```

The engine should never contain:

- Engineering equations
- AASHTO calculations
- HCM calculations
- Traffic equations
- Earthwork equations
- Cost equations

Those belong to the corresponding calculation modules.

---

# Design Principles

The engine follows:

- Separation of Concerns
- Single Responsibility Principle
- Orchestration Pattern
- Modular Architecture
- Configuration-Driven Execution
- Extensible Workflow Design

---

# Future Development

The Engine is designed to support:

- Multi-threaded execution
- Distributed optimization
- Cloud execution
- Batch project processing
- Real-time Digital Twin synchronization
- Plugin-based optimization solvers
- Multiple BIM/CAD integrations

without modifying the public Engine interface.

---

# Implementation Notes

The Engine should remain lightweight.

Its primary purpose is to orchestrate the execution of the CDT-ROP platform by coordinating specialized modules rather than implementing domain-specific logic.

This architecture ensures that engineering calculations, optimization algorithms, Digital Twin functionality, and reporting remain independent, reusable, and easy to maintain.