from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_land_area_unit import ListingAdminV2LandAreaUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2LandArea")


@_attrs_define
class ListingAdminV2LandArea:
    """Area information, Either single value or from and To must be provided

    Attributes:
        unit (ListingAdminV2LandAreaUnit): Unit of measure
        value (Union[Unset, float]): Area. Will be rounded to 2 decimals.
        from_ (Union[Unset, float]): Minimum area
        to (Union[Unset, float]): Maximum area
    """

    unit: ListingAdminV2LandAreaUnit
    value: Union[Unset, float] = UNSET
    from_: Union[Unset, float] = UNSET
    to: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit = self.unit.value

        value = self.value

        from_ = self.from_

        to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unit": unit,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit = ListingAdminV2LandAreaUnit(d.pop("unit"))

        value = d.pop("value", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        listing_admin_v2_land_area = cls(
            unit=unit,
            value=value,
            from_=from_,
            to=to,
        )

        listing_admin_v2_land_area.additional_properties = d
        return listing_admin_v2_land_area

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
