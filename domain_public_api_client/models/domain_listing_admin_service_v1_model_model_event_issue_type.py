from enum import Enum


class DomainListingAdminServiceV1ModelModelEventIssueType(str, Enum):
    EXTERNAL = "External"
    INTERNAL = "Internal"

    def __str__(self) -> str:
        return str(self.value)
