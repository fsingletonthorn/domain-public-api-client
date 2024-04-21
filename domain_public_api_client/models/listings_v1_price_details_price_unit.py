from enum import Enum


class ListingsV1PriceDetailsPriceUnit(str, Enum):
    PERSQM = "perSqm"
    TOTALAMOUNT = "totalAmount"

    def __str__(self) -> str:
        return str(self.value)
