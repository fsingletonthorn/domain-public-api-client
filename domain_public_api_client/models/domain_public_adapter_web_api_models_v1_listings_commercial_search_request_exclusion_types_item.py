from enum import Enum


class DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestExclusionTypesItem(str, Enum):
    SURROUNDINGSUBURBS = "surroundingSuburbs"
    WITHOUTPRICE = "withoutPrice"

    def __str__(self) -> str:
        return str(self.value)
