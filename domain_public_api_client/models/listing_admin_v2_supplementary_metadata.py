from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_supplementary_metadata_measurement_unit import (
    ListingAdminV2SupplementaryMetadataMeasurementUnit,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2SupplementaryMetadata")


@_attrs_define
class ListingAdminV2SupplementaryMetadata:
    """Supplementary metadata

    Attributes:
        name (str): Name
        description (Union[Unset, str]): Description
        measurement (Union[Unset, float]): Measurement
        measurement_unit (Union[Unset, ListingAdminV2SupplementaryMetadataMeasurementUnit]): Measurement unit
    """

    name: str
    description: Union[Unset, str] = UNSET
    measurement: Union[Unset, float] = UNSET
    measurement_unit: Union[Unset, ListingAdminV2SupplementaryMetadataMeasurementUnit] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        measurement = self.measurement

        measurement_unit: Union[Unset, str] = UNSET
        if not isinstance(self.measurement_unit, Unset):
            measurement_unit = self.measurement_unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if measurement is not UNSET:
            field_dict["measurement"] = measurement
        if measurement_unit is not UNSET:
            field_dict["measurementUnit"] = measurement_unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        measurement = d.pop("measurement", UNSET)

        _measurement_unit = d.pop("measurementUnit", UNSET)
        measurement_unit: Union[Unset, ListingAdminV2SupplementaryMetadataMeasurementUnit]
        if isinstance(_measurement_unit, Unset):
            measurement_unit = UNSET
        else:
            measurement_unit = ListingAdminV2SupplementaryMetadataMeasurementUnit(_measurement_unit)

        listing_admin_v2_supplementary_metadata = cls(
            name=name,
            description=description,
            measurement=measurement,
            measurement_unit=measurement_unit,
        )

        listing_admin_v2_supplementary_metadata.additional_properties = d
        return listing_admin_v2_supplementary_metadata

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
