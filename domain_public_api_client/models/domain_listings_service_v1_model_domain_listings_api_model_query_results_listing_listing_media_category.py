from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMediaCategory(str, Enum):
    IMAGE = "image"
    OTHERS = "others"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
