from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listing_admin_service_v1_model_supplementary_metadata import (
        DomainListingAdminServiceV1ModelSupplementaryMetadata,
    )


T = TypeVar("T", bound="DomainListingAdminServiceV1ModelListingSupplementary")


@_attrs_define
class DomainListingAdminServiceV1ModelListingSupplementary:
    """Listing supplementary

    Attributes:
        name (Union[Unset, str]): Name
        description (Union[Unset, str]): Description
        types (Union[Unset, List[str]]): Types
        metadata (Union[Unset, List['DomainListingAdminServiceV1ModelSupplementaryMetadata']]): Metadata
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    types: Union[Unset, List[str]] = UNSET
    metadata: Union[Unset, List["DomainListingAdminServiceV1ModelSupplementaryMetadata"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.types, Unset):
            types = self.types

        metadata: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = []
            for metadata_item_data in self.metadata:
                metadata_item = metadata_item_data.to_dict()
                metadata.append(metadata_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if types is not UNSET:
            field_dict["types"] = types
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_listing_admin_service_v1_model_supplementary_metadata import (
            DomainListingAdminServiceV1ModelSupplementaryMetadata,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        types = cast(List[str], d.pop("types", UNSET))

        metadata = []
        _metadata = d.pop("metadata", UNSET)
        for metadata_item_data in _metadata or []:
            metadata_item = DomainListingAdminServiceV1ModelSupplementaryMetadata.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        domain_listing_admin_service_v1_model_listing_supplementary = cls(
            name=name,
            description=description,
            types=types,
            metadata=metadata,
        )

        domain_listing_admin_service_v1_model_listing_supplementary.additional_properties = d
        return domain_listing_admin_service_v1_model_listing_supplementary

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
