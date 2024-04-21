from enum import Enum


class PropertiesV1PropertyStatus(str, Enum):
    OFFMARKET = "OffMarket"
    ONMARKET = "OnMarket"

    def __str__(self) -> str:
        return str(self.value)
