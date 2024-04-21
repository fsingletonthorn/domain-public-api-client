from enum import Enum


class PropertiesV1ClaimDataClaimant(str, Enum):
    INVESTOR = "Investor"
    OWNER = "Owner"
    TENANT = "Tenant"
    UNSPECIFIED = "Unspecified"

    def __str__(self) -> str:
        return str(self.value)
