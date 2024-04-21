from enum import Enum


class DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSearchMode(str, Enum):
    FORLEASE = "forLease"
    FORSALE = "forSale"
    LEASED = "leased"
    SOLD = "sold"

    def __str__(self) -> str:
        return str(self.value)
