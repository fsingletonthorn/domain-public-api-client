from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_property_media_resource_type import ListingAdminV2PropertyMediaResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2PropertyMedia")


@_attrs_define
class ListingAdminV2PropertyMedia:
    """Resource related to the listing

    Attributes:
        url (str): shows the place from where file can be downloaded
        resource_type (Union[Unset, ListingAdminV2PropertyMediaResourceType]): Type of the resource
    """

    url: str
    resource_type: Union[Unset, ListingAdminV2PropertyMediaResourceType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        resource_type: Union[Unset, str] = UNSET
        if not isinstance(self.resource_type, Unset):
            resource_type = self.resource_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        _resource_type = d.pop("resourceType", UNSET)
        resource_type: Union[Unset, ListingAdminV2PropertyMediaResourceType]
        if isinstance(_resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = ListingAdminV2PropertyMediaResourceType(_resource_type)

        listing_admin_v2_property_media = cls(
            url=url,
            resource_type=resource_type,
        )

        listing_admin_v2_property_media.additional_properties = d
        return listing_admin_v2_property_media

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
