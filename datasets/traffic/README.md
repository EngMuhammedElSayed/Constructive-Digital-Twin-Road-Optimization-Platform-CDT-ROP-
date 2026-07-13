# Traffic Datasets

## Purpose

This directory stores traffic data used by the CDT-ROP platform.

Traffic information is supplied by the user and imported into the application during project setup.

## Supported Formats

- CSV
- Microsoft Excel (.xlsx)

Additional formats may be supported in future releases.

## Typical Data

- Traffic Volume
- AADT
- Heavy Vehicle Percentage
- Design Hour Volume (DHV)
- Directional Distribution Factor (D)
- Peak Hour Factor (PHF)
- Turning Movements

## Data Flow

Traffic File
      │
      ▼
Import Layer
(src/io/)
      │
      ▼
Validation
      │
      ▼
TrafficData Model
      │
      ▼
Capacity Analysis
      │
      ▼
Optimization Engine

## Notes

- No project traffic data is included in the repository.
- All traffic data is imported from external files.
- Imported datasets are validated before use.
