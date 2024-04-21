from enum import Enum


class ListingsV1ListingSaleMode(str, Enum):
    ARCHIVED = "archived"
    BUY = "buy"
    LEASED = "leased"
    RENT = "rent"
    SHARE = "share"
    SOLD = "sold"

    def __str__(self) -> str:
        return str(self.value)
