# Input Requirements

## Overview

The CDT-ROP platform accepts engineering project data from multiple external sources.

All project data is imported into the application, validated, and converted into engineering models before any calculations are performed.

The platform does not contain hard-coded project data.

---

# Supported Input Sources

The following input sources are currently supported or planned.

| Source | Format | Status |
|---------|---------|--------|
| CSV | .csv | Supported |
| Microsoft Excel | .xlsx | Supported |
| JSON | .json | Supported |
| LandXML | .xml | Supported |
| Autodesk Civil 3D | API | Planned |
| Bentley OpenRoads | API | Planned |
| IFC | .ifc | Planned |

---

# Required Project Data

Every project should provide the following engineering information.

| Data Type | Required | Model |
|------------|----------|-------|
| Project Information | Yes | ProjectMetadata |
| Project Settings | Yes | ProjectSettings |
| Horizontal Alignment | Yes | Alignment |
| Terrain Surface | Yes | Surface |
| Design Criteria | Yes | DesignCriteria |
| Optimization Settings | Yes | OptimizationSettings |
| Traffic Data | Optional | TrafficData |
| Cost Parameters | Optional | CostParameters |

---

# Project Metadata

Typical project information includes:

- Project Name
- Project Number
- Client
- Designer
- Organization
- Design Standard
- Coordinate System
- Unit System

---

# Geometry Input

Supported geometry sources:

- CSV Alignment
- LandXML
- Civil 3D
- OpenRoads (Future)

Geometry includes:

- Horizontal Alignment
- Vertical Profile
- Corridor
- Surface

---

# Terrain Input

Supported terrain formats:

- CSV Points
- LandXML Surface
- DEM
- TIN

---

# Traffic Input

Traffic information may include:

- AADT
- Design Hour Volume
- Heavy Vehicle Percentage
- Directional Distribution
- Peak Hour Factor
- Turning Movements

Traffic data is optional for geometric optimization but required for traffic analysis.

---

# Cost Input

Supported cost categories include:

- Earthwork
- Pavement
- Right-of-Way
- Structures
- Drainage
- Utilities

---

# Design Criteria

Engineering constraints include:

- Design Speed
- Maximum Grade
- Minimum Radius
- Maximum Superelevation
- Minimum Stopping Sight Distance
- Cross Slope
- Lane Width
- Shoulder Width

---

# Optimization Settings

Typical optimization parameters:

- Algorithm
- Population Size
- Number of Generations
- Objectives
- Constraints
- Random Seed

---

# Weather Data

Weather information is optional.

Possible inputs include:

- Temperature
- Rainfall
- Humidity
- Visibility
- Wind Speed

Weather data is intended for future Digital Twin extensions.

---

# File Organization

```
datasets/

├── alignments/
├── terrain/
├── traffic/
├── cost/
├── weather/
├── templates/
├── benchmark/
├── exports/
├── sample_projects/
└── standards/
```

---

# Import Workflow

```
External Files
        │
        ▼
Import Layer
(src/io)
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
```

---

# Validation Rules

Before data is accepted by the platform:

- Required fields must exist.
- Data types must be valid.
- Coordinate systems must be defined.
- Units must be specified.
- Missing mandatory information generates validation errors.

---

# Future Input Sources

Future versions may support:

- GIS Databases
- SQL Databases
- REST APIs
- IoT Sensors
- Digital Twin Services
- Cloud Storage
- BIM Servers

---

# Related Documents

- models_design.md
- data_flow.md
- system_architecture.md
- architecture/project_schema.md