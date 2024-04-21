from enum import Enum


class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElementDirection(str, Enum):
    ASCENDING = "Ascending"
    DESCENDING = "Descending"

    def __str__(self) -> str:
        return str(self.value)
