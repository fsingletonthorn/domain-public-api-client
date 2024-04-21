from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.enquiries_v1_recipient_recipient_type import EnquiriesV1RecipientRecipientType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnquiriesV1Recipient")


@_attrs_define
class EnquiriesV1Recipient:
    """Recipient

    Attributes:
        address (str): Gets or Sets Address
        recipient_type (Union[Unset, EnquiriesV1RecipientRecipientType]): Gets or Sets RecipientType
    """

    address: str
    recipient_type: Union[Unset, EnquiriesV1RecipientRecipientType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        address = self.address

        recipient_type: Union[Unset, str] = UNSET
        if not isinstance(self.recipient_type, Unset):
            recipient_type = self.recipient_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "address": address,
            }
        )
        if recipient_type is not UNSET:
            field_dict["recipientType"] = recipient_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address")

        _recipient_type = d.pop("recipientType", UNSET)
        recipient_type: Union[Unset, EnquiriesV1RecipientRecipientType]
        if isinstance(_recipient_type, Unset):
            recipient_type = UNSET
        else:
            recipient_type = EnquiriesV1RecipientRecipientType(_recipient_type)

        enquiries_v1_recipient = cls(
            address=address,
            recipient_type=recipient_type,
        )

        return enquiries_v1_recipient
