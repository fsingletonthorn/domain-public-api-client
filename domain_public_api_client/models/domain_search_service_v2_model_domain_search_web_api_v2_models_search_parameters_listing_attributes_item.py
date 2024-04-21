from enum import Enum


class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsSearchParametersListingAttributesItem(str, Enum):
    HASPHOTOS = "HasPhotos"
    HASPRICE = "HasPrice"
    MARKEDASNEW = "MarkedAsNew"
    NOTUNDERCONTRACT = "NotUnderContract"
    NOTUPFORAUCTION = "NotUpForAuction"

    def __str__(self) -> str:
        return str(self.value)
