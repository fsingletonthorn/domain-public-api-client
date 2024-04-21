from enum import Enum


class ListingsV2ProjectProjectProfileType(str, Enum):
    NOPROFILE = "noProfile"
    PROJECTPROFILEPREMIUM = "projectProfilePremium"
    PROJECTPROFILESTANDARD = "projectProfileStandard"

    def __str__(self) -> str:
        return str(self.value)
