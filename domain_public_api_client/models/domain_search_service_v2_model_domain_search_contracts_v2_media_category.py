from enum import Enum


class DomainSearchServiceV2ModelDomainSearchContractsV2MediaCategory(str, Enum):
    IMAGE = "Image"

    def __str__(self) -> str:
        return str(self.value)
