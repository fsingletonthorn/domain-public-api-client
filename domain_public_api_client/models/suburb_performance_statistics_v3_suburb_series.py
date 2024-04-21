from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.suburb_performance_statistics_v3_suburb_series_info import (
        SuburbPerformanceStatisticsV3SuburbSeriesInfo,
    )


T = TypeVar("T", bound="SuburbPerformanceStatisticsV3SuburbSeries")


@_attrs_define
class SuburbPerformanceStatisticsV3SuburbSeries:
    """APMAPIModelsSuburbV2SeriesModel

    Attributes:
        series_info (Union[List['SuburbPerformanceStatisticsV3SuburbSeriesInfo'], None, Unset]): Gets or Sets SeriesInfo
    """

    series_info: Union[List["SuburbPerformanceStatisticsV3SuburbSeriesInfo"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        series_info: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.series_info, Unset):
            series_info = UNSET
        elif isinstance(self.series_info, list):
            series_info = []
            for series_info_type_0_item_data in self.series_info:
                series_info_type_0_item = series_info_type_0_item_data.to_dict()
                series_info.append(series_info_type_0_item)

        else:
            series_info = self.series_info

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if series_info is not UNSET:
            field_dict["seriesInfo"] = series_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.suburb_performance_statistics_v3_suburb_series_info import (
            SuburbPerformanceStatisticsV3SuburbSeriesInfo,
        )

        d = src_dict.copy()

        def _parse_series_info(
            data: object,
        ) -> Union[List["SuburbPerformanceStatisticsV3SuburbSeriesInfo"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_info_type_0 = []
                _series_info_type_0 = data
                for series_info_type_0_item_data in _series_info_type_0:
                    series_info_type_0_item = SuburbPerformanceStatisticsV3SuburbSeriesInfo.from_dict(
                        series_info_type_0_item_data
                    )

                    series_info_type_0.append(series_info_type_0_item)

                return series_info_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SuburbPerformanceStatisticsV3SuburbSeriesInfo"], None, Unset], data)

        series_info = _parse_series_info(d.pop("seriesInfo", UNSET))

        suburb_performance_statistics_v3_suburb_series = cls(
            series_info=series_info,
        )

        return suburb_performance_statistics_v3_suburb_series
