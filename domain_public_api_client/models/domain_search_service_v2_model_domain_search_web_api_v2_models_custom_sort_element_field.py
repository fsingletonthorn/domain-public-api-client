from enum import Enum


class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElementField(str, Enum):
    ADID = "AdId"
    DATEAVAILABLE = "DateAvailable"
    DATELISTED = "DateListed"
    DATEUPDATED = "DateUpdated"
    EARLIESTAUCTIONTIME = "EarliestAuctionTime"
    EARLIESTINSPECTIONOPENTIME = "EarliestInspectionOpenTime"
    FRESHNESSLEVEL = "FreshnessLevel"
    PRICE = "Price"
    PRICEDISPLAYOPTION = "PriceDisplayOption"
    PRODUCTBOOST = "ProductBoost"
    PROMOLEVELSCORE = "PromoLevelScore"
    SOLDDATE = "SoldDate"
    SUBURBNAME = "SuburbName"

    def __str__(self) -> str:
        return str(self.value)
