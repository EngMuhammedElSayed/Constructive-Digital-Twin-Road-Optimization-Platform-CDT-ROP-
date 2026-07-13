# API Reference

## Overview

This document provides a reference for the public modules, classes, and interfaces of the Constructive Digital Twin Road Optimization Platform (CDT-ROP).

The API reference is updated throughout the development lifecycle as new modules become available.

---

# Project Structure

```
src/
│
├── models/
├── calculations/
├── config/
├── engine/
├── io/
├── optimization/
├── plugins/
├── reports/
├── standards/
├── utils/
└── visualization/
```

---

# Models Package

## Project

Location

```
src/models/project/project.py
```

Purpose

The root object representing an engineering project.

Public Classes

| Class | Description |
|--------|-------------|
| Project | Main project container |
| ProjectMetadata | Project information |
| ProjectSettings | Project configuration |

---

## Geometry

Location

```
src/models/geometry/
```

Available Classes

| Class | Description |
|--------|-------------|
| RoadGeometry | Complete roadway geometry |
| Alignment | Horizontal alignment |
| Profile | Vertical alignment |
| Surface | Existing ground model |
| Corridor | Road corridor |

---

## Traffic

Location

```
src/models/traffic/
```

Available Classes

| Class | Description |
|--------|-------------|
| TrafficData | Traffic engineering data |

---

## Cost

Location

```
src/models/cost/
```

Available Classes

| Class | Description |
|--------|-------------|
| CostParameters | Cost input parameters |

---

## Optimization

Location

```
src/models/optimization/
```

Available Classes

| Class | Description |
|--------|-------------|
| OptimizationSettings | Optimization configuration |

---

# Calculation Modules

Location

```
src/calculations/
```

Current Modules

| Module | Status |
|----------|--------|
| SSD | Under Development |
| HSO | Under Development |
| Earthwork | Under Development |
| Pavement | Under Development |
| Capacity | Under Development |

---

# Standards Package

Location

```
src/standards/
```

Modules

| Module | Description |
|----------|-------------|
| aashto.py | AASHTO design standards |
| egypt.py | Egyptian road design standards |
| hcm.py | Highway Capacity Manual |

---

# Import Package

Location

```
src/io/
```

Modules

| Module | Description |
|----------|-------------|
| csv_reader.py | CSV Import |
| excel_reader.py | Excel Import |
| json_reader.py | JSON Import |
| landxml.py | LandXML Import |

---

# Optimization Package

Location

```
src/optimization/
```

Modules

| Module | Description |
|----------|-------------|
| algorithms | Optimization algorithms |
| objectives | Objective functions |
| constraints | Constraint definitions |
| results | Optimization results |

---

# Visualization Package

Location

```
src/visualization/
```

Modules

| Module | Description |
|----------|-------------|
| charts.py | Engineering charts |
| dashboard.py | Dashboard generation |
| pareto_plot.py | Pareto visualization |

---

# Reports Package

Location

```
src/reports/
```

Modules

| Module | Description |
|----------|-------------|
| report_generator.py | Main report engine |
| pdf_report.py | PDF export |
| excel_report.py | Excel export |

---

# Plugins

Location

```
src/plugins/
```

Modules

| Module | Description |
|----------|-------------|
| Civil3D | Autodesk Civil 3D integration |

---

# Utilities

Location

```
src/utils/
```

Modules

| Module | Description |
|----------|-------------|
| constants.py | Shared constants |
| helpers.py | Utility functions |
| validators.py | Validation functions |

---

# Public Interfaces

The following interfaces are planned:

- Geometry Engine
- Traffic Engine
- Cost Engine
- Optimization Engine
- Reporting Engine
- Civil 3D Connector

---

# Versioning

| Version | API Status |
|----------|------------|
| 0.1 | Initial Architecture |
| 0.2 | Data Models |
| 0.3 | Calculation Engine |
| 0.4 | Optimization Engine |
| 1.0 | Stable Public API |

---

# Documentation Status

| Package | Status |
|----------|--------|
| Models | ✅ |
| Standards | ✅ |
| IO | 🚧 |
| Calculations | 🚧 |
| Optimization | 🚧 |
| Visualization | ⏳ |
| Reports | ⏳ |
| Plugins | ⏳ |

---

# Related Documents

- system_architecture.md
- models_design.md
- coding_guidelines.md
- development_workflow.md