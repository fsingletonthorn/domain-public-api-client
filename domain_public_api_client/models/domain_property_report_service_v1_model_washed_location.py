from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPropertyReportServiceV1ModelWashedLocation")


@_attrs_define
class DomainPropertyReportServiceV1ModelWashedLocation:
    """
    Attributes:
        unit_number (Union[Unset, str]):
        street_number (Union[Unset, str]):
        street_name (Union[Unset, str]):
        street_type (Union[Unset, str]):
        suburb (Union[Unset, str]):
        postcode (Union[Unset, str]):
        state (Union[Unset, str]):
    """

    unit_number: Union[Unset, str] = UNSET
    street_number: Union[Unset, str] = UNSET
    street_name: Union[Unset, str] = UNSET
    street_type: Union[Unset, str] = UNSET
    suburb: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_number = self.unit_number

        street_number = self.street_number

        street_name = self.street_name

        street_type = self.street_type

        suburb = self.suburb

        postcode = self.postcode

        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if street_type is not UNSET:
            field_dict["streetType"] = street_type
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_number = d.pop("unitNumber", UNSET)

        street_number = d.pop("streetNumber", UNSET)

        street_name = d.pop("streetName", UNSET)

        street_type = d.pop("streetType", UNSET)

        suburb = d.pop("suburb", UNSET)

        postcode = d.pop("postcode", UNSET)

        state = d.pop("state", UNSET)

        domain_property_report_service_v1_model_washed_location = cls(
            unit_number=unit_number,
            street_number=street_number,
            street_name=street_name,
            street_type=street_type,
            suburb=suburb,
            postcode=postcode,
            state=state,
        )

        domain_property_report_service_v1_model_washed_location.additional_properties = d
        return domain_property_report_service_v1_model_washed_location

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
