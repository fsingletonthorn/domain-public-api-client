from enum import Enum


class ListingAdminV2SoldDetailsSoldType(str, Enum):
    AUCTION = "auction"
    PRIORTOAUCTION = "priorToAuction"
    PRIVATETREATY = "privateTreaty"

    def __str__(self) -> str:
        return str(self.value)
