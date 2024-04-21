from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listing_admin_service_v1_model_past_sale_address_state import (
    DomainListingAdminServiceV1ModelPastSaleAddressState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelPastSaleAddress")


@_attrs_define
class DomainListingAdminServiceV1ModelPastSaleAddress:
    """Address for past sold listing

    Attributes:
        state (Union[Unset, DomainListingAdminServiceV1ModelPastSaleAddressState]): State
        unit_number (Union[Unset, str]): Unit number for apartments, maximum 30 characters
        street_number (Union[Unset, str]): Street number, maximum 20 characters
        street (Union[Unset, str]): Street name, maximum 100 characters
        suburb (Union[Unset, str]): Suburb name , maximum 50 characters
        postcode (Union[Unset, str]): Postcode
    """

    state: Union[Unset, DomainListingAdminServiceV1ModelPastSaleAddressState] = UNSET
    unit_number: Union[Unset, str] = UNSET
    street_number: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    suburb: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        unit_number = self.unit_number

        street_number = self.street_number

        street = self.street

        suburb = self.suburb

        postcode = self.postcode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if street is not UNSET:
            field_dict["street"] = street
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if postcode is not UNSET:
            field_dict["postcode"] = postcode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, DomainListingAdminServiceV1ModelPastSaleAddressState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DomainListingAdminServiceV1ModelPastSaleAddressState(_state)

        unit_number = d.pop("unitNumber", UNSET)

        street_number = d.pop("streetNumber", UNSET)

        street = d.pop("street", UNSET)

        suburb = d.pop("suburb", UNSET)

        postcode = d.pop("postcode", UNSET)

        domain_listing_admin_service_v1_model_past_sale_address = cls(
            state=state,
            unit_number=unit_number,
            street_number=street_number,
            street=street,
            suburb=suburb,
            postcode=postcode,
        )

        domain_listing_admin_service_v1_model_past_sale_address.additional_properties = d
        return domain_listing_admin_service_v1_model_past_sale_address

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
