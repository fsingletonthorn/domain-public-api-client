from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_performance_v1_daily_project_statistics import ListingPerformanceV1DailyProjectStatistics
    from ..models.listing_performance_v1_project_listing_statistics import ListingPerformanceV1ProjectListingStatistics
    from ..models.listing_performance_v1_project_statistics import ListingPerformanceV1ProjectStatistics


T = TypeVar("T", bound="ListingPerformanceV1ProjectListingStatisticsReport")


@_attrs_define
class ListingPerformanceV1ProjectListingStatisticsReport:
    """
    Attributes:
        summary (Union[Unset, ListingPerformanceV1ProjectStatistics]):
        daily_breakdown (Union[List['ListingPerformanceV1DailyProjectStatistics'], None, Unset]): Listing statistic
            breakdown for the period by days
        listing_breakdown (Union[List['ListingPerformanceV1ProjectListingStatistics'], None, Unset]): Listing statistic
            breakdown for the period by listings
    """

    summary: Union[Unset, "ListingPerformanceV1ProjectStatistics"] = UNSET
    daily_breakdown: Union[List["ListingPerformanceV1DailyProjectStatistics"], None, Unset] = UNSET
    listing_breakdown: Union[List["ListingPerformanceV1ProjectListingStatistics"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        daily_breakdown: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.daily_breakdown, Unset):
            daily_breakdown = UNSET
        elif isinstance(self.daily_breakdown, list):
            daily_breakdown = []
            for daily_breakdown_type_0_item_data in self.daily_breakdown:
                daily_breakdown_type_0_item = daily_breakdown_type_0_item_data.to_dict()
                daily_breakdown.append(daily_breakdown_type_0_item)

        else:
            daily_breakdown = self.daily_breakdown

        listing_breakdown: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.listing_breakdown, Unset):
            listing_breakdown = UNSET
        elif isinstance(self.listing_breakdown, list):
            listing_breakdown = []
            for listing_breakdown_type_0_item_data in self.listing_breakdown:
                listing_breakdown_type_0_item = listing_breakdown_type_0_item_data.to_dict()
                listing_breakdown.append(listing_breakdown_type_0_item)

        else:
            listing_breakdown = self.listing_breakdown

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary
        if daily_breakdown is not UNSET:
            field_dict["dailyBreakdown"] = daily_breakdown
        if listing_breakdown is not UNSET:
            field_dict["listingBreakdown"] = listing_breakdown

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listing_performance_v1_daily_project_statistics import ListingPerformanceV1DailyProjectStatistics
        from ..models.listing_performance_v1_project_listing_statistics import (
            ListingPerformanceV1ProjectListingStatistics,
        )
        from ..models.listing_performance_v1_project_statistics import ListingPerformanceV1ProjectStatistics

        d = src_dict.copy()
        _summary = d.pop("summary", UNSET)
        summary: Union[Unset, ListingPerformanceV1ProjectStatistics]
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = ListingPerformanceV1ProjectStatistics.from_dict(_summary)

        def _parse_daily_breakdown(
            data: object,
        ) -> Union[List["ListingPerformanceV1DailyProjectStatistics"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                daily_breakdown_type_0 = []
                _daily_breakdown_type_0 = data
                for daily_breakdown_type_0_item_data in _daily_breakdown_type_0:
                    daily_breakdown_type_0_item = ListingPerformanceV1DailyProjectStatistics.from_dict(
                        daily_breakdown_type_0_item_data
                    )

                    daily_breakdown_type_0.append(daily_breakdown_type_0_item)

                return daily_breakdown_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ListingPerformanceV1DailyProjectStatistics"], None, Unset], data)

        daily_breakdown = _parse_daily_breakdown(d.pop("dailyBreakdown", UNSET))

        def _parse_listing_breakdown(
            data: object,
        ) -> Union[List["ListingPerformanceV1ProjectListingStatistics"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                listing_breakdown_type_0 = []
                _listing_breakdown_type_0 = data
                for listing_breakdown_type_0_item_data in _listing_breakdown_type_0:
                    listing_breakdown_type_0_item = ListingPerformanceV1ProjectListingStatistics.from_dict(
                        listing_breakdown_type_0_item_data
                    )

                    listing_breakdown_type_0.append(listing_breakdown_type_0_item)

                return listing_breakdown_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ListingPerformanceV1ProjectListingStatistics"], None, Unset], data)

        listing_breakdown = _parse_listing_breakdown(d.pop("listingBreakdown", UNSET))

        listing_performance_v1_project_listing_statistics_report = cls(
            summary=summary,
            daily_breakdown=daily_breakdown,
            listing_breakdown=listing_breakdown,
        )

        return listing_performance_v1_project_listing_statistics_report
