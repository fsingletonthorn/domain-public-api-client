import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SalesResultsV1CityResultsSummary")


@_attrs_define
class SalesResultsV1CityResultsSummary:
    """summary of report for a given city

    Attributes:
        number_listed_for_auction (Union[None, Unset, int]): total number for auction
        number_withdrawn (Union[None, Unset, int]): number withdrawn
        number_unreported (Union[None, Unset, int]): number not reported
        number_auctioned (Union[None, Unset, int]): number auctioned
        number_sold (Union[None, Unset, int]): solde number
        total_sales (Union[None, Unset, float]): total
        median (Union[None, Unset, int]): median for auctioned
        adj_clearance_rate (Union[None, Unset, float]): adjusted clearance rate
        auctioned_date (Union[None, Unset, datetime.datetime]): Date when results were published
        last_modified_date_time (Union[None, Unset, datetime.datetime]): When the results were last modified in Redis.
            Useful for knowing  when the listing enhancer last ran.  If Redis is not use this will be the same as Published
            Date
    """

    number_listed_for_auction: Union[None, Unset, int] = UNSET
    number_withdrawn: Union[None, Unset, int] = UNSET
    number_unreported: Union[None, Unset, int] = UNSET
    number_auctioned: Union[None, Unset, int] = UNSET
    number_sold: Union[None, Unset, int] = UNSET
    total_sales: Union[None, Unset, float] = UNSET
    median: Union[None, Unset, int] = UNSET
    adj_clearance_rate: Union[None, Unset, float] = UNSET
    auctioned_date: Union[None, Unset, datetime.datetime] = UNSET
    last_modified_date_time: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        number_listed_for_auction: Union[None, Unset, int]
        if isinstance(self.number_listed_for_auction, Unset):
            number_listed_for_auction = UNSET
        else:
            number_listed_for_auction = self.number_listed_for_auction

        number_withdrawn: Union[None, Unset, int]
        if isinstance(self.number_withdrawn, Unset):
            number_withdrawn = UNSET
        else:
            number_withdrawn = self.number_withdrawn

        number_unreported: Union[None, Unset, int]
        if isinstance(self.number_unreported, Unset):
            number_unreported = UNSET
        else:
            number_unreported = self.number_unreported

        number_auctioned: Union[None, Unset, int]
        if isinstance(self.number_auctioned, Unset):
            number_auctioned = UNSET
        else:
            number_auctioned = self.number_auctioned

        number_sold: Union[None, Unset, int]
        if isinstance(self.number_sold, Unset):
            number_sold = UNSET
        else:
            number_sold = self.number_sold

        total_sales: Union[None, Unset, float]
        if isinstance(self.total_sales, Unset):
            total_sales = UNSET
        else:
            total_sales = self.total_sales

        median: Union[None, Unset, int]
        if isinstance(self.median, Unset):
            median = UNSET
        else:
            median = self.median

        adj_clearance_rate: Union[None, Unset, float]
        if isinstance(self.adj_clearance_rate, Unset):
            adj_clearance_rate = UNSET
        else:
            adj_clearance_rate = self.adj_clearance_rate

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
        if number_listed_for_auction is not UNSET:
            field_dict["numberListedForAuction"] = number_listed_for_auction
        if number_withdrawn is not UNSET:
            field_dict["numberWithdrawn"] = number_withdrawn
        if number_unreported is not UNSET:
            field_dict["numberUnreported"] = number_unreported
        if number_auctioned is not UNSET:
            field_dict["numberAuctioned"] = number_auctioned
        if number_sold is not UNSET:
            field_dict["numberSold"] = number_sold
        if total_sales is not UNSET:
            field_dict["totalSales"] = total_sales
        if median is not UNSET:
            field_dict["median"] = median
        if adj_clearance_rate is not UNSET:
            field_dict["adjClearanceRate"] = adj_clearance_rate
        if auctioned_date is not UNSET:
            field_dict["auctionedDate"] = auctioned_date
        if last_modified_date_time is not UNSET:
            field_dict["lastModifiedDateTime"] = last_modified_date_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_number_listed_for_auction(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_listed_for_auction = _parse_number_listed_for_auction(d.pop("numberListedForAuction", UNSET))

        def _parse_number_withdrawn(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_withdrawn = _parse_number_withdrawn(d.pop("numberWithdrawn", UNSET))

        def _parse_number_unreported(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_unreported = _parse_number_unreported(d.pop("numberUnreported", UNSET))

        def _parse_number_auctioned(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_auctioned = _parse_number_auctioned(d.pop("numberAuctioned", UNSET))

        def _parse_number_sold(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_sold = _parse_number_sold(d.pop("numberSold", UNSET))

        def _parse_total_sales(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_sales = _parse_total_sales(d.pop("totalSales", UNSET))

        def _parse_median(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        median = _parse_median(d.pop("median", UNSET))

        def _parse_adj_clearance_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        adj_clearance_rate = _parse_adj_clearance_rate(d.pop("adjClearanceRate", UNSET))

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

        sales_results_v1_city_results_summary = cls(
            number_listed_for_auction=number_listed_for_auction,
            number_withdrawn=number_withdrawn,
            number_unreported=number_unreported,
            number_auctioned=number_auctioned,
            number_sold=number_sold,
            total_sales=total_sales,
            median=median,
            adj_clearance_rate=adj_clearance_rate,
            auctioned_date=auctioned_date,
            last_modified_date_time=last_modified_date_time,
        )

        return sales_results_v1_city_results_summary
