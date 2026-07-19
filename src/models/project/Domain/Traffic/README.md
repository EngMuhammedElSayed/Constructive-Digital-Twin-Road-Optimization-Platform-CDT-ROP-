# Traffic Domain

## Overview

The **Traffic Domain** represents all traffic engineering entities used by the Constructive Digital Twin Road Optimization Platform (CDT-ROP).

This domain stores traffic-related data used throughout the roadway design, pavement design, safety analysis, capacity evaluation, and optimization workflow.

The classes contained in this package are **Domain Models** only.

They do **not** implement engineering calculations or traffic simulation algorithms.

---

# Objectives

The Traffic Domain provides a unified representation of:

- Traffic demand
- Traffic characteristics
- Traffic growth
- Vehicle composition
- Highway capacity inputs
- Level of Service (LOS)
- Pavement traffic loading
- Operational traffic conditions

---

# Package Structure

```
Traffic/
│
├── __init__.py
│
├── accident_data.py
├── axle_load.py
├── capacity.py
├── check_vehicle.py
├── delay.py
├── demand_forecast.py
├── design_speed.py
├── design_vehicle.py
├── directional_distribution.py
├── esal.py
├── growth_factor.py
├── intersection.py
├── lane_distribution.py
├── level_of_service.py
├── operating_speed.py
├── origin_destination.py
├── peak_hour_factor.py
├── queue.py
│
└── README.md
```

---

# Domain Entities

The package contains entities representing:

- Traffic volumes
- Speed characteristics
- Design vehicles
- Traffic growth
- Demand forecasts
- Origin–Destination data
- ESAL values
- Capacity information
- Delay
- Queue
- Level of Service
- Lane distribution
- Directional distribution

---

# Relationships

```
Traffic Volume
        │
        ▼
Demand Forecast
        │
        ▼
Growth Factor
        │
        ▼
Peak Hour Factor
        │
        ▼
Directional Distribution
        │
        ▼
Lane Distribution
        │
        ▼
Capacity
        │
        ▼
Delay
        │
        ▼
Queue
        │
        ▼
Level Of Service
```

---

# Integration with Other Domains

The Traffic Domain interacts with:

```
Geometry Domain
        │
        ▼
Traffic Domain
        │
        ├────────► Pavement Domain
        │
        ├────────► Safety Domain
        │
        ├────────► Optimization Domain
        │
        └────────► Digital Twin Platform
```

---

# Used By

Traffic data is consumed by:

- Geometry Design
- Pavement Design
- Capacity Analysis
- Safety Assessment
- Cost Estimation
- Optimization
- Digital Twin Engine

---

# Engineering Standards

The domain is intended to support data compatible with:

- AASHTO Green Book
- Highway Capacity Manual (HCM)
- AASHTO 1993 Pavement Design Guide
- Mechanistic–Empirical Pavement Design Guide (MEPDG)
- MUTCD
- ISO 19650
- IFC
- COBie

---

# Design Principles

This package follows:

- Domain-Driven Design (DDD)
- Clean Architecture
- Single Responsibility Principle (SRP)

Each class represents a **single engineering entity**.

---

# What is NOT included

This package intentionally excludes:

- Capacity calculations
- HCM equations
- Delay equations
- LOS calculations
- Pavement equations
- Traffic assignment
- Demand forecasting algorithms
- AI prediction models
- SUMO simulations
- VISSIM simulations
- NSGA-II optimization

These implementations belong to:

```
src/calculations/
```

or

```
src/simulation/
```

or

```
src/optimization/
```

---

# Future Extensions

The Traffic Domain is designed to support future integration with:

- SUMO
- CARLA
- OpenDRIVE
- BIM
- GIS
- Real-Time IoT Sensors
- Digital Twin Services
