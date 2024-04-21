from enum import Enum


class ListingsV2ProjectCategory(str, Enum):
    APARTMENT = "apartment"
    HOUSEANDLAND = "houseAndLand"
    RETIREMENT = "retirement"

    def __str__(self) -> str:
        return str(self.value)
