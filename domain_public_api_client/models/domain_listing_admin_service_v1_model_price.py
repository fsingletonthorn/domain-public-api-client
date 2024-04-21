from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelPrice")


@_attrs_define
class DomainListingAdminServiceV1ModelPrice:
    r"""Pricing Information

    Attributes:
        display_text (Union[Unset, str]): When provided this will be shown instead of the price range, e.g.: \"Offers
            over $450K considered\"
        from_ (Union[Unset, int]): Lowest price the property is expected to sell/rent for to set search price. For a
            fixed price, set this value the same as To
        to (Union[Unset, int]): Highest price the property is expected to sell/rent for to set search price.   For a
            fixed price, set this value the same as From
    """

    display_text: Union[Unset, str] = UNSET
    from_: Union[Unset, int] = UNSET
    to: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_text = self.display_text

        from_ = self.from_

        to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_text is not UNSET:
            field_dict["displayText"] = display_text
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_text = d.pop("displayText", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        domain_listing_admin_service_v1_model_price = cls(
            display_text=display_text,
            from_=from_,
            to=to,
        )

        domain_listing_admin_service_v1_model_price.additional_properties = d
        return domain_listing_admin_service_v1_model_price

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
