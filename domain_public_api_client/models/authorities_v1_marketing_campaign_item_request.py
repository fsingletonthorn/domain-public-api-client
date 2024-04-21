from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthoritiesV1MarketingCampaignItemRequest")


@_attrs_define
class AuthoritiesV1MarketingCampaignItemRequest:
    """
    Attributes:
        item_id (Union[Unset, str]):
        final_price (Union[Unset, str]):  Example: 4000.00.
        vendor_price (Union[Unset, str]):  Example: 4000.00.
        description (Union[None, Unset, str]):
        selected (Union[Unset, bool]):  Default: True.
        hidden (Union[Unset, bool]):  Default: False.
    """

    item_id: Union[Unset, str] = UNSET
    final_price: Union[Unset, str] = UNSET
    vendor_price: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    selected: Union[Unset, bool] = True
    hidden: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_id = self.item_id

        final_price = self.final_price

        vendor_price = self.vendor_price

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        selected = self.selected

        hidden = self.hidden

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if final_price is not UNSET:
            field_dict["finalPrice"] = final_price
        if vendor_price is not UNSET:
            field_dict["vendorPrice"] = vendor_price
        if description is not UNSET:
            field_dict["description"] = description
        if selected is not UNSET:
            field_dict["selected"] = selected
        if hidden is not UNSET:
            field_dict["hidden"] = hidden

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_id = d.pop("itemId", UNSET)

        final_price = d.pop("finalPrice", UNSET)

        vendor_price = d.pop("vendorPrice", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        selected = d.pop("selected", UNSET)

        hidden = d.pop("hidden", UNSET)

        authorities_v1_marketing_campaign_item_request = cls(
            item_id=item_id,
            final_price=final_price,
            vendor_price=vendor_price,
            description=description,
            selected=selected,
            hidden=hidden,
        )

        authorities_v1_marketing_campaign_item_request.additional_properties = d
        return authorities_v1_marketing_campaign_item_request

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
