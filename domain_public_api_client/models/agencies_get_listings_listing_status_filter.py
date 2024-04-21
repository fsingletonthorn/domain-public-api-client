from enum import Enum


class AgenciesGetListingsListingStatusFilter(str, Enum):
    LIVE = "live"
    LIVEANDARCHIVED = "liveAndArchived"

    def __str__(self) -> str:
        return str(self.value)
