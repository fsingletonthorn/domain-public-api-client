from enum import Enum


class ListingAdminV2CommercialListingV2ContactPreference(str, Enum):
    BYPHONE = "byPhone"

    def __str__(self) -> str:
        return str(self.value)
