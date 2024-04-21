from enum import Enum


class ListingsV2ListingObjective(str, Enum):
    RENT = "rent"
    SALE = "sale"

    def __str__(self) -> str:
        return str(self.value)
