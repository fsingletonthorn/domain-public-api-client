from enum import Enum


class AddressLocatorsV1AddressComponentsComponent(str, Enum):
    POSTCODE = "Postcode"
    STATE = "State"
    STREETNAME = "StreetName"
    STREETNUMBER = "StreetNumber"
    STREETTYPE = "StreetType"
    SUBURB = "Suburb"
    UNITNUMBER = "UnitNumber"

    def __str__(self) -> str:
        return str(self.value)
