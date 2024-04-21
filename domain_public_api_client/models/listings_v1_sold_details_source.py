from enum import Enum


class ListingsV1SoldDetailsSource(str, Enum):
    EXTERNAL = "external"
    INTERNAL = "internal"

    def __str__(self) -> str:
        return str(self.value)
