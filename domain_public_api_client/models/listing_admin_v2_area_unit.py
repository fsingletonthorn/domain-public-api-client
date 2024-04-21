from enum import Enum


class ListingAdminV2AreaUnit(str, Enum):
    ACRES = "acres"
    HECTARES = "hectares"
    SQUAREFEET = "squareFeet"
    SQUAREMETRES = "squareMetres"
    SQUARES = "squares"
    SQUAREYARDS = "squareYards"

    def __str__(self) -> str:
        return str(self.value)
