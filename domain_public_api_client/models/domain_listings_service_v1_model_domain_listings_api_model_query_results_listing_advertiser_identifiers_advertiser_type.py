from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiersAdvertiserType(
    str, Enum
):
    AGENCY = "agency"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
