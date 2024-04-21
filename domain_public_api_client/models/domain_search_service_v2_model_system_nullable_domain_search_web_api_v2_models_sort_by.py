from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_search_service_v2_model_system_nullable_domain_search_web_api_v2_models_sort_by_direction import (
    DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortByDirection,
)
from ..models.domain_search_service_v2_model_system_nullable_domain_search_web_api_v2_models_sort_by_sort_key import (
    DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBySortKey,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_geo_point import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint,
    )


T = TypeVar("T", bound="DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBy")


@_attrs_define
class DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBy:
    """
    Attributes:
        sort_key (Union[Unset, DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBySortKey]):
        direction (Union[Unset, DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortByDirection]):
        proximity_to (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint]):
    """

    sort_key: Union[Unset, DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBySortKey] = UNSET
    direction: Union[Unset, DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortByDirection] = UNSET
    proximity_to: Union[Unset, "DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sort_key: Union[Unset, str] = UNSET
        if not isinstance(self.sort_key, Unset):
            sort_key = self.sort_key.value

        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        proximity_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proximity_to, Unset):
            proximity_to = self.proximity_to.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sort_key is not UNSET:
            field_dict["sortKey"] = sort_key
        if direction is not UNSET:
            field_dict["direction"] = direction
        if proximity_to is not UNSET:
            field_dict["proximityTo"] = proximity_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_geo_point import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint,
        )

        d = src_dict.copy()
        _sort_key = d.pop("sortKey", UNSET)
        sort_key: Union[Unset, DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBySortKey]
        if isinstance(_sort_key, Unset):
            sort_key = UNSET
        else:
            sort_key = DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortBySortKey(_sort_key)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortByDirection]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = DomainSearchServiceV2ModelSystemNullableDomainSearchWebApiV2ModelsSortByDirection(_direction)

        _proximity_to = d.pop("proximityTo", UNSET)
        proximity_to: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint]
        if isinstance(_proximity_to, Unset):
            proximity_to = UNSET
        else:
            proximity_to = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsGeoPoint.from_dict(_proximity_to)

        domain_search_service_v2_model_system_nullable_domain_search_web_api_v2_models_sort_by = cls(
            sort_key=sort_key,
            direction=direction,
            proximity_to=proximity_to,
        )

        domain_search_service_v2_model_system_nullable_domain_search_web_api_v2_models_sort_by.additional_properties = d
        return domain_search_service_v2_model_system_nullable_domain_search_web_api_v2_models_sort_by

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
