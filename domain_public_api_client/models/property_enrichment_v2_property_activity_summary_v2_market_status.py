from enum import Enum


class PropertyEnrichmentV2PropertyActivitySummaryV2MarketStatus(str, Enum):
    OFF_MARKET = "off-market"
    ON_MARKET = "on-market"

    def __str__(self) -> str:
        return str(self.value)
