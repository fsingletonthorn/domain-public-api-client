from enum import Enum


class ListingsV2ProjectAddressPartsDisplayType(str, Enum):
    AREAONLY = "areaOnly"
    FULLADDRESS = "fullAddress"
    REGIONONLY = "regionOnly"
    STATEONLY = "stateOnly"
    STREETANDSUBURB = "streetAndSuburb"
    SUBURBONLY = "suburbOnly"

    def __str__(self) -> str:
        return str(self.value)
