from enum import Enum


class DomainListingAdminServiceV1ModelMedianPriceDataPriceType(str, Enum):
    APARTMENTUNITFLAT = "apartmentUnitFlat"
    HOUSE = "house"
    VACANTLAND = "vacantLand"

    def __str__(self) -> str:
        return str(self.value)
