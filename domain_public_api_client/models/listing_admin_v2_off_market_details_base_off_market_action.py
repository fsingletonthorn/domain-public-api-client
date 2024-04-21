from enum import Enum


class ListingAdminV2OffMarketDetailsBaseOffMarketAction(str, Enum):
    LEASED = "leased"
    SOLD = "sold"
    WITHDRAWN = "withDrawn"

    def __str__(self) -> str:
        return str(self.value)
