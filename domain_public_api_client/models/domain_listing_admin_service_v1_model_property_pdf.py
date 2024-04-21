from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listing_admin_service_v1_model_property_pdf_type import (
    DomainListingAdminServiceV1ModelPropertyPdfType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelPropertyPdf")


@_attrs_define
class DomainListingAdminServiceV1ModelPropertyPdf:
    """PDF file related to the listing

    Attributes:
        type (Union[Unset, DomainListingAdminServiceV1ModelPropertyPdfType]): Type of the PDF
        url (Union[Unset, str]): Url of the PDF
        description (Union[Unset, str]): Description of the PDF
    """

    type: Union[Unset, DomainListingAdminServiceV1ModelPropertyPdfType] = UNSET
    url: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        url = self.url

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, DomainListingAdminServiceV1ModelPropertyPdfType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DomainListingAdminServiceV1ModelPropertyPdfType(_type)

        url = d.pop("url", UNSET)

        description = d.pop("description", UNSET)

        domain_listing_admin_service_v1_model_property_pdf = cls(
            type=type,
            url=url,
            description=description,
        )

        domain_listing_admin_service_v1_model_property_pdf.additional_properties = d
        return domain_listing_admin_service_v1_model_property_pdf

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
