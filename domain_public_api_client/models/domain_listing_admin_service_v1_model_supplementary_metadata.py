from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listing_admin_service_v1_model_supplementary_metadata_measurement_unit import (
    DomainListingAdminServiceV1ModelSupplementaryMetadataMeasurementUnit,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelSupplementaryMetadata")


@_attrs_define
class DomainListingAdminServiceV1ModelSupplementaryMetadata:
    """Supplementary metadata

    Attributes:
        measurement_unit (Union[Unset, DomainListingAdminServiceV1ModelSupplementaryMetadataMeasurementUnit]):
            Measurement unit
        name (Union[Unset, str]): Name
        description (Union[Unset, str]): Description
        measurement (Union[Unset, float]): Measurement
    """

    measurement_unit: Union[Unset, DomainListingAdminServiceV1ModelSupplementaryMetadataMeasurementUnit] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    measurement: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        measurement_unit: Union[Unset, str] = UNSET
        if not isinstance(self.measurement_unit, Unset):
            measurement_unit = self.measurement_unit.value

        name = self.name

        description = self.description

        measurement = self.measurement

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_unit is not UNSET:
            field_dict["measurementUnit"] = measurement_unit
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if measurement is not UNSET:
            field_dict["measurement"] = measurement

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _measurement_unit = d.pop("measurementUnit", UNSET)
        measurement_unit: Union[Unset, DomainListingAdminServiceV1ModelSupplementaryMetadataMeasurementUnit]
        if isinstance(_measurement_unit, Unset):
            measurement_unit = UNSET
        else:
            measurement_unit = DomainListingAdminServiceV1ModelSupplementaryMetadataMeasurementUnit(_measurement_unit)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        measurement = d.pop("measurement", UNSET)

        domain_listing_admin_service_v1_model_supplementary_metadata = cls(
            measurement_unit=measurement_unit,
            name=name,
            description=description,
            measurement=measurement,
        )

        domain_listing_admin_service_v1_model_supplementary_metadata.additional_properties = d
        return domain_listing_admin_service_v1_model_supplementary_metadata

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
