from enum import Enum


class DomainListingAdminServiceV1ModelParkingDetailsParkingType(str, Enum):
    CARPORT = "carport"
    GARAGE = "garage"
    NOPARKING = "noParking"
    ONSITE = "onSite"
    ONSTREET = "onStreet"
    OUTDOOR = "outdoor"

    def __str__(self) -> str:
        return str(self.value)
