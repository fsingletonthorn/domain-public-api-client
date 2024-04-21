from enum import Enum


class DomainSearchServiceV2ModelDomainSearchContractsV2PropertyDetailsFeaturesItem(str, Enum):
    AIRCONDITIONING = "AirConditioning"
    ALARMSYSTEM = "AlarmSystem"
    BALCONYDECK = "BalconyDeck"
    BATH = "Bath"
    BROADBANDINTERNETACCESS = "BroadbandInternetAccess"
    BUILTINWARDROBES = "BuiltInWardrobes"
    CABLEORSATELLITE = "CableOrSatellite"
    CITYVIEWS = "CityViews"
    DISHWASHER = "Dishwasher"
    DOUBLEGLAZEDWINDOWS = "DoubleGlazedWindows"
    ENERGYEFFICIENTAPPLIANCES = "EnergyEfficientAppliances"
    ENSUITE = "Ensuite"
    FIREPLACE = "Fireplace"
    FLOORBOARDS = "Floorboards"
    FULLYFENCED = "FullyFenced"
    FURNISHED = "Furnished"
    GARDENCOURTYARD = "GardenCourtyard"
    GAS = "Gas"
    GREYWATERSYSTEM = "GreywaterSystem"
    GROUNDFLOOR = "GroundFloor"
    GYM = "Gym"
    HEATING = "Heating"
    INDOORSPA = "IndoorSpa"
    INTERCOM = "Intercom"
    INTERNALLAUNDRY = "InternalLaundry"
    NORTHFACING = "NorthFacing"
    OUTDOORSPA = "OutdoorSpa"
    PETSALLOWED = "PetsAllowed"
    RAINWATERSTORAGETANK = "RainwaterStorageTank"
    SECUREPARKING = "SecureParking"
    SEPARATEDININGROOM = "SeparateDiningRoom"
    SHED = "Shed"
    SOLARHOTWATER = "SolarHotWater"
    SOLARPANELS = "SolarPanels"
    STUDY = "Study"
    SWIMMINGPOOL = "SwimmingPool"
    TENNISCOURT = "TennisCourt"
    UNRECOGNISED = "Unrecognised"
    WALLCEILINGINSULATION = "WallCeilingInsulation"
    WATEREFFICIENTAPPLIANCES = "WaterEfficientAppliances"
    WATEREFFICIENTFIXTURES = "WaterEfficientFixtures"
    WATERVIEWS = "WaterViews"

    def __str__(self) -> str:
        return str(self.value)
