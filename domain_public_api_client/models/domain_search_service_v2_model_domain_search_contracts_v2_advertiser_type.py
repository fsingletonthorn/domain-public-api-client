from enum import Enum


class DomainSearchServiceV2ModelDomainSearchContractsV2AdvertiserType(str, Enum):
    AGENCY = "Agency"
    PRIVATE = "Private"

    def __str__(self) -> str:
        return str(self.value)
