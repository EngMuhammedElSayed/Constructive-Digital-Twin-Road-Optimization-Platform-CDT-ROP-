# Cost Domain Models

## Overview

The **Cost** package contains the domain models responsible for representing all cost-related information within the Constructive Digital Twin Road Optimization Platform (CDT-ROP).

These models describe project cost entities only.

This package **does not perform**:

- Quantity Takeoff
- Engineering Calculations
- Cost Estimation
- Financial Analysis
- Optimization
- Life Cycle Cost Analysis (LCCA)

All engineering and financial calculations are implemented in the `calculations` layer.

---

# Purpose

The purpose of this package is to provide a structured representation of:

- Construction Costs
- Earthwork Costs
- Pavement Costs
- Drainage Costs
- Utility Costs
- Environmental Costs
- Maintenance Costs
- Right-of-Way Costs
- Cost Parameters
- Currency
- Inflation
- Contingency

These models are consumed by higher-level services such as:

- Quantity Takeoff Engine
- Cost Calculation Engine
- Optimization Engine
- Digital Twin
- Reporting

---

# Package Structure

```
Cost/
│
├── __init__.py
│
├── construction_cost.py
├── contingency.py
├── cost_breakdown.py
├── cost_category.py
├── cost_item.py
├── cost_model.py
├── cost_parameters.py
├── cost_summary.py
├── currency.py
├── drainage_cost.py
├── earthwork_cost.py
├── environmental_cost.py
├── inflation.py
├── maintenance_cost.py
├── pavement_cost.py
├── right_of_way_cost.py
├── structure_cost.py
├── utility_cost.py
│
└── README.md
```

---

# Architecture

```
Road Project
      │
      ▼
CostModel
      │
      ├─────────────┐
      │             │
      ▼             ▼
Construction     CostParameters
      │
      ▼
CostBreakdown
      │
      ├── Earthwork
      ├── Pavement
      ├── Drainage
      ├── Utilities
      ├── Structures
      ├── ROW
      ├── Environmental
      └── Maintenance
```

---

# Design Principles

The models contained in this package follow the following principles:

- Domain-Driven Design (DDD)
- Single Responsibility Principle (SRP)
- Immutable Engineering Data where applicable
- Separation of Data and Logic
- Calculation-Free Domain Models

---

# Responsibilities

This package is responsible for:

- Storing project cost information
- Organizing cost entities
- Providing structured data for calculations
- Providing input to optimization algorithms

---

# Not Responsible For

This package must never implement:

- Quantity Takeoff
- Cost Estimation Algorithms
- Earthwork Calculations
- Pavement Design
- AASHTO Equations
- NSGA-II
- Multi-objective Optimization
- Carbon Footprint Calculations
- Life Cycle Cost Analysis

Those responsibilities belong to other layers of the CDT-ROP architecture.

---

# Related Packages

```
src/calculations/
src/models/
src/optimization/
src/digital_twin/
src/interfaces/
```

---

# CDT-ROP Architecture

```
Geometry
      │
      ▼
Quantity Takeoff
      │
      ▼
Cost Calculation
      │
      ▼
Cost Domain Models
      │
      ▼
Optimization Engine
      │
      ▼
Digital Twin
```

---

# Version

Current Version: **3.0**

Project:

**Constructive Digital Twin Road Optimization Platform (CDT-ROP)**

Author:

**Eng. Muhammed El-Sayed**
