from enum import Enum


class PropertyEnrichmentV2PropertyActivitySummaryV2OwnerRenter(str, Enum):
    OWNER = "owner"
    RENTER = "renter"

    def __str__(self) -> str:
        return str(self.value)
