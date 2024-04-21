from enum import Enum


class ListingsV2ListingMediaCategory(str, Enum):
    IMAGE = "image"
    OTHERS = "others"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
