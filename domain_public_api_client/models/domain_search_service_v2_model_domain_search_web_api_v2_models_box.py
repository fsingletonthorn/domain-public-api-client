from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_geo_point import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint,
    )


T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsBox")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsBox:
    """
    Attributes:
        top_left (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint]):
        bottom_right (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint]):
    """

    top_left: Union[Unset, "DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint"] = UNSET
    bottom_right: Union[Unset, "DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        top_left: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.top_left, Unset):
            top_left = self.top_left.to_dict()

        bottom_right: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bottom_right, Unset):
            bottom_right = self.bottom_right.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_left is not UNSET:
            field_dict["topLeft"] = top_left
        if bottom_right is not UNSET:
            field_dict["bottomRight"] = bottom_right

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_geo_point import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint,
        )

        d = src_dict.copy()
        _top_left = d.pop("topLeft", UNSET)
        top_left: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint]
        if isinstance(_top_left, Unset):
            top_left = UNSET
        else:
            top_left = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint.from_dict(_top_left)

        _bottom_right = d.pop("bottomRight", UNSET)
        bottom_right: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint]
        if isinstance(_bottom_right, Unset):
            bottom_right = UNSET
        else:
            bottom_right = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint.from_dict(_bottom_right)

        domain_search_service_v2_model_domain_search_web_api_v2_models_box = cls(
            top_left=top_left,
            bottom_right=bottom_right,
        )

        domain_search_service_v2_model_domain_search_web_api_v2_models_box.additional_properties = d
        return domain_search_service_v2_model_domain_search_web_api_v2_models_box

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
