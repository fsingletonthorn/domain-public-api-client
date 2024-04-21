from enum import Enum


class DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsState(str, Enum):
    ACT = "ACT"
    NSW = "NSW"
    NT = "NT"
    QLD = "QLD"
    SA = "SA"
    TAS = "TAS"
    VIC = "VIC"
    WA = "WA"

    def __str__(self) -> str:
        return str(self.value)
