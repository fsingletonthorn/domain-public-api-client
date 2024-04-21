from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsGstOption(str, Enum):
    EX = "ex"
    INC = "inc"
    NA = "na"

    def __str__(self) -> str:
        return str(self.value)
