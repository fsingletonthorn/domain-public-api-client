from enum import Enum


class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetailsSource(str, Enum):
    EXTERNAL = "external"
    INTERNAL = "internal"

    def __str__(self) -> str:
        return str(self.value)
