from enum import Enum


class DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequestSort(str, Enum):
    BUILDINGSIZEASC = "buildingSizeAsc"
    BUILDINGSIZEDESC = "buildingSizeDesc"
    CHEAPESTPERSQMFIRST = "cheapestPerSqmFirst"
    CHEAPESTTOTALFIRST = "cheapestTotalFirst"
    DEFAULT = "default"
    MOSTEXPENSIVEPERSQMFIRST = "mostExpensivePerSqmFirst"
    MOSTEXPENSIVETOTALFIRST = "mostExpensiveTotalFirst"
    NEWESTFIRST = "newestFirst"
    SUBURBASC = "suburbAsc"
    SUBURBDESC = "suburbDesc"

    def __str__(self) -> str:
        return str(self.value)
