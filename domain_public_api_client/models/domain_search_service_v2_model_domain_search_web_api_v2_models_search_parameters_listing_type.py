from enum import Enum


class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersListingType(str, Enum):
    NEWHOMES = "NewHomes"
    RENT = "Rent"
    SALE = "Sale"
    SHARE = "Share"
    SOLD = "Sold"

    def __str__(self) -> str:
        return str(self.value)
