from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetailsSource(str, Enum):
    EXTERNAL = "external"
    INTERNAL = "internal"

    def __str__(self) -> str:
        return str(self.value)
