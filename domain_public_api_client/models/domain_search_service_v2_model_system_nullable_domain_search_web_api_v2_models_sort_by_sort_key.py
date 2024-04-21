from enum import Enum


class DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBySortKey(str, Enum):
    AUCTIONTIME = "AuctionTime"
    DATEAVAILABLE = "DateAvailable"
    DATELISTED = "DateListed"
    DATEUPDATED = "DateUpdated"
    DEFAULT = "Default"
    DEFAULTTHENDATEUPDATED = "DefaultThenDateUpdated"
    INSPECTIONTIME = "InspectionTime"
    PRICE = "Price"
    PROXIMITY = "Proximity"
    SOLDDATE = "SoldDate"
    SUBURB = "Suburb"

    def __str__(self) -> str:
        return str(self.value)
