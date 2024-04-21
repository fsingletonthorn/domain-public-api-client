from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="AuthoritiesV1Attachments")


@_attrs_define
class AuthoritiesV1Attachments:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 0557934b-b9f8-4d88-bd5a-9c69d5bf0beb.
        attachment (Union[Unset, File]):  Example: /path/to/file.
        file_type (Union[Unset, str]):  Example: Available options are marketingAttachments, commissionAttachments,
            espAttachment.
    """

    id: Union[Unset, str] = UNSET
    attachment: Union[Unset, File] = UNSET
    file_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        attachment: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.attachment, Unset):
            attachment = self.attachment.to_tuple()

        file_type = self.file_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if file_type is not UNSET:
            field_dict["fileType"] = file_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _attachment = d.pop("attachment", UNSET)
        attachment: Union[Unset, File]
        if isinstance(_attachment, Unset):
            attachment = UNSET
        else:
            attachment = File(payload=BytesIO(_attachment))

        file_type = d.pop("fileType", UNSET)

        authorities_v1_attachments = cls(
            id=id,
            attachment=attachment,
            file_type=file_type,
        )

        authorities_v1_attachments.additional_properties = d
        return authorities_v1_attachments

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
