from enum import Enum


class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersPropertyEstablishedType(str, Enum):
    ANY = "Any"
    ESTABLISHED = "Established"
    NEW = "New"

    def __str__(self) -> str:
        return str(self.value)
