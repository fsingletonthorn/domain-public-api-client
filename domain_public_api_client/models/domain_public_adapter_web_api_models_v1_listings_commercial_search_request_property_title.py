from enum import Enum


class DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestPropertyTitle(str, Enum):
    FREEHOLD = "freehold"
    NOBUILDING = "noBuilding"
    STRATA = "strata"

    def __str__(self) -> str:
        return str(self.value)
