# Project Class Diagram

## Overview

This document describes the object-oriented class structure of the Constructive Digital Twin Road Optimization Platform (CDT-ROP).

The class diagram represents the static architecture of the engineering data model and defines how the core classes interact with each other.

---

# Design Goals

The class model is designed to achieve:

- Modular architecture
- High cohesion
- Low coupling
- Extensibility
- Reusability
- Maintainability

---

# Root Class

```
Project
```

The `Project` class acts as the root object and owns all engineering domains.

---

# Project Class

## Attributes

```text
metadata
settings
domain
reports
state
```

## Responsibilities

- Manage project lifecycle
- Store engineering domains
- Coordinate engineering workflows
- Provide a unified access point

---

# ProjectMetadata

## Attributes

```text
project_name
project_number
client
designer
organization
description
design_standard
coordinate_system
unit_system
created_date
modified_date
```

## Responsibilities

Store general project information.

---

# ProjectSettings

## Attributes

```text
language
units
autosave
default_report_format
theme
active_standard
```

## Responsibilities

Store application and project configuration.

---

# RoadGeometry

## Attributes

```text
alignment
profile
surface
corridor
```

## Responsibilities

Represent the complete roadway geometry.

---

# Alignment

## Attributes

```text
name
length
start_station
end_station
elements
```

## Responsibilities

Store horizontal alignment data.

---

# Profile

## Attributes

```text
pvis
vertical_curves
grades
```

## Responsibilities

Store vertical alignment information.

---

# Surface

## Attributes

```text
name
coordinate_system
points
triangles
```

## Responsibilities

Represent the existing terrain model.

---

# Corridor

## Attributes

```text
regions
assemblies
targets
```

## Responsibilities

Represent the roadway corridor.

---

# TrafficData

## Attributes

```text
aadt
dhv
heavy_vehicle_percentage
phf
directional_distribution
```

## Responsibilities

Store traffic engineering data.

---

# CostParameters

## Attributes

```text
earthwork_cost
pavement_cost
row_cost
utility_cost
```

## Responsibilities

Store cost-related parameters.

---

# DesignCriteria

## Attributes

```text
design_speed
minimum_radius
maximum_grade
superelevation
ssd
```

## Responsibilities

Store engineering constraints.

---

# OptimizationSettings

## Attributes

```text
algorithm
population_size
generations
objectives
constraints
```

## Responsibilities

Store optimization configuration.

---

# Class Relationships

```
Project
│
├── ProjectMetadata
├── ProjectSettings
├── RoadGeometry
│      ├── Alignment
│      ├── Profile
│      ├── Surface
│      └── Corridor
│
├── TrafficData
├── CostParameters
├── DesignCriteria
└── OptimizationSettings
```

---

# Dependency Rules

The following dependency rules apply:

- Project owns all engineering objects.
- Calculation modules never own engineering data.
- Engineering models never access external files.
- Optimization operates on engineering models only.
- Reports consume calculation and optimization results.

---

# Engineering Layers

```
Project
      │
      ▼
Engineering Models
      │
      ▼
Engineering Calculations
      │
      ▼
Optimization
      │
      ▼
Visualization
      │
      ▼
Reporting
```

---

# Future Classes

The architecture allows the following classes to be added without modifying the existing design.

Future additions include:

- WeatherData
- DrainageModel
- UtilityNetwork
- BridgeModel
- PavementStructure
- ConstructionSchedule
- AssetModel
- DigitalTwinState

---

# UML Diagram

The complete UML class diagram is documented in:

```
architecture/uml_data_model.md
```

---

# Related Documents

- models_design.md
- object_relationship.md
- uml_data_model.md
- project_schema.md
- system_components.md