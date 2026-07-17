# Interfaces Layer

## Overview

The **Interfaces** layer defines the public contracts used by the CDT-ROP platform to exchange data with external applications, engineering software, and storage formats.

This layer contains **interfaces only**.

No business logic, engineering calculations, optimization algorithms, or file parsing implementations are allowed in this package.

Concrete implementations belong to the integration layer.

---

# Objectives

The Interfaces layer provides a unified API between the CDT-ROP Core Engine and external systems.

It enables communication with:

- Autodesk Civil 3D
- Bentley OpenRoads Designer
- Microsoft Excel
- JSON
- LandXML
- Future BIM platforms
- Future GIS platforms
- Future databases
- Future cloud services

---

# Package Structure

```text
interfaces/

├── civil3d/
├── excel/
├── json/
├── landxml/
│
└── README.md
```

---

# Responsibilities

The Interfaces layer is responsible for defining:

- Readers
- Writers
- Validators
- Mappers
- Factories
- Exceptions

Each interface package follows the same architecture.

---

# Standard Package Layout

```text
interface_name/

__init__.py

README.md

exceptions.py
factory.py

reader.py
writer.py
mapper.py
validator.py
```

Additional helper modules may include:

```text
metadata.py

schema.py

version.py

namespaces.py

templates.py
```

depending on the interface requirements.

---

# Interface Workflow

```text
External File

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

Domain Models

        │

        ▼

Engineering Engine

        │

        ▼

Mapper

        │

        ▼

Writer

        │

        ▼

External File
```

---

# Supported Interfaces

## Civil3D

Purpose:

Communication with Autodesk Civil 3D.

---

## Excel

Purpose:

Reading and exporting engineering spreadsheets.

---

## JSON

Purpose:

Configuration files, project storage and API communication.

---

## LandXML

Purpose:

Road geometry and BIM interoperability.

---

# Design Principles

Every interface follows:

- Interface Segregation Principle
- Single Responsibility Principle
- Dependency Inversion Principle
- Factory Pattern
- Mapper Pattern
- Validation Layer
- Separation of Concerns

---

# Not Allowed

The Interfaces layer must **not** contain:

- Road geometry calculations
- Earthwork calculations
- Traffic calculations
- Pavement calculations
- Optimization algorithms
- Cost estimation
- Digital Twin simulation
- Database business logic

These belong to the engineering modules.

---

# Future Interfaces

The architecture is designed to support future interfaces such as:

```text
interfaces/

api/

csv/

database/

ifc/

infragml/

sqlite/

postgres/

mongodb/

rest/

grpc/

cloud/
```

without changing the CDT-ROP core.

---

# Implementation Layer

Concrete implementations should be developed separately.

Example:

```text
src/

interfaces/

integrations/
```

Example:

```text
integrations/

civil3d/

excel/

json/

landxml/
```

The CDT-ROP Core Engine communicates only with the interfaces and remains independent from any external software or library.

---

# Architecture Goal

The primary goal of this layer is to isolate the CDT-ROP engineering engine from all external technologies, allowing any interface implementation to be replaced without affecting the core platform.
