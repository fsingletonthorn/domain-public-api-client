from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.listings_v2_pdf_upload_type import ListingsV2PdfUploadType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV2PdfUpload")


@_attrs_define
class ListingsV2PdfUpload:
    """PDF file

    Attributes:
        type (Union[Unset, ListingsV2PdfUploadType]): Gets or Sets Type
        url (Union[None, Unset, str]): Url of the PDF
        filename (Union[None, Unset, str]): Original file name of the PDF
        file_description (Union[None, Unset, str]): Description of the PDF
    """

    type: Union[Unset, ListingsV2PdfUploadType] = UNSET
    url: Union[None, Unset, str] = UNSET
    filename: Union[None, Unset, str] = UNSET
    file_description: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        filename: Union[None, Unset, str]
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        file_description: Union[None, Unset, str]
        if isinstance(self.file_description, Unset):
            file_description = UNSET
        else:
            file_description = self.file_description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url
        if filename is not UNSET:
            field_dict["filename"] = filename
        if file_description is not UNSET:
            field_dict["fileDescription"] = file_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, ListingsV2PdfUploadType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ListingsV2PdfUploadType(_type)

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_filename(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        filename = _parse_filename(d.pop("filename", UNSET))

        def _parse_file_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_description = _parse_file_description(d.pop("fileDescription", UNSET))

        listings_v2_pdf_upload = cls(
            type=type,
            url=url,
            filename=filename,
            file_description=file_description,
        )

        return listings_v2_pdf_upload
