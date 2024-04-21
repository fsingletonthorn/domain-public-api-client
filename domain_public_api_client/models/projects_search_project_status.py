from enum import Enum


class ProjectsSearchProjectStatus(str, Enum):
    INACTIVE = "inActive"
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
