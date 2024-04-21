from enum import Enum


class ListingsV1SoldDetailsSoldAction(str, Enum):
    AUCTION = "auction"
    NOTSTATED = "notStated"
    PRIVATETREATY = "privateTreaty"
    SOLDPRIORTOAUCTION = "soldPriorToAuction"
    WITHDRAWN = "withdrawn"

    def __str__(self) -> str:
        return str(self.value)
