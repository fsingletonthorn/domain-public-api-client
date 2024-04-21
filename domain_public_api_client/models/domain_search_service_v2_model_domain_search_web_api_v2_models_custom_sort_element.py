from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_custom_sort_element_direction import (
    DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElementDirection,
)
from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_custom_sort_element_field import (
    DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElementField,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElement")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElement:
    """
    Attributes:
        field (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElementField]):
        direction (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElementDirection]):
    """

    field: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElementField] = UNSET
    direction: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElementDirection] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field: Union[Unset, str] = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.value

        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _field = d.pop("field", UNSET)
        field: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElementField]
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElementField(_field)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElementDirection]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElementDirection(_direction)

        domain_search_service_v2_model_domain_search_web_api_v2_models_custom_sort_element = cls(
            field=field,
            direction=direction,
        )

        domain_search_service_v2_model_domain_search_web_api_v2_models_custom_sort_element.additional_properties = d
        return domain_search_service_v2_model_domain_search_web_api_v2_models_custom_sort_element

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
