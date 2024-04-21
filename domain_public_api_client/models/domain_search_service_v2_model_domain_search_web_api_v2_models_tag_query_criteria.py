from enum import Enum


class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQueryCriteria(str, Enum):
    EXCLUDE = "Exclude"
    INCLUDE = "Include"

    def __str__(self) -> str:
        return str(self.value)
