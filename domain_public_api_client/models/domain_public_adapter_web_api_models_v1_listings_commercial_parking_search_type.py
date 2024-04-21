from enum import Enum


class DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearchType(str, Enum):
    NOPARKING = "noParking"
    ONSITE = "onSite"
    ONSTREET = "onStreet"

    def __str__(self) -> str:
        return str(self.value)
