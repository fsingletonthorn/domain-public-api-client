from enum import Enum


class ListingsV2AdvertiserIdentifiersAdvertiserType(str, Enum):
    AGENCY = "agency"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
