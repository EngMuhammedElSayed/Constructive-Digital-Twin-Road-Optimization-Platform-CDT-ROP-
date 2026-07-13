# Coding Guidelines

## Overview

This document defines the coding standards for the Constructive Digital Twin Road Optimization Platform (CDT-ROP).

The objective is to ensure that the codebase remains readable, maintainable, testable, and consistent throughout the project's development.

---

# General Principles

The project follows the following principles:

- Readability over cleverness
- Engineering-first design
- Modular architecture
- Separation of concerns
- Strong typing
- Reusable components
- Self-documenting code

---

# Python Version

Current supported version:

```
Python 3.12+
```

---

# Project Structure

```
src/
│
├── models/
├── calculations/
├── optimization/
├── engine/
├── io/
├── standards/
├── visualization/
├── reports/
├── plugins/
├── utils/
└── config/
```

Each module has a single responsibility.

---

# Naming Conventions

## Modules

Use lowercase.

Example

```
road_geometry.py
traffic_data.py
earthwork.py
```

---

## Classes

Use PascalCase.

Example

```python
Project
RoadGeometry
TrafficData
CostParameters
OptimizationSettings
```

---

## Functions

Use snake_case.

Example

```python
calculate_ssd()

load_alignment()

generate_report()

validate_surface()
```

---

## Variables

Use descriptive snake_case.

Good

```python
design_speed

minimum_radius

traffic_volume
```

Avoid

```python
x

tmp

value1
```

---

## Constants

Use UPPER_CASE.

Example

```python
MAX_SUPERELEVATION

DEFAULT_UNIT

EARTH_RADIUS
```

---

# Type Hints

Always use type hints.

Example

```python
def calculate_ssd(
    design_speed: float,
    grade: float
) -> float:
    ...
```

---

# Documentation

Every public class should include a docstring.

Example

```python
class Alignment:
    """
    Represents the horizontal roadway alignment.
    """
```

Every public function should also include a docstring.

---

# Comments

Explain engineering intent.

Do not explain obvious Python syntax.

Good

```python
# Convert design speed from km/h to m/s before calculation.
```

Avoid

```python
# Increment i
i += 1
```

---

# Import Order

Imports should follow this order.

1. Python Standard Library

```python
from pathlib import Path
```

2. Third-party Libraries

```python
import numpy as np
```

3. Project Imports

```python
from src.models.project.project import Project
```

Separate each group with one blank line.

---

# Error Handling

Raise meaningful exceptions.

Example

```python
raise ValueError(
    "Design speed must be greater than zero."
)
```

Never suppress exceptions silently.

Avoid

```python
except:
    pass
```

---

# Engineering Rules

Engineering calculations must:

- Never read files directly.
- Never modify project data.
- Never contain user interface code.
- Never contain export logic.

Calculations receive engineering models as input and return engineering results.

---

# Data Validation

Validate input before calculation.

Typical validation includes:

- Required values
- Unit consistency
- Coordinate systems
- Design limits
- Null values

---

# File Responsibilities

| Directory | Responsibility |
|------------|----------------|
| models | Engineering data models |
| calculations | Engineering equations |
| optimization | Optimization algorithms |
| io | Import and export |
| engine | Workflow orchestration |
| standards | Design standards |
| visualization | Charts and graphics |
| reports | Report generation |
| plugins | External software integration |
| utils | Shared utilities |

---

# Testing

Every new engineering calculation should include at least one unit test.

Future tests should verify:

- Numerical correctness
- Boundary conditions
- Invalid input handling

---

# Formatting

Recommended tools:

- black
- isort
- ruff

Formatting should be applied before committing code.

---

# Git Commit Messages

Use clear, descriptive commit messages.

Examples:

```
Add Project domain model

Implement SSD calculation

Refactor alignment validation

Add LandXML reader
```

Avoid messages such as:

```
Update

Fix

Changes
```

---

# Pull Requests

Every pull request should:

- Have a clear description.
- Reference related issues.
- Pass all tests.
- Update documentation when necessary.

---

# Future Improvements

Future versions may include:

- Automated linting
- Continuous Integration
- Static code analysis
- Documentation generation
- Code coverage reports

---

# Related Documents

- CONTRIBUTING.md
- development_workflow.md
- api_reference.md