from enum import Enum


class ListingsV1InspectionRecurrence(str, Enum):
    NONE = "none"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
