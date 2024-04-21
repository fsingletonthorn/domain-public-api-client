from enum import Enum


class ListingsV2SaleDetailsSaleMethod(str, Enum):
    AUCTION = "auction"
    EXPRESSIONOFINTEREST = "expressionOfInterest"
    NOTSTATED = "notStated"
    PRIVATETREATY = "privateTreaty"
    TENDER = "tender"

    def __str__(self) -> str:
        return str(self.value)
