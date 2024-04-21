import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse")


@_attrs_define
class DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse:
    """
    Attributes:
        s_3_key (Union[Unset, str]):
        message (Union[Unset, str]):
        enquiry_receipt_timestamp (Union[Unset, datetime.datetime]):
        warnings (Union[Unset, List[str]]):
    """

    s_3_key: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    enquiry_receipt_timestamp: Union[Unset, datetime.datetime] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        s_3_key = self.s_3_key

        message = self.message

        enquiry_receipt_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.enquiry_receipt_timestamp, Unset):
            enquiry_receipt_timestamp = self.enquiry_receipt_timestamp.isoformat()

        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if s_3_key is not UNSET:
            field_dict["s3Key"] = s_3_key
        if message is not UNSET:
            field_dict["message"] = message
        if enquiry_receipt_timestamp is not UNSET:
            field_dict["enquiryReceiptTimestamp"] = enquiry_receipt_timestamp
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        s_3_key = d.pop("s3Key", UNSET)

        message = d.pop("message", UNSET)

        _enquiry_receipt_timestamp = d.pop("enquiryReceiptTimestamp", UNSET)
        enquiry_receipt_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_enquiry_receipt_timestamp, Unset):
            enquiry_receipt_timestamp = UNSET
        else:
            enquiry_receipt_timestamp = isoparse(_enquiry_receipt_timestamp)

        warnings = cast(List[str], d.pop("warnings", UNSET))

        domain_enquiry_service_v1_model_group_enquiry_service_models_enquiry_response = cls(
            s_3_key=s_3_key,
            message=message,
            enquiry_receipt_timestamp=enquiry_receipt_timestamp,
            warnings=warnings,
        )

        domain_enquiry_service_v1_model_group_enquiry_service_models_enquiry_response.additional_properties = d
        return domain_enquiry_service_v1_model_group_enquiry_service_models_enquiry_response

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
