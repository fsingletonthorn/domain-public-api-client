from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SuburbPerformanceStatisticsV3SuburbSeriesHeader")


@_attrs_define
class SuburbPerformanceStatisticsV3SuburbSeriesHeader:
    """APMAPIModelsSuburbV2SeriesHeaderModel

    Attributes:
        suburb (Union[None, Unset, str]): Gets or Sets Suburb
        state (Union[None, Unset, str]): Gets or Sets State
        property_category (Union[None, Unset, str]): Gets or Sets PropertyCategory
    """

    suburb: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET
    property_category: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        suburb: Union[None, Unset, str]
        if isinstance(self.suburb, Unset):
            suburb = UNSET
        else:
            suburb = self.suburb

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        property_category: Union[None, Unset, str]
        if isinstance(self.property_category, Unset):
            property_category = UNSET
        else:
            property_category = self.property_category

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if state is not UNSET:
            field_dict["state"] = state
        if property_category is not UNSET:
            field_dict["propertyCategory"] = property_category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_suburb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suburb = _parse_suburb(d.pop("suburb", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_property_category(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_category = _parse_property_category(d.pop("propertyCategory", UNSET))

        suburb_performance_statistics_v3_suburb_series_header = cls(
            suburb=suburb,
            state=state,
            property_category=property_category,
        )

        return suburb_performance_statistics_v3_suburb_series_header
