# Engine Module

## Overview

The **Engine** module is the orchestration layer of the CDT-ROP platform.

It coordinates all major subsystems without performing engineering calculations itself.

The engine is responsible for controlling the complete workflow of the platform, from loading project data to generating optimization results and updating the Constructive Digital Twin.

---

# Responsibilities

The Engine Layer is responsible for:

- Loading project configuration
- Loading engineering standards
- Loading datasets
- Initializing system modules
- Coordinating calculation engines
- Executing optimization workflows
- Managing Digital Twin synchronization
- Generating reports
- Handling execution pipeline

The Engine Layer **does not perform engineering calculations**.

---

# Architecture

```text
                 User Interface
                        │
                        ▼
                 Application Engine
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
 Validation        Calculation      Optimization
                        │
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
 Geometry          Traffic            Pavement
      ▼                 ▼                 ▼
 Earthwork         Cost            Digital Twin
                        │
                        ▼
                    Reporting
```

---

# Directory Structure

```text
engine/

├── README.md
├── engine.py
├── project_engine.py
├── validation_engine.py
├── geometry_engine.py
├── traffic_engine.py
├── earthwork_engine.py
├── cost_engine.py
├── optimization_engine.py
├── digital_twin_engine.py
├── report_engine.py
└── pipeline.py
```

---

# Module Description

## engine.py

Main application orchestrator.

Coordinates the execution of all platform modules.

---

## project_engine.py

Loads and manages project data.

Responsibilities include:

- Project initialization
- Project lifecycle
- Project metadata

---

## validation_engine.py

Executes all validation modules before calculations.

Includes:

- Geometry validation
- Traffic validation
- Cost validation
- Project validation

---

## geometry_engine.py

Coordinates all geometry calculations.

Includes:

- Horizontal Alignment
- Vertical Alignment
- SSD
- HSO
- Superelevation
- Earthwork Geometry

---

## traffic_engine.py

Coordinates all traffic calculations.

Includes:

- Capacity
- LOS
- Delay
- Queue
- Speed
- Safety

---

## earthwork_engine.py

Coordinates earthwork calculations.

Includes:

- Cut
- Fill
- Mass Haul
- Balance

---

## cost_engine.py

Coordinates all project cost modules.

Includes:

- Earthwork Cost
- Pavement Cost
- Bridge Cost
- Drainage Cost
- Utility Cost
- Traffic Cost
- Environmental Cost
- Life Cycle Cost

---

## optimization_engine.py

Controls optimization workflow.

Supports:

- NSGA-II
- Future optimization algorithms

---

## digital_twin_engine.py

Updates the Constructive Digital Twin.

Coordinates:

- BIM
- GIS
- Databases
- Synchronization
- History

---

## report_engine.py

Generates project outputs.

Supports:

- PDF
- Excel
- HTML
- LaTeX
- JSON

---

## pipeline.py

Defines the execution workflow of the platform.

Typical execution order:

1. Load Configuration
2. Load Standards
3. Load Project
4. Validate Inputs
5. Run Geometry
6. Run Traffic
7. Run Earthwork
8. Run Cost
9. Run Optimization
10. Update Digital Twin
11. Generate Reports

---

# Design Principles

The Engine Layer follows these principles:

- Single Responsibility Principle
- Separation of Concerns
- Modular Architecture
- Dependency Injection
- Configuration-Driven Execution

---

# Dependencies

The Engine Layer depends on:

```text
config/
core/
calculations/
standards/
optimization/
digital_twin/
io/
validation/
reporting/
```

The Engine Layer should **not** contain:

- Engineering equations
- Design standards
- Optimization mathematics
- Unit prices
- Project-specific data

These responsibilities belong to their respective modules.

---

# Future Extensions

The architecture is designed to support future integration with:

- Autodesk Civil 3D
- Bentley OpenRoads Designer
- Autodesk InfraWorks
- ArcGIS
- QGIS
- SUMO
- CARLA
- Cloud-based Digital Twin platforms
- Distributed optimization engines

without changing the Engine architecture.
