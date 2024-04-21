from enum import Enum


class SocialBoostV1ListingRateInfoProductListingRule(str, Enum):
    EARLYACCESS = "EarlyAccess"
    NONE = "None"
    SOCIALBOOSTAGENT = "SocialBoostAgent"
    SOCIALBOOSTALL = "SocialBoostAll"
    SOCIALBOOSTCASUAL = "SocialBoostCasual"
    SOCIALBOOSTRURALAGENT = "SocialBoostRuralAgent"
    SOCIALBOOSTRURALALL = "SocialBoostRuralAll"
    SOCIALBOOSTRURALCASUAL = "SocialBoostRuralCasual"

    def __str__(self) -> str:
        return str(self.value)
