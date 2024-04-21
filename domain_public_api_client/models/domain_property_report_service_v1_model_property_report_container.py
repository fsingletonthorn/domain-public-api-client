from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPropertyReportServiceV1ModelPropertyReportContainer")


@_attrs_define
class DomainPropertyReportServiceV1ModelPropertyReportContainer:
    """
    Attributes:
        mime_type (Union[Unset, str]):
        content (Union[Unset, str]):
    """

    mime_type: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mime_type = self.mime_type

        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mime_type = d.pop("mimeType", UNSET)

        content = d.pop("content", UNSET)

        domain_property_report_service_v1_model_property_report_container = cls(
            mime_type=mime_type,
            content=content,
        )

        domain_property_report_service_v1_model_property_report_container.additional_properties = d
        return domain_property_report_service_v1_model_property_report_container

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
