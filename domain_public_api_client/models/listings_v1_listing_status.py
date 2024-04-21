from enum import Enum


class ListingsV1ListingStatus(str, Enum):
    ARCHIVED = "archived"
    DEPOSITTAKEN = "depositTaken"
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
