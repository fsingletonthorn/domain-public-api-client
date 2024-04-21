from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.demographics_v2_demographics_item import DemographicsV2DemographicsItem


T = TypeVar("T", bound="DemographicsV2Demographics")


@_attrs_define
class DemographicsV2Demographics:
    """DemographicsModel

    Attributes:
        type (Union[None, Unset, str]): Gets or Sets Type
        total (Union[None, Unset, int]): Gets or Sets Total
        year (Union[None, Unset, int]): Gets or Sets Year
        items (Union[List['DemographicsV2DemographicsItem'], None, Unset]): Gets or Sets Items
    """

    type: Union[None, Unset, str] = UNSET
    total: Union[None, Unset, int] = UNSET
    year: Union[None, Unset, int] = UNSET
    items: Union[List["DemographicsV2DemographicsItem"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type: Union[None, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        else:
            type = self.type

        total: Union[None, Unset, int]
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        year: Union[None, Unset, int]
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        items: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if total is not UNSET:
            field_dict["total"] = total
        if year is not UNSET:
            field_dict["year"] = year
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.demographics_v2_demographics_item import DemographicsV2DemographicsItem

        d = src_dict.copy()

        def _parse_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type = _parse_type(d.pop("type", UNSET))

        def _parse_total(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total = _parse_total(d.pop("total", UNSET))

        def _parse_year(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        year = _parse_year(d.pop("year", UNSET))

        def _parse_items(data: object) -> Union[List["DemographicsV2DemographicsItem"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = DemographicsV2DemographicsItem.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["DemographicsV2DemographicsItem"], None, Unset], data)

        items = _parse_items(d.pop("items", UNSET))

        demographics_v2_demographics = cls(
            type=type,
            total=total,
            year=year,
            items=items,
        )

        return demographics_v2_demographics
