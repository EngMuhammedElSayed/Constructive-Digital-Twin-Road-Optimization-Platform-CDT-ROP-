class BaseRoadStandard(ABC):

    @abstractmethod
    def get_side_friction(...):
        ...

    @abstractmethod
    def minimum_radius(...):
        ...

    @abstractmethod
    def summary(...):
        ...
      class AASHTO(BaseRoadStandard):
    ...

class EgyptCode(BaseRoadStandard):
    ...

class SaudiMOT(BaseRoadStandard):
    ...
