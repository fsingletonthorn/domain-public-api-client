import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.enquiries_v1_enquiry_report_delivery_method import EnquiriesV1EnquiryReportDeliveryMethod
from ..models.enquiries_v1_enquiry_report_enquiry_type import EnquiriesV1EnquiryReportEnquiryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enquiries_v1_enquiry_report_meta_data_type_0 import EnquiriesV1EnquiryReportMetaDataType0
    from ..models.enquiries_v1_recipient_delivery_status import EnquiriesV1RecipientDeliveryStatus
    from ..models.enquiries_v1_sender import EnquiriesV1Sender


T = TypeVar("T", bound="EnquiriesV1EnquiryReport")


@_attrs_define
class EnquiriesV1EnquiryReport:
    """
    Attributes:
        delivery_method (Union[Unset, EnquiriesV1EnquiryReportDeliveryMethod]):
        enquiry_type (Union[Unset, EnquiriesV1EnquiryReportEnquiryType]):
        id (Union[None, Unset, str]):
        message (Union[None, Unset, str]):
        meta_data (Union['EnquiriesV1EnquiryReportMetaDataType0', None, Unset]):
        recipients_delivery_status (Union[List['EnquiriesV1RecipientDeliveryStatus'], None, Unset]):
        reference_id (Union[None, Unset, int]):
        sender (Union[Unset, EnquiriesV1Sender]):
        date_received (Union[None, Unset, datetime.datetime]):
        agency_id (Union[None, Unset, int]):
    """

    delivery_method: Union[Unset, EnquiriesV1EnquiryReportDeliveryMethod] = UNSET
    enquiry_type: Union[Unset, EnquiriesV1EnquiryReportEnquiryType] = UNSET
    id: Union[None, Unset, str] = UNSET
    message: Union[None, Unset, str] = UNSET
    meta_data: Union["EnquiriesV1EnquiryReportMetaDataType0", None, Unset] = UNSET
    recipients_delivery_status: Union[List["EnquiriesV1RecipientDeliveryStatus"], None, Unset] = UNSET
    reference_id: Union[None, Unset, int] = UNSET
    sender: Union[Unset, "EnquiriesV1Sender"] = UNSET
    date_received: Union[None, Unset, datetime.datetime] = UNSET
    agency_id: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.enquiries_v1_enquiry_report_meta_data_type_0 import EnquiriesV1EnquiryReportMetaDataType0

        delivery_method: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_method, Unset):
            delivery_method = self.delivery_method.value

        enquiry_type: Union[Unset, str] = UNSET
        if not isinstance(self.enquiry_type, Unset):
            enquiry_type = self.enquiry_type.value

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        message: Union[None, Unset, str]
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        meta_data: Union[Dict[str, Any], None, Unset]
        if isinstance(self.meta_data, Unset):
            meta_data = UNSET
        elif isinstance(self.meta_data, EnquiriesV1EnquiryReportMetaDataType0):
            meta_data = self.meta_data.to_dict()
        else:
            meta_data = self.meta_data

        recipients_delivery_status: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.recipients_delivery_status, Unset):
            recipients_delivery_status = UNSET
        elif isinstance(self.recipients_delivery_status, list):
            recipients_delivery_status = []
            for recipients_delivery_status_type_0_item_data in self.recipients_delivery_status:
                recipients_delivery_status_type_0_item = recipients_delivery_status_type_0_item_data.to_dict()
                recipients_delivery_status.append(recipients_delivery_status_type_0_item)

        else:
            recipients_delivery_status = self.recipients_delivery_status

        reference_id: Union[None, Unset, int]
        if isinstance(self.reference_id, Unset):
            reference_id = UNSET
        else:
            reference_id = self.reference_id

        sender: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        date_received: Union[None, Unset, str]
        if isinstance(self.date_received, Unset):
            date_received = UNSET
        elif isinstance(self.date_received, datetime.datetime):
            date_received = self.date_received.isoformat()
        else:
            date_received = self.date_received

        agency_id: Union[None, Unset, int]
        if isinstance(self.agency_id, Unset):
            agency_id = UNSET
        else:
            agency_id = self.agency_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if delivery_method is not UNSET:
            field_dict["deliveryMethod"] = delivery_method
        if enquiry_type is not UNSET:
            field_dict["enquiryType"] = enquiry_type
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data
        if recipients_delivery_status is not UNSET:
            field_dict["recipientsDeliveryStatus"] = recipients_delivery_status
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if sender is not UNSET:
            field_dict["sender"] = sender
        if date_received is not UNSET:
            field_dict["dateReceived"] = date_received
        if agency_id is not UNSET:
            field_dict["agencyId"] = agency_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.enquiries_v1_enquiry_report_meta_data_type_0 import EnquiriesV1EnquiryReportMetaDataType0
        from ..models.enquiries_v1_recipient_delivery_status import EnquiriesV1RecipientDeliveryStatus
        from ..models.enquiries_v1_sender import EnquiriesV1Sender

        d = src_dict.copy()
        _delivery_method = d.pop("deliveryMethod", UNSET)
        delivery_method: Union[Unset, EnquiriesV1EnquiryReportDeliveryMethod]
        if isinstance(_delivery_method, Unset):
            delivery_method = UNSET
        else:
            delivery_method = EnquiriesV1EnquiryReportDeliveryMethod(_delivery_method)

        _enquiry_type = d.pop("enquiryType", UNSET)
        enquiry_type: Union[Unset, EnquiriesV1EnquiryReportEnquiryType]
        if isinstance(_enquiry_type, Unset):
            enquiry_type = UNSET
        else:
            enquiry_type = EnquiriesV1EnquiryReportEnquiryType(_enquiry_type)

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_meta_data(data: object) -> Union["EnquiriesV1EnquiryReportMetaDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_data_type_0 = EnquiriesV1EnquiryReportMetaDataType0.from_dict(data)

                return meta_data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["EnquiriesV1EnquiryReportMetaDataType0", None, Unset], data)

        meta_data = _parse_meta_data(d.pop("metaData", UNSET))

        def _parse_recipients_delivery_status(
            data: object,
        ) -> Union[List["EnquiriesV1RecipientDeliveryStatus"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recipients_delivery_status_type_0 = []
                _recipients_delivery_status_type_0 = data
                for recipients_delivery_status_type_0_item_data in _recipients_delivery_status_type_0:
                    recipients_delivery_status_type_0_item = EnquiriesV1RecipientDeliveryStatus.from_dict(
                        recipients_delivery_status_type_0_item_data
                    )

                    recipients_delivery_status_type_0.append(recipients_delivery_status_type_0_item)

                return recipients_delivery_status_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["EnquiriesV1RecipientDeliveryStatus"], None, Unset], data)

        recipients_delivery_status = _parse_recipients_delivery_status(d.pop("recipientsDeliveryStatus", UNSET))

        def _parse_reference_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        reference_id = _parse_reference_id(d.pop("referenceId", UNSET))

        _sender = d.pop("sender", UNSET)
        sender: Union[Unset, EnquiriesV1Sender]
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = EnquiriesV1Sender.from_dict(_sender)

        def _parse_date_received(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_received_type_0 = isoparse(data)

                return date_received_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_received = _parse_date_received(d.pop("dateReceived", UNSET))

        def _parse_agency_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        agency_id = _parse_agency_id(d.pop("agencyId", UNSET))

        enquiries_v1_enquiry_report = cls(
            delivery_method=delivery_method,
            enquiry_type=enquiry_type,
            id=id,
            message=message,
            meta_data=meta_data,
            recipients_delivery_status=recipients_delivery_status,
            reference_id=reference_id,
            sender=sender,
            date_received=date_received,
            agency_id=agency_id,
        )

        return enquiries_v1_enquiry_report
