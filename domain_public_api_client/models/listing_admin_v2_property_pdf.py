from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_property_pdf_type import ListingAdminV2PropertyPdfType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2PropertyPdf")


@_attrs_define
class ListingAdminV2PropertyPdf:
    """PDF file related to the listing

    Attributes:
        url (str): Url of the PDF
        type (Union[Unset, ListingAdminV2PropertyPdfType]): Type of the PDF. `DevProjectPdf` PDF files are only visible,
            if the listing is a child listing of an active development project.
        description (Union[Unset, str]): Description of the PDF
    """

    url: str
    type: Union[Unset, ListingAdminV2PropertyPdfType] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        _type = d.pop("type", UNSET)
        type: Union[Unset, ListingAdminV2PropertyPdfType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ListingAdminV2PropertyPdfType(_type)

        description = d.pop("description", UNSET)

        listing_admin_v2_property_pdf = cls(
            url=url,
            type=type,
            description=description,
        )

        listing_admin_v2_property_pdf.additional_properties = d
        return listing_admin_v2_property_pdf

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
