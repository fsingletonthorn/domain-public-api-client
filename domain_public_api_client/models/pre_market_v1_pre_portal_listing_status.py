from enum import Enum


class PreMarketV1PrePortalListingStatus(str, Enum):
    DRAFT = "draft"
    LISTED = "listed"
    PREMARKET = "preMarket"
    SOLD = "sold"
    WITHDRAWN = "withdrawn"

    def __str__(self) -> str:
        return str(self.value)
