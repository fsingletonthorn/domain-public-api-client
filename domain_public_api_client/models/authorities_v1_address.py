from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuthoritiesV1Address")


@_attrs_define
class AuthoritiesV1Address:
    """
    Attributes:
        country (str):  Example: Australia.
        number (str):  Example: 123123/45.
        postcode (str):  Example: 2000.
        state (str):  Example: New South Wales.
        street (str):  Example: Sample St.
        suburb (str):  Example: Sydney.
    """

    country: str
    number: str
    postcode: str
    state: str
    street: str
    suburb: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        country = self.country

        number = self.number

        postcode = self.postcode

        state = self.state

        street = self.street

        suburb = self.suburb

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country": country,
                "number": number,
                "postcode": postcode,
                "state": state,
                "street": street,
                "suburb": suburb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        country = d.pop("country")

        number = d.pop("number")

        postcode = d.pop("postcode")

        state = d.pop("state")

        street = d.pop("street")

        suburb = d.pop("suburb")

        authorities_v1_address = cls(
            country=country,
            number=number,
            postcode=postcode,
            state=state,
            street=street,
            suburb=suburb,
        )

        authorities_v1_address.additional_properties = d
        return authorities_v1_address

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
