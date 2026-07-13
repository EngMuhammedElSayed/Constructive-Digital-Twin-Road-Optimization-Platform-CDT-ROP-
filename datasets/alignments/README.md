# Alignment Datasets

## Purpose

This directory stores roadway alignment datasets used by the CDT-ROP platform.

The application supports importing alignment data from multiple external sources. No project-specific data is included in the repository.

## Supported Input Formats

- CSV
- LandXML

Additional formats may be supported in future releases.

## Directory Structure

alignments/
├── csv/
├── json/
├── landxml/
└── README.md

## Data Flow

External Source
        │
        ▼
Alignment File
        │
        ▼
Import Layer
(src/io/)
        │
        ▼
Validation Layer
        │
        ▼
Geometry Models
        │
        ▼
Project Model
        │
        ▼
Engineering Calculations
        │
        ▼
Optimization Engine

## Notes

- Alignment files are user-provided.
- The repository does not include fixed project data.
- Imported files are validated before being converted into engineering models.
- All imported data is mapped to the Project Domain Model.

