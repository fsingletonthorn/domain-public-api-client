from enum import Enum


class DomainListingAdminServiceV1ModelResidentialListingContactPreference(str, Enum):
    BYPHONE = "byPhone"

    def __str__(self) -> str:
        return str(self.value)
