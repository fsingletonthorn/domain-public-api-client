from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint:
    """
    Attributes:
        lat (Union[Unset, float]):
        lon (Union[Unset, float]):
    """

    lat: Union[Unset, float] = UNSET
    lon: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lat = self.lat

        lon = self.lon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lat = d.pop("lat", UNSET)

        lon = d.pop("lon", UNSET)

        domain_search_service_v2_model_domain_search_web_api_v2_models_geo_point = cls(
            lat=lat,
            lon=lon,
        )

        domain_search_service_v2_model_domain_search_web_api_v2_models_geo_point.additional_properties = d
        return domain_search_service_v2_model_domain_search_web_api_v2_models_geo_point

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
