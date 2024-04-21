from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_price_search_type import (
    DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearchType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearch")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearch:
    """Search criteria. Price

    Attributes:
        min_ (Union[Unset, int]): Minimum price. null - no minimum price limit
        max_ (Union[Unset, int]): Maximum price. null - no maximum price limit
        type (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearchType]): Price type
    """

    min_: Union[Unset, int] = UNSET
    max_: Union[Unset, int] = UNSET
    type: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearchType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_ = self.min_

        max_ = self.max_

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearchType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DomainPublicAdapterWebApiModelsV1ListingsCommercialPriceSearchType(_type)

        domain_public_adapter_web_api_models_v1_listings_commercial_price_search = cls(
            min_=min_,
            max_=max_,
            type=type,
        )

        domain_public_adapter_web_api_models_v1_listings_commercial_price_search.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_commercial_price_search

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
