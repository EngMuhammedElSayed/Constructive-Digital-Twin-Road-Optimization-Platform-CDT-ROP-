# Digital Twin Models

## Overview

This package contains the **domain models** representing the Constructive Digital Twin used by the CDT-ROP platform.

The models define the structure of the Digital Twin during the road design lifecycle without implementing synchronization, simulation, or communication logic.

---

# Purpose

The package provides data models for:

- Digital Twin configuration
- Data sources
- Synchronization settings
- Simulation settings
- Metadata
- Version information
- Digital Twin state

These models serve as containers exchanged between the Digital Twin engine, optimization engine, BIM interfaces, and project domain.

---

# Package Structure

```text
digital_twin/
│
├── __init__.py
├── digital_twin.py
├── digital_twin_configuration.py
├── data_source.py
├── synchronization_settings.py
├── synchronization_status.py
├── simulation_settings.py
├── sensor_configuration.py
├── update_policy.py
├── version_control.py
├── twin_metadata.py
└── README.md
```

---

# Responsibilities

This package is responsible for:

- Representing the Digital Twin domain
- Defining Digital Twin configuration
- Managing Digital Twin metadata
- Defining synchronization parameters
- Defining simulation parameters
- Representing available data sources

---

# Out of Scope

This package must **never** contain:

- Civil 3D API calls
- LandXML parsing
- Excel import/export
- JSON parsing
- Database access
- REST API communication
- Synchronization logic
- Optimization algorithms
- Engineering calculations
- Event processing
- Simulation execution

These responsibilities belong to other packages.

---

# Related Packages

```text
src/
│
├── digital_twin/
│
├── engine/
│
├── optimization/
│
├── interfaces/
│
├── io/
│
├── calculations/
│
└── models/
```

---

# Design Philosophy

The package follows **Domain-Driven Design (DDD)**.

Each class represents engineering or Digital Twin data only.

Business logic is intentionally separated into services and engines.

---

# Future Extensions

Possible future additions include:

- TwinSnapshot
- TwinState
- TwinEvent
- HealthStatus
- SensorReading
- SynchronizationLog
- PredictionResult
- SimulationResult
- DataStream
- EventHistory
