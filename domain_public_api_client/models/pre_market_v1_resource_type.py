from enum import Enum


class PreMarketV1ResourceType(str, Enum):
    FLOORPLAN = "floorPlan"
    PHOTOGRAPH = "photograph"

    def __str__(self) -> str:
        return str(self.value)
