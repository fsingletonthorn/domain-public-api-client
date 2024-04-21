from enum import Enum


class SchoolsV2SchoolCatchmentType(str, Enum):
    PRIMARY = "Primary"
    SECONDARY = "Secondary"

    def __str__(self) -> str:
        return str(self.value)
