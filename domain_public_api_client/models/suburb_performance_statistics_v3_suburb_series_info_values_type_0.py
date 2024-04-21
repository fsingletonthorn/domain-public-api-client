from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0")


@_attrs_define
class SuburbPerformanceStatisticsV3SuburbSeriesInfoValuesType0:
    """Gets or Sets Values"""

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        suburb_performance_statistics_v3_suburb_series_info_values_type_0 = cls()

        suburb_performance_statistics_v3_suburb_series_info_values_type_0.additional_properties = d
        return suburb_performance_statistics_v3_suburb_series_info_values_type_0

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
