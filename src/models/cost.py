from dataclasses import dataclass

@dataclass
class CostParameters:
    """
    Stores construction cost parameters.
    """

    pavement_cost: float
    row_cost: float
    earthwork_cost: float
