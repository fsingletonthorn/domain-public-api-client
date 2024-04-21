from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_geo_point import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint,
    )


T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCircle")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCircle:
    """
    Attributes:
        center (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint]):
        radius_in_meters (Union[Unset, int]):
    """

    center: Union[Unset, "DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint"] = UNSET
    radius_in_meters: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        center: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.center, Unset):
            center = self.center.to_dict()

        radius_in_meters = self.radius_in_meters

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if center is not UNSET:
            field_dict["center"] = center
        if radius_in_meters is not UNSET:
            field_dict["radiusInMeters"] = radius_in_meters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_geo_point import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint,
        )

        d = src_dict.copy()
        _center = d.pop("center", UNSET)
        center: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint]
        if isinstance(_center, Unset):
            center = UNSET
        else:
            center = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint.from_dict(_center)

        radius_in_meters = d.pop("radiusInMeters", UNSET)

        domain_search_service_v2_model_domain_search_web_api_v2_models_circle = cls(
            center=center,
            radius_in_meters=radius_in_meters,
        )

        domain_search_service_v2_model_domain_search_web_api_v2_models_circle.additional_properties = d
        return domain_search_service_v2_model_domain_search_web_api_v2_models_circle

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
