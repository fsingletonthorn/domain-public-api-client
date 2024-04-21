from enum import Enum


class ListingAdminV2SpecificUnitDetailOccupancy(str, Enum):
    TENANTED = "tenanted"
    VACANT = "vacant"

    def __str__(self) -> str:
        return str(self.value)
