from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listing_admin_service_v1_model_property_media_resource_type import (
    DomainListingAdminServiceV1ModelPropertyMediaResourceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelPropertyMedia")


@_attrs_define
class DomainListingAdminServiceV1ModelPropertyMedia:
    """Resource related to the listing

    Attributes:
        resource_type (Union[Unset, DomainListingAdminServiceV1ModelPropertyMediaResourceType]): Type of the resource
        url (Union[Unset, str]): shows the place from where file can be downloaded
    """

    resource_type: Union[Unset, DomainListingAdminServiceV1ModelPropertyMediaResourceType] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_type: Union[Unset, str] = UNSET
        if not isinstance(self.resource_type, Unset):
            resource_type = self.resource_type.value

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _resource_type = d.pop("resourceType", UNSET)
        resource_type: Union[Unset, DomainListingAdminServiceV1ModelPropertyMediaResourceType]
        if isinstance(_resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = DomainListingAdminServiceV1ModelPropertyMediaResourceType(_resource_type)

        url = d.pop("url", UNSET)

        domain_listing_admin_service_v1_model_property_media = cls(
            resource_type=resource_type,
            url=url,
        )

        domain_listing_admin_service_v1_model_property_media.additional_properties = d
        return domain_listing_admin_service_v1_model_property_media

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
