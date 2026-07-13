# Engineering Data Model Design

## Overview

The CDT-ROP platform is built around a centralized engineering data model.

Each engineering module operates on structured domain objects rather than raw files. External data (CSV, Excel, LandXML, JSON, Civil 3D) is imported, validated, and converted into strongly typed models before being processed by the calculation and optimization engines.

---

# Design Principles

The engineering data model follows these principles:

- Single Source of Truth
- Separation of Concerns
- Strongly Typed Objects
- Modular Design
- Extensibility
- Engineering-Oriented Structure
- Platform Independence

---

# Data Model Hierarchy

```
Project
│
├── Metadata
├── Settings
│
├── Geometry
│   ├── Alignment
│   ├── Profile
│   ├── Surface
│   └── Corridor
│
├── Traffic
│
├── Cost
│
├── Optimization
│
└── Design Criteria
```

---

# Core Models

## Project

The root object of the application.

Responsibilities:

- Stores project metadata
- Connects all engineering models
- Coordinates project lifecycle

---

## ProjectMetadata

Stores general project information.

Typical information includes:

- Project Name
- Client
- Designer
- Design Standard
- Coordinate System
- Units

---

## ProjectSettings

Stores application and project settings.

Examples:

- Active Design Standard
- Unit System
- Optimization Options
- Report Settings

---

## RoadGeometry

Represents the roadway geometry.

Contains:

- Alignment
- Profile
- Surface
- Corridor

---

## Alignment

Represents the horizontal alignment.

Contains:

- Tangents
- Circular Curves
- Spiral Curves
- Stations

---

## Profile

Represents the vertical alignment.

Contains:

- Grades
- Vertical Curves
- PVI Data

---

## Surface

Represents terrain information.

Supported sources:

- LandXML
- CSV
- DEM
- Civil 3D

---

## Corridor

Represents the roadway corridor.

Contains:

- Assembly Information
- Regions
- Targets
- Cross Sections

---

## TrafficData

Stores roadway traffic information.

Examples:

- AADT
- DHV
- Heavy Vehicle Percentage
- PHF
- Directional Distribution

---

## CostParameters

Stores engineering cost parameters.

Categories include:

- Earthwork
- Pavement
- Right-of-Way
- Construction

---

## DesignCriteria

Stores engineering design constraints.

Examples:

- Design Speed
- Maximum Grade
- Minimum Radius
- Superelevation
- Stopping Sight Distance

---

## OptimizationSettings

Stores optimization configuration.

Examples:

- Algorithm
- Population Size
- Generations
- Objectives
- Constraints

---

# Relationships Between Models

```
Project
│
├── Metadata
├── Settings
├── Geometry
│     ├── Alignment
│     ├── Profile
│     ├── Surface
│     └── Corridor
│
├── Traffic
├── Cost
├── Design Criteria
└── Optimization
```

---

# Data Lifecycle

```
External Files
      │
      ▼
Import Layer
      │
      ▼
Validation
      │
      ▼
Engineering Models
      │
      ▼
Calculation Engine
      │
      ▼
Optimization Engine
      │
      ▼
Visualization
      │
      ▼
Reporting
```

---

# Supported Input Sources

The engineering models can be populated from:

- CSV
- Excel
- JSON
- LandXML
- Autodesk Civil 3D

Future versions may support:

- OpenRoads Designer
- IFC
- GIS
- Cloud Services

---

# Model Responsibilities

| Model | Responsibility |
|--------|----------------|
| Project | Root engineering object |
| ProjectMetadata | Project information |
| ProjectSettings | Configuration |
| RoadGeometry | Road geometry |
| Alignment | Horizontal alignment |
| Profile | Vertical alignment |
| Surface | Terrain model |
| Corridor | Corridor definition |
| TrafficData | Traffic information |
| CostParameters | Cost data |
| DesignCriteria | Engineering constraints |
| OptimizationSettings | Optimization configuration |

---

# Future Extensions

The data model is designed to support future modules without changing the core architecture.

Planned extensions include:

- Weather Model
- Drainage Model
- Utilities Model
- Bridge Model
- Pavement Structure Model
- Construction Schedule
- Digital Twin State
- Asset Management

---

# Related Documents

- system_architecture.md
- architecture/project_class_diagram.md
- architecture/object_relationship.md
- architecture/uml_data_model.md