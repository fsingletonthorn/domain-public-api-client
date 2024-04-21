from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsBusinessPhoneNumber")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsBusinessPhoneNumber:
    r"""Phone number details

    Attributes:
        display_label (Union[Unset, str]): Diplay label
        type (Union[Unset, str]): Type: \"fax\", \"mobile\", \"telephone\"
        number (Union[Unset, str]): Phone number
    """

    display_label: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_label = self.display_label

        type = self.type

        number = self.number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_label is not UNSET:
            field_dict["displayLabel"] = display_label
        if type is not UNSET:
            field_dict["type"] = type
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_label = d.pop("displayLabel", UNSET)

        type = d.pop("type", UNSET)

        number = d.pop("number", UNSET)

        domain_public_adapter_web_api_models_v1_listings_business_phone_number = cls(
            display_label=display_label,
            type=type,
            number=number,
        )

        domain_public_adapter_web_api_models_v1_listings_business_phone_number.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_business_phone_number

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
