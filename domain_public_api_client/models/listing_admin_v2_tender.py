import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2Tender")


@_attrs_define
class ListingAdminV2Tender:
    """Tender Information

    Attributes:
        recipient_name (Union[Unset, str]): The recipient name of the tender, up to 50 characters
        address (Union[Unset, str]): Street address, up to 100 characters.
        end_date (Union[Unset, datetime.datetime]): Closing Date
    """

    recipient_name: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        recipient_name = self.recipient_name

        address = self.address

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recipient_name is not UNSET:
            field_dict["recipientName"] = recipient_name
        if address is not UNSET:
            field_dict["address"] = address
        if end_date is not UNSET:
            field_dict["endDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        recipient_name = d.pop("recipientName", UNSET)

        address = d.pop("address", UNSET)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        listing_admin_v2_tender = cls(
            recipient_name=recipient_name,
            address=address,
            end_date=end_date,
        )

        listing_admin_v2_tender.additional_properties = d
        return listing_admin_v2_tender

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
