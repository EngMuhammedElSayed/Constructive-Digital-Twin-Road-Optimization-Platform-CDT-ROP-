# JSON Interface

## Overview

The **JSON Interface** provides the abstraction layer for reading, validating, mapping, and writing JSON documents used throughout the Constructive Digital Twin Road Optimization Platform (CDT-ROP).

This package defines interfaces only. It does **not** contain any direct implementation using Python's built-in `json` module or third-party libraries.

Concrete implementations belong to the integration layer.

---

# Purpose

The JSON interface is responsible for providing a unified access layer for all JSON-based resources used by the platform.

Typical resources include:

- Project configuration
- Alignment data
- Terrain data
- Traffic data
- Weather data
- Cost databases
- Optimization settings
- Digital Twin state
- Reports
- Metadata
- Templates

---

# Package Structure

```text
json/

├── __init__.py
├── exceptions.py
├── factory.py
├── mapper.py
├── reader.py
├── validator.py
├── writer.py
└── README.md
```

---

# Module Description

## reader.py

Defines the abstract interface for reading JSON files.

Responsibilities:

- Open JSON documents
- Read objects
- Read arrays
- Read values
- Load engineering datasets

---

## writer.py

Defines the abstract interface for exporting JSON files.

Responsibilities:

- Create JSON documents
- Export engineering models
- Save optimization results
- Write reports

---

## mapper.py

Maps JSON data to CDT-ROP domain models and converts domain models back into JSON-compatible dictionaries.

Responsibilities:

- Dictionary → Model
- Model → Dictionary
- List mapping
- Field mapping

---

## validator.py

Defines the validation interface for JSON documents.

Validation includes:

- Required fields
- Missing keys
- Data types
- Engineering units
- Schema validation
- Version compatibility

---

## factory.py

Provides a centralized factory for creating JSON interface objects.

---

## exceptions.py

Contains all JSON-specific exceptions used throughout the platform.

---

# Architecture

```text
JSON File
      │
      ▼
JsonReader
      │
      ▼
JsonValidator
      │
      ▼
JsonMapper
      │
      ▼
Domain Models
      │
      ▼
Engineering Modules
      │
      ▼
JsonWriter
      │
      ▼
JSON File
```

---

# Responsibilities

The JSON interface is responsible for:

- Reading JSON documents
- Writing JSON documents
- Mapping JSON objects
- Validating JSON content
- Managing JSON metadata

The JSON interface is **not responsible for**:

- Engineering calculations
- Optimization algorithms
- Traffic analysis
- Geometry calculations
- Cost estimation
- Report generation

These responsibilities belong to other platform modules.

---

# Design Principles

The JSON interface follows:

- Separation of Concerns
- Single Responsibility Principle
- Interface Segregation Principle
- Factory Pattern
- Mapper Pattern
- Validation Layer
- Extensible Architecture

---

# Supported Resources

The interface is designed to support JSON documents for:

- Project
- Alignment
- Geometry
- Terrain
- Traffic
- Weather
- Cost
- Optimization
- Digital Twin
- Reports
- Metadata
- Configuration

---

# Future Development

Future implementations may support:

- JSON Schema validation
- JSON5
- GeoJSON
- Streaming JSON
- Compressed JSON
- Remote JSON APIs
- Cloud storage
- Version migration
- Incremental updates

without changing the public interface.

---

# Implementation Notes

This package defines only the public interface.

Concrete implementations should be placed in a dedicated integration layer, allowing different JSON libraries or storage mechanisms to be used without affecting the rest of the CDT-ROP architecture.
