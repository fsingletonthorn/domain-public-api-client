from enum import Enum


class ListingAdminV2CommercialListingV2OccupancyType(str, Enum):
    TENANTED = "tenanted"
    VACANT = "vacant"

    def __str__(self) -> str:
        return str(self.value)
