from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressPartsStateAbbreviation(str, Enum):
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
