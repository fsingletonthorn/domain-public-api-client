from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsHiddenReasonsItem(str, Enum):
    BYAGENCY = "byAgency"
    QLDRESTRICTION = "qLDRestriction"

    def __str__(self) -> str:
        return str(self.value)
