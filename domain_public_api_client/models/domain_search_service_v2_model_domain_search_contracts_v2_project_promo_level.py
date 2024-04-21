from enum import Enum


class DomainSearchServiceV2ModelDomainSearchContractsV2ProjectPromoLevel(str, Enum):
    PREMIUM = "Premium"
    STANDARD = "Standard"

    def __str__(self) -> str:
        return str(self.value)
