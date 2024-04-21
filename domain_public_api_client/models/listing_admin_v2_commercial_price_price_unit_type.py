from enum import Enum


class ListingAdminV2CommercialPricePriceUnitType(str, Enum):
    PERSQM = "perSqm"
    TOTALAMOUNT = "totalAmount"

    def __str__(self) -> str:
        return str(self.value)
