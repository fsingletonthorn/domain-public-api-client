from enum import Enum


class ListingAdminV2BusinessOffMarketListingListingAction(str, Enum):
    RENT = "rent"
    SALE = "sale"

    def __str__(self) -> str:
        return str(self.value)
