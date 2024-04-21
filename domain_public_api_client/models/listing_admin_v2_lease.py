from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2Lease")


@_attrs_define
class ListingAdminV2Lease:
    """Properties for lease listings

    Attributes:
        term_of_lease_from (Union[Unset, int]): Integer value of lease term range from
        term_of_lease_to (Union[Unset, int]): Integer value of lease term range to
        lease_outgoings (Union[Unset, int]): Outgoing cost of current lease
    """

    term_of_lease_from: Union[Unset, int] = UNSET
    term_of_lease_to: Union[Unset, int] = UNSET
    lease_outgoings: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        term_of_lease_from = self.term_of_lease_from

        term_of_lease_to = self.term_of_lease_to

        lease_outgoings = self.lease_outgoings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term_of_lease_from is not UNSET:
            field_dict["termOfLeaseFrom"] = term_of_lease_from
        if term_of_lease_to is not UNSET:
            field_dict["termOfLeaseTo"] = term_of_lease_to
        if lease_outgoings is not UNSET:
            field_dict["leaseOutgoings"] = lease_outgoings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        term_of_lease_from = d.pop("termOfLeaseFrom", UNSET)

        term_of_lease_to = d.pop("termOfLeaseTo", UNSET)

        lease_outgoings = d.pop("leaseOutgoings", UNSET)

        listing_admin_v2_lease = cls(
            term_of_lease_from=term_of_lease_from,
            term_of_lease_to=term_of_lease_to,
            lease_outgoings=lease_outgoings,
        )

        listing_admin_v2_lease.additional_properties = d
        return listing_admin_v2_lease

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
