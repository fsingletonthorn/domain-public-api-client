from enum import Enum


class SchoolsV2SchoolSchoolSector(str, Enum):
    CATHOLIC = "Catholic"
    GOVERNMENT = "Government"
    INDEPENDENT = "Independent"

    def __str__(self) -> str:
        return str(self.value)
