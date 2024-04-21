import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.enquiries_v1_recipient_delivery_status_delivery_status import (
    EnquiriesV1RecipientDeliveryStatusDeliveryStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enquiries_v1_recipient import EnquiriesV1Recipient


T = TypeVar("T", bound="EnquiriesV1RecipientDeliveryStatus")


@_attrs_define
class EnquiriesV1RecipientDeliveryStatus:
    """RecipientDeliveryStatus

    Attributes:
        delivery_status (Union[Unset, EnquiriesV1RecipientDeliveryStatusDeliveryStatus]): Gets or Sets DeliveryStatus
        recipient (Union[Unset, EnquiriesV1Recipient]): Recipient
        date (Union[None, Unset, datetime.datetime]): Gets or Sets Date
    """

    delivery_status: Union[Unset, EnquiriesV1RecipientDeliveryStatusDeliveryStatus] = UNSET
    recipient: Union[Unset, "EnquiriesV1Recipient"] = UNSET
    date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        delivery_status: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_status, Unset):
            delivery_status = self.delivery_status.value

        recipient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.to_dict()

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if delivery_status is not UNSET:
            field_dict["deliveryStatus"] = delivery_status
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.enquiries_v1_recipient import EnquiriesV1Recipient

        d = src_dict.copy()
        _delivery_status = d.pop("deliveryStatus", UNSET)
        delivery_status: Union[Unset, EnquiriesV1RecipientDeliveryStatusDeliveryStatus]
        if isinstance(_delivery_status, Unset):
            delivery_status = UNSET
        else:
            delivery_status = EnquiriesV1RecipientDeliveryStatusDeliveryStatus(_delivery_status)

        _recipient = d.pop("recipient", UNSET)
        recipient: Union[Unset, EnquiriesV1Recipient]
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = EnquiriesV1Recipient.from_dict(_recipient)

        def _parse_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date = _parse_date(d.pop("date", UNSET))

        enquiries_v1_recipient_delivery_status = cls(
            delivery_status=delivery_status,
            recipient=recipient,
            date=date,
        )

        return enquiries_v1_recipient_delivery_status
