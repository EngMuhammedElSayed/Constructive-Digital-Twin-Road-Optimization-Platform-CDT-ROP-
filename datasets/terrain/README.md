# Terrain Datasets

## Purpose

This directory stores terrain and surface data used by the CDT-ROP platform.

Terrain information is imported from external sources and is never hard-coded inside the application.

## Supported Input Formats

- CSV Point Files
- LandXML Surface Files
- DEM (Digital Elevation Model)
- TIN Surface Files

Additional formats may be supported in future releases.

## Data Flow

Terrain File
        │
        ▼
Import Layer
(src/io/)
        │
        ▼
Validation
        │
        ▼
Surface Model
        │
        ▼
Road Geometry
        │
        ▼
Earthwork Engine
        │
        ▼
Optimization Engine

## Notes

- Terrain files are supplied by the user.
- The repository does not include project terrain data.
- Imported datasets are validated before being converted into Surface models.
