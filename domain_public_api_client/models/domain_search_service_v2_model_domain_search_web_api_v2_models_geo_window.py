from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_box import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsBox,
    )
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_circle import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCircle,
    )
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_polygon import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsPolygon,
    )


T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoWindow")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoWindow:
    """
    Attributes:
        box (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsBox]):
        circle (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCircle]):
        polygon (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsPolygon]):
    """

    box: Union[Unset, "DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsBox"] = UNSET
    circle: Union[Unset, "DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCircle"] = UNSET
    polygon: Union[Unset, "DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsPolygon"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        box: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.box, Unset):
            box = self.box.to_dict()

        circle: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.circle, Unset):
            circle = self.circle.to_dict()

        polygon: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.polygon, Unset):
            polygon = self.polygon.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if box is not UNSET:
            field_dict["box"] = box
        if circle is not UNSET:
            field_dict["circle"] = circle
        if polygon is not UNSET:
            field_dict["polygon"] = polygon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_box import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsBox,
        )
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_circle import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCircle,
        )
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_polygon import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsPolygon,
        )

        d = src_dict.copy()
        _box = d.pop("box", UNSET)
        box: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsBox]
        if isinstance(_box, Unset):
            box = UNSET
        else:
            box = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsBox.from_dict(_box)

        _circle = d.pop("circle", UNSET)
        circle: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCircle]
        if isinstance(_circle, Unset):
            circle = UNSET
        else:
            circle = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCircle.from_dict(_circle)

        _polygon = d.pop("polygon", UNSET)
        polygon: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsPolygon]
        if isinstance(_polygon, Unset):
            polygon = UNSET
        else:
            polygon = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsPolygon.from_dict(_polygon)

        domain_search_service_v2_model_domain_search_web_api_v2_models_geo_window = cls(
            box=box,
            circle=circle,
            polygon=polygon,
        )

        domain_search_service_v2_model_domain_search_web_api_v2_models_geo_window.additional_properties = d
        return domain_search_service_v2_model_domain_search_web_api_v2_models_geo_window

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
