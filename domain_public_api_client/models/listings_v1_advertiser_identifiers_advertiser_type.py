from enum import Enum


class ListingsV1AdvertiserIdentifiersAdvertiserType(str, Enum):
    AGENCY = "agency"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
