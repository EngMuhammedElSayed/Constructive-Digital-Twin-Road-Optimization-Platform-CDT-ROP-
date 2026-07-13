# Project Schema

## Purpose

This document defines the complete structure of a road engineering project
used by the Constructive Digital Twin Road Optimization Platform (CDT-ROP).

The Project object is the root entity of the entire software architecture.

All calculations, optimization algorithms, Civil 3D integration,
report generation, and Digital Twin synchronization operate on this object.

---

# Project

Project
│
├── Metadata
├── Geometry
├── Traffic
├── Surface
├── Corridor
├── Cost
├── Standards
├── Optimization
├── Civil3D
├── Reports
├── Results
└── Digital Twin

---

## Metadata

Stores general project information.

Examples:

- Project Name
- Project Number
- Client
- Consultant
- Country
- Coordinate System
- Units

---

## Geometry

Stores roadway geometry.

Examples:

- Alignment
- Profile
- Cross Section
- Horizontal Curves
- Vertical Curves
- Design Speed

---

## Traffic

Stores traffic demand.

Examples:

- AADT
- DHV
- PHF
- Growth Rate
- Heavy Vehicles

---

## Surface

Stores terrain information.

Examples:

- Existing Ground
- Finished Ground
- TIN Surface
- DEM

---

## Corridor

Stores Civil 3D corridor information.

Examples:

- Baseline
- Regions
- Assemblies
- Sample Lines

---

## Cost

Stores cost parameters.

Examples:

- Earthwork Cost
- Pavement Cost
- ROW Cost

---

## Standards

Stores design standards.

Examples:

- AASHTO
- HCM
- Egyptian Code

---

## Optimization

Stores optimization settings.

Examples:

- NSGA-II
- Population
- Mutation
- Crossover
- Objectives

---

## Civil 3D

Stores Civil 3D references.

Examples:

- Drawing
- Alignment
- Corridor
- Surface

---

## Reports

Stores generated reports.

Examples:

- PDF
- Excel
- Quantities

---

## Results

Stores engineering calculation results.

Examples:

- Earthwork
- Safety
- Capacity
- Cost
- Constraints

---

## Digital Twin

Stores synchronization information.

Examples:

- Synchronization Time
- Update Interval
- Sensor Status
- Cloud Status
