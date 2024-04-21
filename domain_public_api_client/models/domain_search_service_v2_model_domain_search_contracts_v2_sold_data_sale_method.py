from enum import Enum


class DomainSearchServiceV2ModelDomainSearchContractsV2SoldDataSaleMethod(str, Enum):
    NOTSTATED = "NotStated"
    SOLDBYAUCTION = "SoldByAuction"
    SOLDBYPRIVATETREATY = "SoldByPrivateTreaty"
    SOLDPRIORTOAUCTION = "SoldPriorToAuction"
    WITHDRAWN = "Withdrawn"

    def __str__(self) -> str:
        return str(self.value)
