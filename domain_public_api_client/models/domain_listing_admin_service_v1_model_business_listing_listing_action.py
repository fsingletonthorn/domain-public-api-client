from enum import Enum


class DomainListingAdminServiceV1ModelBusinessListingListingAction(str, Enum):
    RENT = "rent"
    SALE = "sale"
    SALEANDLEASE = "saleAndLease"

    def __str__(self) -> str:
        return str(self.value)
