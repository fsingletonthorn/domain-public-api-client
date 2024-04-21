from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsCommercialGeoPoint:
    """Geographic coordinate

    Attributes:
        lat (Union[Unset, float]): Location latitude
        long (Union[Unset, float]): Location longitude
    """

    lat: Union[Unset, float] = UNSET
    long: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lat = self.lat

        long = self.long

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lat is not UNSET:
            field_dict["lat"] = lat
        if long is not UNSET:
            field_dict["long"] = long

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lat = d.pop("lat", UNSET)

        long = d.pop("long", UNSET)

        domain_public_adapter_web_api_models_v1_listings_commercial_geo_point = cls(
            lat=lat,
            long=long,
        )

        domain_public_adapter_web_api_models_v1_listings_commercial_geo_point.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_commercial_geo_point

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
