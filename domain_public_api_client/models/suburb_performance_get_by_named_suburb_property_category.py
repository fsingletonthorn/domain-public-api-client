from enum import Enum


class SuburbPerformanceGetByNamedSuburbPropertyCategory(str, Enum):
    HOUSE = "house"
    UNIT = "unit"

    def __str__(self) -> str:
        return str(self.value)
