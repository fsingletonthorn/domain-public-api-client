from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingMedianPriceDataPriceType(str, Enum):
    APARTMENTUNITFLAT = "apartmentUnitFlat"
    HOUSE = "house"
    VACANTLAND = "vacantLand"

    def __str__(self) -> str:
        return str(self.value)
