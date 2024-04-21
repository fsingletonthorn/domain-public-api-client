import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SalesResultsV1CityResultsDate")


@_attrs_define
class SalesResultsV1CityResultsDate:
    """last date when results were updated

    Attributes:
        auctioned_date (Union[None, Unset, datetime.datetime]): Date when results were published
        last_modified_date_time (Union[None, Unset, datetime.datetime]): When the results were last modified in Redis.
            Useful for knowing  when the listing enhancer last ran.  If Redis is not use this will be the same as Published
            Date
    """

    auctioned_date: Union[None, Unset, datetime.datetime] = UNSET
    last_modified_date_time: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        auctioned_date: Union[None, Unset, str]
        if isinstance(self.auctioned_date, Unset):
            auctioned_date = UNSET
        elif isinstance(self.auctioned_date, datetime.datetime):
            auctioned_date = self.auctioned_date.isoformat()
        else:
            auctioned_date = self.auctioned_date

        last_modified_date_time: Union[None, Unset, str]
        if isinstance(self.last_modified_date_time, Unset):
            last_modified_date_time = UNSET
        elif isinstance(self.last_modified_date_time, datetime.datetime):
            last_modified_date_time = self.last_modified_date_time.isoformat()
        else:
            last_modified_date_time = self.last_modified_date_time

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if auctioned_date is not UNSET:
            field_dict["auctionedDate"] = auctioned_date
        if last_modified_date_time is not UNSET:
            field_dict["lastModifiedDateTime"] = last_modified_date_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_auctioned_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auctioned_date_type_0 = isoparse(data)

                return auctioned_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        auctioned_date = _parse_auctioned_date(d.pop("auctionedDate", UNSET))

        def _parse_last_modified_date_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_date_time_type_0 = isoparse(data)

                return last_modified_date_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_modified_date_time = _parse_last_modified_date_time(d.pop("lastModifiedDateTime", UNSET))

        sales_results_v1_city_results_date = cls(
            auctioned_date=auctioned_date,
            last_modified_date_time=last_modified_date_time,
        )

        return sales_results_v1_city_results_date
