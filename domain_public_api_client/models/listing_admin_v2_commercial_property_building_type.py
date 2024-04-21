from enum import Enum


class ListingAdminV2CommercialPropertyBuildingType(str, Enum):
    NA = "nA"
    PART = "part"
    WHOLE = "whole"

    def __str__(self) -> str:
        return str(self.value)
