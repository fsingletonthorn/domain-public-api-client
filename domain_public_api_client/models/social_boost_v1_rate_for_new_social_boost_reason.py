from enum import Enum


class SocialBoostV1RateForNewSocialBoostReason(str, Enum):
    BASEDONCONTRACT = "BasedOnContract"
    NOCONTRACTFOUND = "NoContractFound"
    NORATEFOUND = "NoRateFound"
    PROPERTYTYPEEXCLUDED = "PropertyTypeExcluded"

    def __str__(self) -> str:
        return str(self.value)
