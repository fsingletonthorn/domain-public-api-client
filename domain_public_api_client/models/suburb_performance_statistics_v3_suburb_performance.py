from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.suburb_performance_statistics_v3_suburb_series import SuburbPerformanceStatisticsV3SuburbSeries
    from ..models.suburb_performance_statistics_v3_suburb_series_header import (
        SuburbPerformanceStatisticsV3SuburbSeriesHeader,
    )


T = TypeVar("T", bound="SuburbPerformanceStatisticsV3SuburbPerformance")


@_attrs_define
class SuburbPerformanceStatisticsV3SuburbPerformance:
    """APMAPIModelsSuburbV2SuburbPerformanceModel

    Attributes:
        header (Union[Unset, SuburbPerformanceStatisticsV3SuburbSeriesHeader]): APMAPIModelsSuburbV2SeriesHeaderModel
        series (Union[Unset, SuburbPerformanceStatisticsV3SuburbSeries]): APMAPIModelsSuburbV2SeriesModel
    """

    header: Union[Unset, "SuburbPerformanceStatisticsV3SuburbSeriesHeader"] = UNSET
    series: Union[Unset, "SuburbPerformanceStatisticsV3SuburbSeries"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        header: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        series: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if header is not UNSET:
            field_dict["header"] = header
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.suburb_performance_statistics_v3_suburb_series import SuburbPerformanceStatisticsV3SuburbSeries
        from ..models.suburb_performance_statistics_v3_suburb_series_header import (
            SuburbPerformanceStatisticsV3SuburbSeriesHeader,
        )

        d = src_dict.copy()
        _header = d.pop("header", UNSET)
        header: Union[Unset, SuburbPerformanceStatisticsV3SuburbSeriesHeader]
        if isinstance(_header, Unset):
            header = UNSET
        else:
            header = SuburbPerformanceStatisticsV3SuburbSeriesHeader.from_dict(_header)

        _series = d.pop("series", UNSET)
        series: Union[Unset, SuburbPerformanceStatisticsV3SuburbSeries]
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = SuburbPerformanceStatisticsV3SuburbSeries.from_dict(_series)

        suburb_performance_statistics_v3_suburb_performance = cls(
            header=header,
            series=series,
        )

        return suburb_performance_statistics_v3_suburb_performance
