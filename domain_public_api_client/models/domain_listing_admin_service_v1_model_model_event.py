from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listing_admin_service_v1_model_model_event_issue_type import (
    DomainListingAdminServiceV1ModelModelEventIssueType,
)
from ..models.domain_listing_admin_service_v1_model_model_event_severity import (
    DomainListingAdminServiceV1ModelModelEventSeverity,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelModelEvent")


@_attrs_define
class DomainListingAdminServiceV1ModelModelEvent:
    """Processing Event, use to show information, warnings or Errors

    Attributes:
        severity (Union[Unset, DomainListingAdminServiceV1ModelModelEventSeverity]): Severity of the Event
        issue_type (Union[Unset, DomainListingAdminServiceV1ModelModelEventIssueType]): Type of the issue
        message (Union[Unset, str]): Message associated with the event
    """

    severity: Union[Unset, DomainListingAdminServiceV1ModelModelEventSeverity] = UNSET
    issue_type: Union[Unset, DomainListingAdminServiceV1ModelModelEventIssueType] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        severity: Union[Unset, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        issue_type: Union[Unset, str] = UNSET
        if not isinstance(self.issue_type, Unset):
            issue_type = self.issue_type.value

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if severity is not UNSET:
            field_dict["severity"] = severity
        if issue_type is not UNSET:
            field_dict["issueType"] = issue_type
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, DomainListingAdminServiceV1ModelModelEventSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = DomainListingAdminServiceV1ModelModelEventSeverity(_severity)

        _issue_type = d.pop("issueType", UNSET)
        issue_type: Union[Unset, DomainListingAdminServiceV1ModelModelEventIssueType]
        if isinstance(_issue_type, Unset):
            issue_type = UNSET
        else:
            issue_type = DomainListingAdminServiceV1ModelModelEventIssueType(_issue_type)

        message = d.pop("message", UNSET)

        domain_listing_admin_service_v1_model_model_event = cls(
            severity=severity,
            issue_type=issue_type,
            message=message,
        )

        domain_listing_admin_service_v1_model_model_event.additional_properties = d
        return domain_listing_admin_service_v1_model_model_event

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
