from enum import Enum


class ListingsV1MedianPriceDataPriceType(str, Enum):
    APARTMENTUNITFLAT = "apartmentUnitFlat"
    HOUSE = "house"
    VACANTLAND = "vacantLand"

    def __str__(self) -> str:
        return str(self.value)
