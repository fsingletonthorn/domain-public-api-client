from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_area_unit import ListingAdminV2AreaUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2Area")


@_attrs_define
class ListingAdminV2Area:
    """Area information, Either single value or from and To must be provided

    Attributes:
        value (Union[Unset, float]): Area. Will be rounded to 2 decimals.
        from_ (Union[Unset, float]): Minimum area
        to (Union[Unset, float]): Maximum area
        unit (Union[Unset, ListingAdminV2AreaUnit]): Unit of measure, defaults to SquareMetres if not provided.
    """

    value: Union[Unset, float] = UNSET
    from_: Union[Unset, float] = UNSET
    to: Union[Unset, float] = UNSET
    unit: Union[Unset, ListingAdminV2AreaUnit] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        from_ = self.from_

        to = self.to

        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, ListingAdminV2AreaUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = ListingAdminV2AreaUnit(_unit)

        listing_admin_v2_area = cls(
            value=value,
            from_=from_,
            to=to,
            unit=unit,
        )

        listing_admin_v2_area.additional_properties = d
        return listing_admin_v2_area

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
