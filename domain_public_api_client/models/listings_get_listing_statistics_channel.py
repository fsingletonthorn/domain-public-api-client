from enum import Enum


class ListingsGetListingStatisticsChannel(str, Enum):
    BUSINESS = "business"
    COMMERCIAL = "commercial"
    RESIDENTIAL = "residential"

    def __str__(self) -> str:
        return str(self.value)
