from enum import Enum


class DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSaleType(str, Enum):
    AUCTION = "auction"
    EXPRESSIONOFINTEREST = "expressionOfInterest"
    STANDARDSALE = "standardSale"
    TENDER = "tender"

    def __str__(self) -> str:
        return str(self.value)
