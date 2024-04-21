from enum import Enum


class BookingsV2RateForNewListingRequestListingType(str, Enum):
    RENT = "rent"
    SALE = "sale"

    def __str__(self) -> str:
        return str(self.value)
