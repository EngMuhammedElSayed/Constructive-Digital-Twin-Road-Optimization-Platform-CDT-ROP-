# System Components

## Overview

The Constructive Digital Twin system is divided into several independent components. Each component has a single responsibility to improve maintainability, extensibility, and software quality.

---

## User Interface

Responsible for collecting user inputs.

Examples:

- Project Information
- Design Parameters
- Optimization Settings

---

## Data Layer

Stores all engineering data.

Contains:

- Project
- Geometry
- Traffic
- Cost
- Surface
- Alignment
- Corridor

---

## Engineering Engine

Responsible for engineering calculations.

Examples:

- SSD
- HSO
- Earthwork
- Pavement Cost
- ROW Cost
- Capacity

---

## Optimization Engine

Responsible for:

- Objective Functions
- Constraints
- NSGA-II
- Pareto Front

---

## Visualization Engine

Responsible for:

- Charts
- Pareto Front
- Engineering Results

---

## Reporting Engine

Responsible for:

- PDF Reports
- Excel Reports
- Design Summary

---

## Civil 3D Connector

Responsible for communication with Autodesk Civil 3D.

Examples:

- Read Alignment
- Read Surface
- Read Corridor
- Update Design
