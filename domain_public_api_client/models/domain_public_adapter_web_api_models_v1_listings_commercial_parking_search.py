from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_public_adapter_web_api_models_v1_listings_commercial_parking_search_type import (
    DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearchType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearch")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearch:
    """Listing search. Parking search criteria

    Attributes:
        type (Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearchType]): Parking type
        carspaces (Union[Unset, int]): Minimum carspace count
    """

    type: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearchType] = UNSET
    carspaces: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        carspaces = self.carspaces

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if carspaces is not UNSET:
            field_dict["carspaces"] = carspaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearchType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DomainPublicAdapterWebApiModelsV1ListingsCommercialParkingSearchType(_type)

        carspaces = d.pop("carspaces", UNSET)

        domain_public_adapter_web_api_models_v1_listings_commercial_parking_search = cls(
            type=type,
            carspaces=carspaces,
        )

        domain_public_adapter_web_api_models_v1_listings_commercial_parking_search.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_commercial_parking_search

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
