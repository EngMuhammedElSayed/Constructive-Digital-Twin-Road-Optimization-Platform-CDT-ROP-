# Data Flow

## Overview

This document describes how engineering data flows through the Constructive Digital Twin Road Optimization Platform (CDT-ROP).

The platform follows a structured workflow in which external engineering data is imported, validated, converted into engineering models, processed by calculation engines, optimized, visualized, and finally exported.

---

# High-Level Data Flow

```
External Sources
        │
        ▼
Import Layer
        │
        ▼
Validation Layer
        │
        ▼
Engineering Data Models
        │
        ▼
Engineering Calculations
        │
        ▼
Optimization Engine
        │
        ▼
Visualization
        │
        ▼
Reporting
        │
        ▼
Export
```

---

# External Data Sources

The platform accepts data from multiple engineering sources.

```
CSV
Excel
LandXML
JSON
Civil 3D
```

Future versions may support:

- Bentley OpenRoads
- IFC
- GIS
- Cloud APIs

---

# Import Layer

Responsible modules:

```
src/io/
```

Examples:

- csv_reader.py
- excel_reader.py
- json_reader.py
- landxml.py

Responsibilities:

- Read external files
- Detect file format
- Parse engineering data
- Convert raw data into objects

---

# Validation Layer

Responsibilities:

- Verify required fields
- Check coordinate systems
- Validate units
- Validate geometry
- Validate engineering constraints

Invalid data is rejected before entering the Project model.

---

# Engineering Data Models

Validated data is converted into structured models.

```
Project
│
├── Metadata
├── Settings
├── Geometry
│
│   ├── Alignment
│   ├── Profile
│   ├── Surface
│   └── Corridor
│
├── Traffic
├── Cost
├── Design Criteria
└── Optimization
```

---

# Engineering Calculation Layer

Calculation modules receive engineering models.

Examples:

```
SSD

HSO

Earthwork

Capacity

Pavement

ROW
```

The calculation layer never reads external files directly.

It always operates on engineering models.

---

# Optimization Layer

Optimization receives:

- Geometry
- Traffic
- Cost
- Design Criteria

Produces:

- Optimized Design
- Pareto Solutions

---

# Visualization Layer

Responsible for displaying results.

Examples:

- Charts
- Pareto Front
- Dashboards
- Geometry Visualization

---

# Reporting Layer

Produces engineering reports.

Examples:

- PDF
- Excel
- CSV
- JSON

---

# Export Layer

Exports optimized engineering data.

Supported outputs:

- CSV
- Excel
- JSON
- LandXML

Future:

- Civil 3D
- IFC

---

# Detailed Workflow

```
                User
                  │
                  ▼
          Select Input Files
                  │
                  ▼
            Import Layer
                  │
                  ▼
          Validation Layer
                  │
                  ▼
             Project Model
                  │
                  ▼
        Engineering Models
                  │
                  ▼
      Engineering Calculations
                  │
                  ▼
      Optimization Engine
                  │
                  ▼
         Visualization Layer
                  │
                  ▼
          Reporting Engine
                  │
                  ▼
           Export Engine
```

---

# Module Interaction

```
datasets/
      │
      ▼
src/io
      │
      ▼
src/models
      │
      ▼
src/calculations
      │
      ▼
src/optimization
      │
      ▼
src/reports
      │
      ▼
datasets/exports
```

---

# Design Principles

The data flow follows the following principles:

- Single Direction Data Flow
- Separation of Concerns
- Strongly Typed Models
- No Engineering Calculations During Import
- No Direct File Access Inside Calculation Modules
- Independent Engineering Components

---

# Error Handling

Errors may occur during:

- File Reading
- Validation
- Engineering Calculations
- Optimization
- Export

Each layer reports errors independently without affecting other modules.

---

# Future Extensions

Future versions may include:

- Real-Time Digital Twin Synchronization
- Cloud Data Sources
- BIM Collaboration
- GIS Integration
- Live Sensor Streams
- REST API Integration

---

# Related Documents

- system_architecture.md
- models_design.md
- input_requirements.md
- architecture/system_components.md
- architecture/object_relationship.md