from enum import Enum


class DomainPublicAdapterWebApiModelsV1ListingsListingStatus(str, Enum):
    ARCHIVED = "archived"
    LEASED = "leased"
    LIVE = "live"
    NEW = "new"
    NEWDEVELOPMENT = "newDevelopment"
    PENDING = "pending"
    RECENTLYUPDATED = "recentlyUpdated"
    SOLD = "sold"
    UNDEROFFER = "underOffer"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
