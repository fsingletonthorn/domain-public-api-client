from enum import Enum


class ListingAdminV2CommercialOffMarketPropertyPropertyTypeItem(str, Enum):
    AQUACULTURE = "aquaculture"
    CROPPING = "cropping"
    DAIRYFARMING = "dairyFarming"
    DEVELOPMENTLAND = "developmentLand"
    EQUINE = "equine"
    FARMLET = "farmlet"
    FISHINGFORESTRY = "fishingForestry"
    GRAZING = "grazing"
    HORTICULTURE = "horticulture"
    HOTELLEISURE = "hotelLeisure"
    INDUSTRIALWAREHOUSE = "industrialWarehouse"
    INTERNATIONALCOMMERCIAL = "internationalCommercial"
    IRRIGATIONSERVICES = "irrigationServices"
    LIVESTOCK = "livestock"
    MEDICALCONSULTING = "medicalConsulting"
    MIXEDFARMING = "mixedFarming"
    OFFICES = "offices"
    ORCHARD = "orchard"
    OTHER = "other"
    PARKINGCARSPACE = "parkingCarSpace"
    RETAIL = "retail"
    RURALCOMMERCIALFARMING = "ruralCommercialFarming"
    RURALLIFESTYLE = "ruralLifestyle"
    SERVICEDOFFICES = "servicedOffices"
    SHOWROOMSBULKYGOODS = "showroomsBulkyGoods"
    VITICULTURE = "viticulture"

    def __str__(self) -> str:
        return str(self.value)
