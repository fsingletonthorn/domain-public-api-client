from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.properties_v1_claim_data_claimant import PropertiesV1ClaimDataClaimant
from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertiesV1ClaimData")


@_attrs_define
class PropertiesV1ClaimData:
    """DomainPropertyIdModelClaimsClaimData

    Attributes:
        claimant (Union[Unset, PropertiesV1ClaimDataClaimant]): Gets or Sets Claimant
    """

    claimant: Union[Unset, PropertiesV1ClaimDataClaimant] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        claimant: Union[Unset, str] = UNSET
        if not isinstance(self.claimant, Unset):
            claimant = self.claimant.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if claimant is not UNSET:
            field_dict["claimant"] = claimant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _claimant = d.pop("claimant", UNSET)
        claimant: Union[Unset, PropertiesV1ClaimDataClaimant]
        if isinstance(_claimant, Unset):
            claimant = UNSET
        else:
            claimant = PropertiesV1ClaimDataClaimant(_claimant)

        properties_v1_claim_data = cls(
            claimant=claimant,
        )

        return properties_v1_claim_data
