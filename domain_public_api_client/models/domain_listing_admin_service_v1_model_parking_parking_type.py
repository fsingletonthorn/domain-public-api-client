from enum import Enum


class DomainListingAdminServiceV1ModelParkingParkingType(str, Enum):
    NOPARKING = "noParking"
    ONSITE = "onSite"
    ONSTREET = "onStreet"

    def __str__(self) -> str:
        return str(self.value)
