from enum import Enum


class ListingsV2PriceDetailsHiddenReasonsType0Item(str, Enum):
    BYAGENCY = "byAgency"
    QLDRESTRICTION = "qldRestriction"

    def __str__(self) -> str:
        return str(self.value)
