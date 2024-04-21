from enum import Enum


class ListingsV1PriceDetailsPriceType(str, Enum):
    GROSS = "gross"
    NET = "net"

    def __str__(self) -> str:
        return str(self.value)
