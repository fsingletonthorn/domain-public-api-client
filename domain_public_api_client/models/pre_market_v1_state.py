from enum import Enum


class PreMarketV1State(str, Enum):
    ACT = "act"
    NSW = "nsw"
    NT = "nt"
    QLD = "qld"
    SA = "sa"
    TAS = "tas"
    VIC = "vic"
    WA = "wa"

    def __str__(self) -> str:
        return str(self.value)
