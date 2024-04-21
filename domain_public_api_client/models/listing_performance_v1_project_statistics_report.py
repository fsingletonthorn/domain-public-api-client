from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_performance_v1_daily_project_statistics import ListingPerformanceV1DailyProjectStatistics
    from ..models.listing_performance_v1_project_statistics import ListingPerformanceV1ProjectStatistics


T = TypeVar("T", bound="ListingPerformanceV1ProjectStatisticsReport")


@_attrs_define
class ListingPerformanceV1ProjectStatisticsReport:
    """
    Attributes:
        summary (Union[Unset, ListingPerformanceV1ProjectStatistics]):
        daily_breakdown (Union[List['ListingPerformanceV1DailyProjectStatistics'], None, Unset]): Listing statistic
            breakdown for the period by days
    """

    summary: Union[Unset, "ListingPerformanceV1ProjectStatistics"] = UNSET
    daily_breakdown: Union[List["ListingPerformanceV1DailyProjectStatistics"], None, Unset] = UNSET

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

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary
        if daily_breakdown is not UNSET:
            field_dict["dailyBreakdown"] = daily_breakdown

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listing_performance_v1_daily_project_statistics import ListingPerformanceV1DailyProjectStatistics
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

        listing_performance_v1_project_statistics_report = cls(
            summary=summary,
            daily_breakdown=daily_breakdown,
        )

        return listing_performance_v1_project_statistics_report
