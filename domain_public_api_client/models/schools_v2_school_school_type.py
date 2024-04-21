from enum import Enum


class SchoolsV2SchoolSchoolType(str, Enum):
    COMBINED = "Combined"
    PRIMARY = "Primary"
    SECONDARY = "Secondary"
    SPECIAL = "Special"

    def __str__(self) -> str:
        return str(self.value)
