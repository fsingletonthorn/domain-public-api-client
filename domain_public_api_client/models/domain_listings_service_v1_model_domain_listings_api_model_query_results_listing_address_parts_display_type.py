from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressPartsDisplayType(str, Enum):
    AREAONLY = "areaOnly"
    FULLADDRESS = "fullAddress"
    REGIONONLY = "regionOnly"
    STATEONLY = "stateOnly"
    STREETANDSUBURB = "streetAndSuburb"
    SUBURBONLY = "suburbOnly"

    def __str__(self) -> str:
        return str(self.value)
