# Object Relationship

```text
User
 │
 ▼
Project
 │
 ├────────► RoadGeometry
 │
 ├────────► TrafficData
 │
 ├────────► CostParameters
 │
 ├────────► OptimizationSettings
 │
 ├────────► SurfaceModel
 │
 ├────────► AlignmentModel
 │
 └────────► CorridorModel

             │
             ▼

Engineering Engine

             │
             ▼

Optimization Engine (NSGA-II)

             │
             ▼

Pareto Solutions

             │
             ▼

Reports

             │
             ▼

Civil 3D
```
