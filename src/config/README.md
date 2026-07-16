# Configuration Module

## Overview

The `config` module contains all application configuration files used by the CDT-ROP platform.

This module centralizes system settings and separates configuration from business logic.

No engineering equations, optimization algorithms, or project-specific data should be stored here.

---

# Objectives

- Centralize all configuration files.
- Separate configuration from implementation.
- Simplify system maintenance.
- Support multiple engineering standards.
- Allow easy customization without modifying source code.

---

# Directory Structure

```text
config/
│
├── README.md
├── app_config.py
├── civil3d_config.py
├── cost_config.py
├── defaults.py
├── digital_twin_config.py
├── geometry_config.py
├── optimization_config.py
├── paths.py
├── logging_config.py
├── localization_config.py
└── standards_config.py
```

---

# Configuration Files

## app_config.py

Global application settings.

Examples:

- Application name
- Version
- Default language
- Default country
- General system options

---

## civil3d_config.py

Autodesk Civil 3D integration settings.

Examples:

- Civil 3D version
- LandXML version
- Import options
- Export options
- BIM settings

---

## cost_config.py

Cost calculation system configuration.

Examples:

- Currency
- Cost database location
- Enabled cost modules
- Reporting options

Unit prices are NOT stored here.

---

## defaults.py

Global default values used by the application.

Examples:

- Default units
- Default language
- Default optimization algorithm
- Default coordinate system

---

## digital_twin_config.py

Constructive Digital Twin configuration.

Examples:

- Synchronization
- BIM integration
- GIS integration
- Database options
- Cache settings

---

## geometry_config.py

Geometry engine configuration.

Examples:

- Geometry modules
- Calculation options
- Precision
- Import/Export options

Design criteria are NOT stored here.

---

## optimization_config.py

Optimization engine settings.

Examples:

- Population size
- Number of generations
- Parallel processing
- Checkpoints

Objective functions and constraints are NOT defined here.

---

## paths.py

Centralized project paths.

Examples:

- Dataset directory
- Output directory
- Cache directory
- Log directory

---

## logging_config.py

Application logging configuration.

Examples:

- Log level
- Log format
- Log destination

---

## localization_config.py

Localization settings.

Examples:

- Languages
- Regional settings
- Number formatting
- Date formatting

---

## standards_config.py

Engineering standards configuration.

Examples:

- Active design standard
- Country
- Highway code
- Standard provider selection

---

# Design Philosophy

The configuration layer contains only system settings.

Engineering calculations belong to:

```text
src/calculations/
```

Optimization algorithms belong to:

```text
src/optimization/
```

Engineering standards belong to:

```text
src/standards/
```

Project datasets belong to:

```text
datasets/
```

---

# Architecture

```text
Configuration
        │
        ▼
Application Core
        │
        ▼
Standards Provider
        │
        ▼
Calculation Engines
        │
        ▼
Optimization Engine
        │
        ▼
Digital Twin
```

---

# Configuration Rules

- Never store engineering equations here.
- Never store project data here.
- Never store unit prices here.
- Never store optimization objectives here.
- Never hard-code engineering standards here.
- Configuration files should contain only system settings.

---

# Future Extensions

The configuration module is designed to support future integrations, including:

- Bentley OpenRoads Designer
- Autodesk InfraWorks
- Autodesk Revit
- ArcGIS
- QGIS
- PostgreSQL/PostGIS
- Cloud Digital Twin services

without modifying the existing architecture.