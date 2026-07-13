# Weather Datasets

## Purpose

This directory stores weather data that can be imported into the CDT-ROP platform.

Weather information is optional and is primarily intended for Digital Twin simulations, operational analysis, and future environmental assessment modules.

## Supported Formats

- CSV
- JSON

Additional formats and online weather services may be supported in future releases.

## Possible Data

- Air Temperature
- Relative Humidity
- Rainfall
- Wind Speed
- Wind Direction
- Visibility
- Atmospheric Pressure

## Data Flow

Weather File
      │
      ▼
Import Layer
(src/io/)
      │
      ▼
Validation
      │
      ▼
Weather Model
      │
      ▼
Digital Twin
      │
      ▼
Engineering Analysis

## Notes

- Weather data is optional.
- No weather datasets are included with the repository.
- Weather information may be imported from external files or online services in future releases.
