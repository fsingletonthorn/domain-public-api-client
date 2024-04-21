from enum import Enum


class SuburbPerformanceGetByNamedSuburbWithoutPostcodePropertyCategory(str, Enum):
    HOUSE = "house"
    UNIT = "unit"

    def __str__(self) -> str:
        return str(self.value)
