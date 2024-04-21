from enum import Enum


class PropertiesV1AdvertOnMarketTypesType0Item(str, Enum):
    RENT = "Rent"
    SALE = "Sale"
    SHARE = "Share"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
