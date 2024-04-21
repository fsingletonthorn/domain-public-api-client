from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_geo_point import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint,
    )


T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsPolygon")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsPolygon:
    """
    Attributes:
        points (Union[Unset, List['DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint']]):
    """

    points: Union[Unset, List["DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        points: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_geo_point import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint,
        )

        d = src_dict.copy()
        points = []
        _points = d.pop("points", UNSET)
        for points_item_data in _points or []:
            points_item = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint.from_dict(points_item_data)

            points.append(points_item)

        domain_search_service_v2_model_domain_search_web_api_v2_models_polygon = cls(
            points=points,
        )

        domain_search_service_v2_model_domain_search_web_api_v2_models_polygon.additional_properties = d
        return domain_search_service_v2_model_domain_search_web_api_v2_models_polygon

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
