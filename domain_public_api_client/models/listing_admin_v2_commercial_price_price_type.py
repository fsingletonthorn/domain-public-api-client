from enum import Enum


class ListingAdminV2CommercialPricePriceType(str, Enum):
    GROSS = "gross"
    NET = "net"

    def __str__(self) -> str:
        return str(self.value)
