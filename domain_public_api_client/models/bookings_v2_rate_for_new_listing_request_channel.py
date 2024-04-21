from enum import Enum


class BookingsV2RateForNewListingRequestChannel(str, Enum):
    BUSINESS = "business"
    COMMERCIAL = "commercial"
    RESIDENTIAL = "residential"

    def __str__(self) -> str:
        return str(self.value)
