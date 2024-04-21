from enum import Enum


class DomainSearchServiceV2ModelDomainSearchContractsV2SearchResultType(str, Enum):
    PROJECT = "Project"
    PROPERTYLISTING = "PropertyListing"

    def __str__(self) -> str:
        return str(self.value)
