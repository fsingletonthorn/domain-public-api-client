from enum import Enum


class DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequestSort(str, Enum):
    DEFAULT = "default"
    HIGHTTOTALPRICEFIRST = "hightTotalPriceFirst"
    LOWTOTALPRICEFIRST = "lowTotalPriceFirst"
    NEWESTFIRST = "newestFirst"
    SUBURBASC = "suburbAsc"
    SUBURBDESC = "suburbDesc"

    def __str__(self) -> str:
        return str(self.value)
