from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsPriceUnit(str, Enum):
    PERSQM = "perSqm"
    TOTALAMOUNT = "totalAmount"

    def __str__(self) -> str:
        return str(self.value)
