from enum import Enum


class PropertyImagesGetState(str, Enum):
    ACT = "ACT"
    NSW = "NSW"
    NT = "NT"
    OT = "OT"
    QLD = "QLD"
    SA = "SA"
    TAS = "TAS"
    VIC = "VIC"
    WA = "WA"

    def __str__(self) -> str:
        return str(self.value)
