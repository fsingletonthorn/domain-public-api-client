import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelAuction")


@_attrs_define
class DomainListingAdminServiceV1ModelAuction:
    r"""Auction Details

    Attributes:
        date_time (Union[Unset, datetime.datetime]): Date of the auction. format: yyyy-MM-ddTHH:mm:ss
        location (Union[Unset, str]): Optional. Venue for the Auction. String max 100 characters. If the Location is
            omitted, or included but empty, the Venue will default to \"On Site\".
        url (Union[Unset, str]): Optional on-line auction URL. Must be a valid URL and maximum 255 characters. If an
            empty string is received, the property will be re-set.
    """

    date_time: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_time: Union[Unset, str] = UNSET
        if not isinstance(self.date_time, Unset):
            date_time = self.date_time.isoformat()

        location = self.location

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if location is not UNSET:
            field_dict["location"] = location
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _date_time = d.pop("dateTime", UNSET)
        date_time: Union[Unset, datetime.datetime]
        if isinstance(_date_time, Unset):
            date_time = UNSET
        else:
            date_time = isoparse(_date_time)

        location = d.pop("location", UNSET)

        url = d.pop("url", UNSET)

        domain_listing_admin_service_v1_model_auction = cls(
            date_time=date_time,
            location=location,
            url=url,
        )

        domain_listing_admin_service_v1_model_auction.additional_properties = d
        return domain_listing_admin_service_v1_model_auction

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
