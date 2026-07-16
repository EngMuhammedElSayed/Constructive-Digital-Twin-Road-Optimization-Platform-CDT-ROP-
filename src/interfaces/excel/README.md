# Excel Interface

## Overview

The **Excel Interface** provides the abstraction layer between Microsoft Excel workbooks and the CDT-ROP domain model.

This layer is responsible for defining how Excel data is imported, validated, mapped, and exported without depending on any specific Excel library.

The interface itself contains **no engineering calculations** and **no Excel implementation code**.

---

# Objectives

The Excel Interface is designed to:

- Import engineering datasets
- Export project results
- Validate workbook structure
- Map worksheet data to domain models
- Support configurable templates
- Support multiple spreadsheet formats in the future

---

# Supported Templates

The interface works with the templates located in:

```text
resources/templates/
```

Current templates include:

```text
excel_template.xlsx
project_template.xlsx
alignment_template.xlsx
traffic_template.xlsx
terrain_template.xlsx
weather_template.xlsx
cost_template.xlsx
optimization_template.xlsx
```

---

# Package Structure

```text
excel/

├── __init__.py
├── README.md
├── exceptions.py
├── factory.py
├── mapper.py
├── reader.py
├── templates.py
├── validator.py
└── writer.py
```

---

# Module Description

## reader.py

Defines the abstract interface for reading Excel workbooks.

Responsibilities:

- Open workbook
- Read worksheets
- Read rows
- Read columns
- Read templates

---

## writer.py

Defines the abstract interface for exporting CDT-ROP data to Excel.

Responsibilities:

- Export worksheets
- Export reports
- Export optimization results
- Export project data

---

## mapper.py

Responsible for mapping between:

```text
Excel Worksheets
        ⇅
CDT-ROP Domain Models
```

No file I/O occurs here.

---

## validator.py

Responsible for validating workbook structure.

Typical checks include:

- Missing worksheets
- Missing columns
- Empty required fields
- Invalid units
- Duplicate IDs
- Invalid data types

---

## templates.py

Provides access to Excel templates stored in:

```text
resources/templates/
```

This module centralizes template management.

---

## factory.py

Implements the Factory Pattern.

Creates interface components such as:

- ExcelReader
- ExcelWriter
- ExcelMapper
- ExcelValidator
- ExcelTemplateManager

---

## exceptions.py

Contains all custom exceptions related to Excel operations.

Examples include:

- ExcelFileNotFoundError
- WorksheetNotFoundError
- MissingColumnError
- ValidationError
- TemplateMismatchError

---

# Data Flow

```text
Excel Workbook
        │
        ▼
Reader
        │
        ▼
Validator
        │
        ▼
Mapper
        │
        ▼
CDT-ROP Domain Models
        │
        ▼
Engineering Calculations
        │
        ▼
Mapper
        │
        ▼
Writer
        │
        ▼
Excel Workbook
```

---

# Design Principles

The Excel Interface follows the following principles:

- Separation of Concerns
- Single Responsibility Principle
- Interface-Based Design
- Configuration-Driven Mapping
- Template-Based Import
- Library Independence

---

# Dependencies

The interface depends on:

```text
resources/templates/
resources/translations/
datasets/
src/models/
src/config/
```

The interface does **not** depend on:

- Geometry calculations
- Traffic calculations
- Optimization algorithms
- Digital Twin modules

---

# Future Extensions

The architecture is prepared for future support of:

- Microsoft Excel (.xlsx)
- CSV
- OpenDocument Spreadsheet (.ods)
- Google Sheets
- LibreOffice Calc

without changing the public interface.

---

# Implementation Notes

The files in this directory define the **interface layer only**.

Concrete implementations using libraries such as **openpyxl**, **pandas**, or other spreadsheet libraries should be placed in the integration layer, not in this package.

Recommended implementation location:

```text
src/
└── integrations/
    └── excel/
        ├── openpyxl_reader.py
        ├── openpyxl_writer.py
        ├── pandas_reader.py
        ├── pandas_writer.py
        └── template_loader.py
```

This separation ensures that the CDT-ROP platform remains independent of any specific spreadsheet library and simplifies future maintenance and extension.
