from enum import Enum


class ListingsBypropertyidSaleMode(str, Enum):
    BOTH = "both"
    RENT = "rent"
    SALE = "sale"

    def __str__(self) -> str:
        return str(self.value)
