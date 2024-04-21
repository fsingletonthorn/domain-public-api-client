from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_public_adapter_web_api_models_v1_enquiries_enquiry_delivery_method import (
    DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryDeliveryMethod,
)
from ..models.domain_public_adapter_web_api_models_v1_enquiries_enquiry_enquiry_type import (
    DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryEnquiryType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_public_adapter_web_api_models_v1_enquiries_enquiry_meta_data import (
        DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryMetaData,
    )
    from ..models.domain_public_adapter_web_api_models_v1_enquiries_sender import (
        DomainPublicAdapterWebApiModelsV1EnquiriesSender,
    )


T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry:
    """An enquiry with associated reference (eg. listing)

    Attributes:
        delivery_method (Union[Unset, DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryDeliveryMethod]): Delivery method
            of the enquiry
        enquiry_type (Union[Unset, DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryEnquiryType]): Type of enquiry
        reference_id (Union[Unset, int]): Listing identifier
        id (Union[Unset, str]): Enquiry identifier
        sender (Union[Unset, DomainPublicAdapterWebApiModelsV1EnquiriesSender]): Contains enquiry sender details
        subject (Union[Unset, str]): Enquiry subject
        message (Union[Unset, str]): Enquiry message
        meta_data (Union[Unset, DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryMetaData]): MetaData of the enquiry
    """

    delivery_method: Union[Unset, DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryDeliveryMethod] = UNSET
    enquiry_type: Union[Unset, DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryEnquiryType] = UNSET
    reference_id: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    sender: Union[Unset, "DomainPublicAdapterWebApiModelsV1EnquiriesSender"] = UNSET
    subject: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    meta_data: Union[Unset, "DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryMetaData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delivery_method: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_method, Unset):
            delivery_method = self.delivery_method.value

        enquiry_type: Union[Unset, str] = UNSET
        if not isinstance(self.enquiry_type, Unset):
            enquiry_type = self.enquiry_type.value

        reference_id = self.reference_id

        id = self.id

        sender: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        subject = self.subject

        message = self.message

        meta_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_method is not UNSET:
            field_dict["deliveryMethod"] = delivery_method
        if enquiry_type is not UNSET:
            field_dict["enquiryType"] = enquiry_type
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if id is not UNSET:
            field_dict["id"] = id
        if sender is not UNSET:
            field_dict["sender"] = sender
        if subject is not UNSET:
            field_dict["subject"] = subject
        if message is not UNSET:
            field_dict["message"] = message
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_public_adapter_web_api_models_v1_enquiries_enquiry_meta_data import (
            DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryMetaData,
        )
        from ..models.domain_public_adapter_web_api_models_v1_enquiries_sender import (
            DomainPublicAdapterWebApiModelsV1EnquiriesSender,
        )

        d = src_dict.copy()
        _delivery_method = d.pop("deliveryMethod", UNSET)
        delivery_method: Union[Unset, DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryDeliveryMethod]
        if isinstance(_delivery_method, Unset):
            delivery_method = UNSET
        else:
            delivery_method = DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryDeliveryMethod(_delivery_method)

        _enquiry_type = d.pop("enquiryType", UNSET)
        enquiry_type: Union[Unset, DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryEnquiryType]
        if isinstance(_enquiry_type, Unset):
            enquiry_type = UNSET
        else:
            enquiry_type = DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryEnquiryType(_enquiry_type)

        reference_id = d.pop("referenceId", UNSET)

        id = d.pop("id", UNSET)

        _sender = d.pop("sender", UNSET)
        sender: Union[Unset, DomainPublicAdapterWebApiModelsV1EnquiriesSender]
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = DomainPublicAdapterWebApiModelsV1EnquiriesSender.from_dict(_sender)

        subject = d.pop("subject", UNSET)

        message = d.pop("message", UNSET)

        _meta_data = d.pop("metaData", UNSET)
        meta_data: Union[Unset, DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryMetaData]
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = DomainPublicAdapterWebApiModelsV1EnquiriesEnquiryMetaData.from_dict(_meta_data)

        domain_public_adapter_web_api_models_v1_enquiries_enquiry = cls(
            delivery_method=delivery_method,
            enquiry_type=enquiry_type,
            reference_id=reference_id,
            id=id,
            sender=sender,
            subject=subject,
            message=message,
            meta_data=meta_data,
        )

        domain_public_adapter_web_api_models_v1_enquiries_enquiry.additional_properties = d
        return domain_public_adapter_web_api_models_v1_enquiries_enquiry

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
