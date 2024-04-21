from enum import Enum


class DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestSearchMode(str, Enum):
    FORSALE = "forSale"
    FRANCHISEBRAND = "franchiseBrand"
    FRANCHISEOPPORTUNITY = "franchiseOpportunity"

    def __str__(self) -> str:
        return str(self.value)
