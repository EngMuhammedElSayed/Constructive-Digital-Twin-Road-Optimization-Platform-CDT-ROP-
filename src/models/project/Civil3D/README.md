# Civil3D Project Models

## Overview

This package contains **Civil 3D project-specific domain models** used by the CDT-ROP platform.

These models represent Civil 3D project information as structured Python objects.

The package does **not** contain:

- Autodesk Civil 3D API code
- COM Automation
- .NET Interop
- File readers or writers
- Business logic
- Geometry calculations

Those responsibilities belong to other packages.

---

# Purpose

This package provides a structured representation of:

- Civil 3D project information
- Drawing configuration
- Document settings
- Civil 3D object references
- Project metadata

The models act as containers between the interfaces layer and the optimization engine.

---

# Package Structure

```
Civil3D/
│
├── __init__.py
├── civil3d_project_info.py
├── drawing_settings.py
├── document_settings.py
├── object_references.py
├── project_metadata.py
└── README.md
```

---

# Responsibilities

This package is responsible for:

- Project information
- Drawing metadata
- Document configuration
- Object reference storage
- Civil 3D project state

---

# Not Responsible For

This package must never contain:

- Civil 3D COM calls
- Autodesk API calls
- LandXML parsing
- Excel import
- JSON import
- Optimization algorithms
- Engineering calculations
- Geometry generation

---

# Related Packages

```
src/
│
├── interfaces/
│   ├── civil3d/
│   ├── landxml/
│   ├── excel/
│   └── json/
│
├── io/
│
├── models/
│   ├── geometry/
│   ├── traffic/
│   ├── cost/
│   ├── optimization/
│   └── project/
│
├── calculations/
│
├── optimization/
│
└── engine/
```

---

# Design Philosophy

The package follows a Domain-Driven Design (DDD) approach.

Each model represents engineering data only.

No business logic should be implemented here.

---

# Future Extensions

Possible future models include:

- Civil3DStyles
- LabelSetConfiguration
- LayerConfiguration
- SurveyDatabase
- PipeNetworkConfiguration
- PressureNetworkConfiguration
