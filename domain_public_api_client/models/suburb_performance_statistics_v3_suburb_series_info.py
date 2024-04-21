from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.suburb_performance_statistics_v3_suburb_series_info_values_type_0 import (
        SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0,
    )


T = TypeVar("T", bound="SuburbPerformanceStatisticsV3SuburbSeriesInfo")


@_attrs_define
class SuburbPerformanceStatisticsV3SuburbSeriesInfo:
    """APMAPIModelsSuburbV2SeriesInfoModel

    Attributes:
        year (Union[None, Unset, int]): Gets or Sets Year
        month (Union[None, Unset, int]): Gets or Sets Month
        values (Union['SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0', None, Unset]): Gets or Sets Values
    """

    year: Union[None, Unset, int] = UNSET
    month: Union[None, Unset, int] = UNSET
    values: Union["SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0", None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.suburb_performance_statistics_v3_suburb_series_info_values_type_0 import (
            SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0,
        )

        year: Union[None, Unset, int]
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        month: Union[None, Unset, int]
        if isinstance(self.month, Unset):
            month = UNSET
        else:
            month = self.month

        values: Union[Dict[str, Any], None, Unset]
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0):
            values = self.values.to_dict()
        else:
            values = self.values

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if year is not UNSET:
            field_dict["year"] = year
        if month is not UNSET:
            field_dict["month"] = month
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.suburb_performance_statistics_v3_suburb_series_info_values_type_0 import (
            SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0,
        )

        d = src_dict.copy()

        def _parse_year(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        year = _parse_year(d.pop("year", UNSET))

        def _parse_month(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        month = _parse_month(d.pop("month", UNSET))

        def _parse_values(
            data: object,
        ) -> Union["SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                values_type_0 = SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0.from_dict(data)

                return values_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0", None, Unset], data)

        values = _parse_values(d.pop("values", UNSET))

        suburb_performance_statistics_v3_suburb_series_info = cls(
            year=year,
            month=month,
            values=values,
        )

        return suburb_performance_statistics_v3_suburb_series_info
