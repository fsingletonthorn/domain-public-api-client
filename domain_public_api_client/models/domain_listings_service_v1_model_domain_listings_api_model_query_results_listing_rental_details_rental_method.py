from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetailsRentalMethod(str, Enum):
    HOLIDAY = "holiday"
    LEASE = "lease"
    NOTSTATED = "notStated"
    RENT = "rent"
    SHARE = "share"

    def __str__(self) -> str:
        return str(self.value)
