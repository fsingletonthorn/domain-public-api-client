from enum import Enum


class DomainSearchServiceV2ModelDomainSearchContractsV2SoldDataSource(str, Enum):
    AGENCY = "Agency"
    APM = "Apm"

    def __str__(self) -> str:
        return str(self.value)
