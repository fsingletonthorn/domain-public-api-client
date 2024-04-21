from enum import Enum


class DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListingListingType(str, Enum):
    NEWHOMES = "NewHomes"
    RENT = "Rent"
    SALE = "Sale"
    SHARE = "Share"
    SOLD = "Sold"

    def __str__(self) -> str:
        return str(self.value)
