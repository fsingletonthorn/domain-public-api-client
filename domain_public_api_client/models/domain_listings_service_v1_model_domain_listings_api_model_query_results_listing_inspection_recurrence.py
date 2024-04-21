from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspectionRecurrence(str, Enum):
    NONE = "none"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
