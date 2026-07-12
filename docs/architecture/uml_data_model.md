# UML Data Model

```text
                               +----------------------+
                               |      Project         |
                               +----------------------+
                               | name                 |
                               | description          |
                               | design_standard      |
                               | project_length       |
                               +----------------------+
                                         |
       -----------------------------------------------------------------
       |                 |                 |              |             |
       |                 |                 |              |             |
       ▼                 ▼                 ▼              ▼             ▼

+----------------+ +----------------+ +----------------+ +----------------+ +----------------+
| RoadGeometry   | | TrafficData    | | CostParameters | | Optimization   | | SurfaceModel   |
+----------------+ +----------------+ +----------------+ +----------------+ +----------------+
| radius         | | demand         | | pavement_cost  | | population     | | surface_name   |
| grade          | | capacity       | | row_cost       | | generations    | | source_file    |
| lane_width     | | PHF            | | earthwork_cost | | objectives     | | coordinate_sys |
| shoulder_width | | HV%            | | unit_prices    | | constraints    | | resolution     |
| median_width   | +----------------+ +----------------+ +----------------+ +----------------+
| superelevation |
+----------------+

                     |
                     |
                     ▼

              +-------------------+
              | AlignmentModel    |
              +-------------------+
              | horizontal        |
              | vertical          |
              | stations          |
              +-------------------+

                     |
                     ▼

              +-------------------+
              | CorridorModel     |
              +-------------------+
              | assembly          |
              | regions           |
              | targets           |
              +-------------------+
```
