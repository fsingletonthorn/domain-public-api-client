from enum import Enum


class ListingsV2ProjectEstimatedCompletionTertile(str, Enum):
    EARLY = "early"
    LATE = "late"
    MID = "mid"

    def __str__(self) -> str:
        return str(self.value)
