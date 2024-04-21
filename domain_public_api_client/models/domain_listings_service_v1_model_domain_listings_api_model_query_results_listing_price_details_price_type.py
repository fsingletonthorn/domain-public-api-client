from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsPriceType(str, Enum):
    GROSS = "gross"
    NET = "net"

    def __str__(self) -> str:
        return str(self.value)
