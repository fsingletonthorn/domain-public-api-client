from enum import Enum


class ListingAdminV2ParkingParkingType(str, Enum):
    NOPARKING = "noParking"
    ONSITE = "onSite"
    ONSTREET = "onStreet"

    def __str__(self) -> str:
        return str(self.value)
