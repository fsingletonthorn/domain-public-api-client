from enum import Enum


class SchoolsV2SchoolGender(str, Enum):
    BOYS = "Boys"
    COED = "CoEd"
    GIRLS = "Girls"

    def __str__(self) -> str:
        return str(self.value)
