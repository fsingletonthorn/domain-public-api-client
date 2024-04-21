from enum import Enum


class ListingAdminV2CommercialPriceGstOptionType(str, Enum):
    EX = "ex"
    INC = "inc"
    NA = "nA"

    def __str__(self) -> str:
        return str(self.value)
