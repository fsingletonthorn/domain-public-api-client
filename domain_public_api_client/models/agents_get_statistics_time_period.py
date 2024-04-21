from enum import Enum


class AgentsGetStatisticsTimePeriod(str, Enum):
    LAST7DAYS = "last7Days"
    LAST90DAYS = "last90Days"
    WHOLECAMPAIGN = "wholeCampaign"

    def __str__(self) -> str:
        return str(self.value)
