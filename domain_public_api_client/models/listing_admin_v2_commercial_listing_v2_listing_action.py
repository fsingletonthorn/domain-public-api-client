from enum import Enum


class ListingAdminV2CommercialListingV2ListingAction(str, Enum):
    RENT = "rent"
    SALE = "sale"
    SALEANDLEASE = "saleAndLease"

    def __str__(self) -> str:
        return str(self.value)
