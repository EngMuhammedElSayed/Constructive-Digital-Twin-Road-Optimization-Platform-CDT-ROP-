# Cost Datasets

## Purpose

This directory stores cost-related input files used by the CDT-ROP platform.

Cost information is provided by the user and is never hard-coded inside the application.

## Supported Categories

- Earthwork
- Pavement
- Right of Way (ROW)
- Project Costs

## Input Sources

- Excel
- CSV
- JSON (Future)
- Database (Future)

## Data Flow

Cost File
    │
    ▼
Cost Reader
    │
    ▼
Validation
    │
    ▼
CostParameters Model
    │
    ▼
Cost Engine
    │
    ▼
Optimization Engine

## Notes

- No default project costs are included.
- All values are supplied by the user.
- Cost files are validated before use.
