from enum import Enum


class AddressLocatorsV1ApmIdModelLevel(str, Enum):
    ADDRESS = "Address"
    POSTCODE = "Postcode"
    STATE = "State"
    STREET = "Street"
    SUBURB = "Suburb"

    def __str__(self) -> str:
        return str(self.value)
