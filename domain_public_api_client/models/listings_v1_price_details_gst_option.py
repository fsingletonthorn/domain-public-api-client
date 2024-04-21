from enum import Enum


class ListingsV1PriceDetailsGstOption(str, Enum):
    EX = "ex"
    INC = "inc"
    NA = "na"

    def __str__(self) -> str:
        return str(self.value)
