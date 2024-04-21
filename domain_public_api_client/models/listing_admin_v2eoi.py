import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2EOI")


@_attrs_define
class ListingAdminV2EOI:
    """Express of Interest

    Attributes:
        end_date (datetime.datetime): End date of EOI
        address (Union[Unset, str]): Street address, up to 100 characters
        recipient_name (Union[Unset, str]): The recipient name of the EOI, up to 50 characters
    """

    end_date: datetime.datetime
    address: Union[Unset, str] = UNSET
    recipient_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_date = self.end_date.isoformat()

        address = self.address

        recipient_name = self.recipient_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endDate": end_date,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if recipient_name is not UNSET:
            field_dict["recipientName"] = recipient_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end_date = isoparse(d.pop("endDate"))

        address = d.pop("address", UNSET)

        recipient_name = d.pop("recipientName", UNSET)

        listing_admin_v2eoi = cls(
            end_date=end_date,
            address=address,
            recipient_name=recipient_name,
        )

        listing_admin_v2eoi.additional_properties = d
        return listing_admin_v2eoi

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
