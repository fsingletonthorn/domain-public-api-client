from enum import Enum


class DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListingPromoLevel(str, Enum):
    ELITE = "Elite"
    ELITEPP = "ElitePP"
    PREMIUMPLUS = "PremiumPlus"
    STANDARD = "Standard"
    STANDARDPP = "StandardPP"

    def __str__(self) -> str:
        return str(self.value)
