from enum import Enum


class DomainListingAdminServiceV1ModelAddressDisplayOption(str, Enum):
    AREAONLY = "areaOnly"
    FULLADDRESS = "fullAddress"
    REGIONONLY = "regionOnly"
    STATEONLY = "stateOnly"
    STREETANDSUBURB = "streetAndSuburb"
    SUBURBONLY = "suburbOnly"
    UNSPECIFIED = "unspecified"

    def __str__(self) -> str:
        return str(self.value)
