from enum import Enum


class SuburbPerformanceGetByNamedSuburbPeriodSize(str, Enum):
    HALFYEARS = "halfYears"
    QUARTERS = "quarters"
    YEARS = "years"

    def __str__(self) -> str:
        return str(self.value)
