from enum import Enum


class ListingsV2InspectionRecurrence(str, Enum):
    NONE = "none"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
