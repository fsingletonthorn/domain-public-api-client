from enum import Enum


class SocialBoostV1RateForNewSocialBoostRequestModelPropertyType(str, Enum):
    ACREAGESEMIRURAL = "AcreageSemiRural"
    APARTMENTUNITFLAT = "ApartmentUnitFlat"
    AQUACULTURE = "Aquaculture"
    BLOCKOFUNITS = "BlockOfUnits"
    CARSPACE = "Carspace"
    CROPPING = "Cropping"
    DAIRYFARMING = "DairyFarming"
    DEVELOPMENTSITE = "DevelopmentSite"
    DUPLEX = "Duplex"
    EQUINE = "Equine"
    FARM = "Farm"
    FARMLET = "Farmlet"
    FISHINGFORESTRY = "FishingForestry"
    GRAZING = "Grazing"
    HORTICULTURE = "Horticulture"
    HOUSE = "House"
    IRRIGATIONSERVICES = "IrrigationServices"
    LIVESTOCK = "Livestock"
    MIXEDFARMING = "MixedFarming"
    NEWAPARTMENTS = "NewApartments"
    NEWHOMEDESIGNS = "NewHomeDesigns"
    NEWHOUSELAND = "NewHouseLand"
    NEWLAND = "NewLand"
    ORCHARD = "Orchard"
    PENTHOUSE = "Penthouse"
    RETIREMENT = "Retirement"
    RETIREMENTVILLAGE = "RetirementVillage"
    RURAL = "Rural"
    RURALLIFESTYLE = "RuralLifestyle"
    SEMIDETACHED = "SemiDetached"
    SPECIALISTFARM = "SpecialistFarm"
    STUDIO = "Studio"
    TERRACE = "Terrace"
    TOWNHOUSE = "Townhouse"
    UNKNOWN = "Unknown"
    VACANTLAND = "VacantLand"
    VILLA = "Villa"
    VITICULTURE = "Viticulture"

    def __str__(self) -> str:
        return str(self.value)
