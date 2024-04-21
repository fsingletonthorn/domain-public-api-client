from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2LeasedDetails")


@_attrs_define
class ListingAdminV2LeasedDetails:
    """Leased Details

    Attributes:
        leased_price (Union[Unset, int]): Optional. The weekly rental price.
        leased_duration (Union[Unset, int]): The duration of the lease in weeks.
    """

    leased_price: Union[Unset, int] = UNSET
    leased_duration: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        leased_price = self.leased_price

        leased_duration = self.leased_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if leased_price is not UNSET:
            field_dict["leasedPrice"] = leased_price
        if leased_duration is not UNSET:
            field_dict["leasedDuration"] = leased_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        leased_price = d.pop("leasedPrice", UNSET)

        leased_duration = d.pop("leasedDuration", UNSET)

        listing_admin_v2_leased_details = cls(
            leased_price=leased_price,
            leased_duration=leased_duration,
        )

        listing_admin_v2_leased_details.additional_properties = d
        return listing_admin_v2_leased_details

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
