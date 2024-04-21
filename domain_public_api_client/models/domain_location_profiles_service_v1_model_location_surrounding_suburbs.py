from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainLocationProfilesServiceV1ModelLocationSurroundingSuburbs")


@_attrs_define
class DomainLocationProfilesServiceV1ModelLocationSurroundingSuburbs:
    """
    Attributes:
        name (Union[Unset, str]):
        url_slug (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    url_slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        url_slug = self.url_slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if url_slug is not UNSET:
            field_dict["urlSlug"] = url_slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        url_slug = d.pop("urlSlug", UNSET)

        domain_location_profiles_service_v1_model_location_surrounding_suburbs = cls(
            name=name,
            url_slug=url_slug,
        )

        domain_location_profiles_service_v1_model_location_surrounding_suburbs.additional_properties = d
        return domain_location_profiles_service_v1_model_location_surrounding_suburbs

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
