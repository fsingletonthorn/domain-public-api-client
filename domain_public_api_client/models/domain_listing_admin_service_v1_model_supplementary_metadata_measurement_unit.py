from enum import Enum


class DomainListingAdminServiceV1ModelSupplementaryMetadataMeasurementUnit(str, Enum):
    DSE = "dse"
    HECTARES = "hectares"
    MILLIMETRES = "millimetres"
    SQUAREMETRES = "squareMetres"

    def __str__(self) -> str:
        return str(self.value)
