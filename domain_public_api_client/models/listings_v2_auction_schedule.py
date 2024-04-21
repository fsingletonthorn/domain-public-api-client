import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV2AuctionSchedule")


@_attrs_define
class ListingsV2AuctionSchedule:
    """Encapsulates the details of a Property being Auctioned.

    Attributes:
        location_description (Union[None, Unset, str]): Description and location of the auction provided by advertiser
        opening_date_time (Union[None, Unset, datetime.datetime]): Opening date and time of the auction. e.g.
            2015-01-01T12:00:00  DateTime is in a local timezone.
        terms (Union[None, Unset, str]): Terms of the auction
        url (Union[None, Unset, str]): On-line URL of the auction
    """

    location_description: Union[None, Unset, str] = UNSET
    opening_date_time: Union[None, Unset, datetime.datetime] = UNSET
    terms: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        location_description: Union[None, Unset, str]
        if isinstance(self.location_description, Unset):
            location_description = UNSET
        else:
            location_description = self.location_description

        opening_date_time: Union[None, Unset, str]
        if isinstance(self.opening_date_time, Unset):
            opening_date_time = UNSET
        elif isinstance(self.opening_date_time, datetime.datetime):
            opening_date_time = self.opening_date_time.isoformat()
        else:
            opening_date_time = self.opening_date_time

        terms: Union[None, Unset, str]
        if isinstance(self.terms, Unset):
            terms = UNSET
        else:
            terms = self.terms

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if location_description is not UNSET:
            field_dict["locationDescription"] = location_description
        if opening_date_time is not UNSET:
            field_dict["openingDateTime"] = opening_date_time
        if terms is not UNSET:
            field_dict["terms"] = terms
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_location_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_description = _parse_location_description(d.pop("locationDescription", UNSET))

        def _parse_opening_date_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opening_date_time_type_0 = isoparse(data)

                return opening_date_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        opening_date_time = _parse_opening_date_time(d.pop("openingDateTime", UNSET))

        def _parse_terms(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        terms = _parse_terms(d.pop("terms", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        listings_v2_auction_schedule = cls(
            location_description=location_description,
            opening_date_time=opening_date_time,
            terms=terms,
            url=url,
        )

        return listings_v2_auction_schedule
