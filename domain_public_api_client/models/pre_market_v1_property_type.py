from enum import Enum


class PreMarketV1PropertyType(str, Enum):
    APARTMENTUNITFLAT = "apartmentUnitFlat"
    HOUSE = "house"
    TOWNHOUSE = "townhouse"
    VACANTLAND = "vacantLand"

    def __str__(self) -> str:
        return str(self.value)
