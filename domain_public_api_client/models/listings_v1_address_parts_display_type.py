from enum import Enum


class ListingsV1AddressPartsDisplayType(str, Enum):
    AREAONLY = "areaOnly"
    FULLADDRESS = "fullAddress"
    REGIONONLY = "regionOnly"
    STATEONLY = "stateOnly"
    STREETANDSUBURB = "streetAndSuburb"
    SUBURBONLY = "suburbOnly"

    def __str__(self) -> str:
        return str(self.value)
