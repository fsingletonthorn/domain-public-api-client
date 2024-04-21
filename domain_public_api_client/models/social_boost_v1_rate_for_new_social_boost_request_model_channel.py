from enum import Enum


class SocialBoostV1RateForNewSocialBoostRequestModelChannel(str, Enum):
    BUSINESS = "Business"
    COMMERCIAL = "Commercial"
    RESIDENTIAL = "Residential"

    def __str__(self) -> str:
        return str(self.value)
