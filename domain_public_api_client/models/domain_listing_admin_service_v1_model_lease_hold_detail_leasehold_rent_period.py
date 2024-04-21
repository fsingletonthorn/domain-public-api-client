from enum import Enum


class DomainListingAdminServiceV1ModelLeaseHoldDetailLeaseholdRentPeriod(str, Enum):
    PERANNUM = "perAnnum"
    PERMONTH = "perMonth"

    def __str__(self) -> str:
        return str(self.value)
