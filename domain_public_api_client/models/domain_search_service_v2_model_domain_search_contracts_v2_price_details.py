from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchContractsV2PriceDetails")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchContractsV2PriceDetails:
    """
    Attributes:
        price (Union[Unset, int]):
        price_from (Union[Unset, int]):
        price_to (Union[Unset, int]):
        display_price (Union[Unset, str]):
    """

    price: Union[Unset, int] = UNSET
    price_from: Union[Unset, int] = UNSET
    price_to: Union[Unset, int] = UNSET
    display_price: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price = self.price

        price_from = self.price_from

        price_to = self.price_to

        display_price = self.display_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price is not UNSET:
            field_dict["price"] = price
        if price_from is not UNSET:
            field_dict["priceFrom"] = price_from
        if price_to is not UNSET:
            field_dict["priceTo"] = price_to
        if display_price is not UNSET:
            field_dict["displayPrice"] = display_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        price = d.pop("price", UNSET)

        price_from = d.pop("priceFrom", UNSET)

        price_to = d.pop("priceTo", UNSET)

        display_price = d.pop("displayPrice", UNSET)

        domain_search_service_v2_model_domain_search_contracts_v2_price_details = cls(
            price=price,
            price_from=price_from,
            price_to=price_to,
            display_price=display_price,
        )

        domain_search_service_v2_model_domain_search_contracts_v2_price_details.additional_properties = d
        return domain_search_service_v2_model_domain_search_contracts_v2_price_details

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
