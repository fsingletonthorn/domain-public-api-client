from enum import Enum


class SocialBoostV1RateForNewSocialBoostRequestModelListingType(str, Enum):
    NONE = "None"
    RENT = "Rent"
    SALE = "Sale"

    def __str__(self) -> str:
        return str(self.value)
