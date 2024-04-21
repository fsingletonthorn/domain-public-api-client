from enum import Enum


class DomainPublicAdapterWebApiModelsV1ListingsListingObjective(str, Enum):
    RENT = "rent"
    SALE = "sale"

    def __str__(self) -> str:
        return str(self.value)
