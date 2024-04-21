from enum import Enum


class DomainListingAdminServiceV1ModelResidentialListingLifeStyleType(str, Enum):
    FIRSTHOME = "firstHome"
    INVESTMENT = "investment"
    RETIREMENT = "retirement"
    SEACHANGE = "seaChange"
    TREECHANGE = "treeChange"
    YOUNGFAMILIES = "youngFamilies"

    def __str__(self) -> str:
        return str(self.value)
