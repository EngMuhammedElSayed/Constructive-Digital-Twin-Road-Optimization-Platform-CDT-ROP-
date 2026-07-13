# Project Schema

## Overview

This document defines the canonical project schema used throughout the Constructive Digital Twin Road Optimization Platform (CDT-ROP).

Every project, regardless of its input source, is transformed into this internal schema before engineering calculations are performed.

The project schema serves as the Single Source of Truth (SSOT) for all engineering modules.

---

# Design Principles

The project schema follows the following principles:

- Single Source of Truth
- Strongly Typed Objects
- Domain Separation
- Extensible Architecture
- Independent Engineering Modules
- Platform Independence

---

# Canonical Project Schema

```
Project
│
├── Metadata
│
├── Settings
│
├── Domain
│   │
│   ├── Geometry
│   │      ├── Alignment
│   │      ├── Profile
│   │      ├── Surface
│   │      └── Corridor
│   │
│   ├── Traffic
│   │
│   ├── Cost
│   │
│   ├── DesignCriteria
│   │
│   └── Optimization
│
├── Reports
│
└── State
```

---

# Schema Description

## Metadata

Contains general project information.

Typical fields

- Project Name
- Project Number
- Client
- Organization
- Designer
- Description
- Coordinate System
- Unit System
- Design Standard

---

## Settings

Contains application settings.

Typical fields

- Language
- Units
- Autosave
- Active Standard
- Default Report Format

---

## Domain

Contains all engineering data.

The domain is divided into independent engineering modules.

---

### Geometry

Contains roadway geometry.

Includes

- Alignment
- Profile
- Surface
- Corridor

---

### Traffic

Contains traffic engineering information.

Examples

- AADT
- DHV
- PHF
- Heavy Vehicles

---

### Cost

Contains engineering cost parameters.

Examples

- Earthwork
- Pavement
- Right-of-Way
- Structures

---

### Design Criteria

Contains design constraints.

Examples

- Design Speed
- Minimum Radius
- Maximum Grade
- Superelevation
- SSD

---

### Optimization

Contains optimization settings.

Examples

- Algorithm
- Population Size
- Generations
- Objectives
- Constraints

---

## Reports

Contains generated engineering reports.

Examples

- PDF
- Excel
- JSON
- CSV

---

## State

Stores the current status of the engineering project.

Typical states

- Created
- Imported
- Validated
- Calculated
- Optimized
- Report Generated
- Exported

---

# Data Sources

The schema is independent of data sources.

Supported sources

```
CSV

Excel

JSON

LandXML

Civil 3D
```

Future sources

- OpenRoads
- IFC
- GIS
- Cloud APIs

---

# Import Mapping

```
CSV
      │
Excel
      │
JSON
      │
LandXML
      │
Civil 3D
      │
      ▼
 Import Layer
      │
      ▼
 Validation
      │
      ▼
 Project Schema
```

---

# Schema Usage

The project schema is used by:

- Engineering Calculations
- Optimization Engine
- Reporting Engine
- Visualization Engine
- Civil 3D Plugin
- Future Digital Twin Engine

---

# Schema Rules

Every project shall contain:

- Metadata
- Settings
- Domain

Geometry shall contain:

- Alignment
- Profile
- Surface

Traffic and Cost data are optional depending on the analysis.

Reports are generated after engineering calculations.

State is updated automatically during the project lifecycle.

---

# Future Extensions

The schema is designed for future expansion.

Future domains include

- Weather
- Drainage
- Utilities
- Bridges
- Pavement Structure
- Construction
- Asset Management
- Digital Twin

---

# Schema Evolution

The schema will evolve using semantic versioning.

Example

```
Schema v1.0
```

Future versions will maintain backward compatibility whenever possible.

---

# Related Documents

- project_class_diagram.md
- object_relationship.md
- uml_data_model.md
- models_design.md
- system_architecture.md