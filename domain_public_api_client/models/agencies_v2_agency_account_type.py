from enum import Enum


class AgenciesV2AgencyAccountType(str, Enum):
    BUSINESS = "business"
    COMMERCIALFULL = "commercialFull"
    COMMERCIALLIGHT = "commercialLight"
    DEVELOPER = "developer"
    HOLIDAY = "holiday"
    NONE = "none"
    RESIDENTIAL = "residential"

    def __str__(self) -> str:
        return str(self.value)
