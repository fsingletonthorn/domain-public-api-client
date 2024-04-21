from enum import Enum


class ListingAdminV2SpecificUnitDetailPriceUnit(str, Enum):
    PERSQM = "perSqm"
    TOTALAMOUNT = "totalAmount"

    def __str__(self) -> str:
        return str(self.value)
