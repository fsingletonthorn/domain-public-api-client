from enum import Enum


class DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearchType(str, Enum):
    PERSQM = "perSqm"
    TOTALAMOUNT = "totalAmount"

    def __str__(self) -> str:
        return str(self.value)
