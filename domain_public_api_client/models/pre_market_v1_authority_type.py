from enum import Enum


class PreMarketV1AuthorityType(str, Enum):
    AUCTION = "auction"
    EXPRESSIONOFINTEREST = "expressionOfInterest"
    PRIVATESALE = "privateSale"

    def __str__(self) -> str:
        return str(self.value)
