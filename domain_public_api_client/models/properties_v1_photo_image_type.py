from enum import Enum


class PropertiesV1PhotoImageType(str, Enum):
    FLOORPLAN = "Floorplan"
    GOOGLESTREETVIEW = "GoogleStreetView"
    PROPERTY = "Property"

    def __str__(self) -> str:
        return str(self.value)
