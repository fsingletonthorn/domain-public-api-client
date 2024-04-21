from enum import Enum


class SocialBoostV1ListingRateInfoProductListingLevel(str, Enum):
    BRANDED = "Branded"
    GOLD = "Gold"
    NONE = "None"
    PLATINUM = "Platinum"
    PLATINUMEXTEND = "PlatinumExtend"
    SILVER = "Silver"
    TIER1 = "Tier1"
    TIER2 = "Tier2"
    TIER3 = "Tier3"

    def __str__(self) -> str:
        return str(self.value)
