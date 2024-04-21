from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainAvmV1Address")


@_attrs_define
class DomainAvmV1Address:
    """The Address model used.

    Attributes:
        unit_number (Union[None, Unset, str]): The unit number of the address.
        street_number (Union[None, Unset, str]): The street number of the address.
        street_name (Union[None, Unset, str]): The street name of the address.
        street_type (Union[None, Unset, str]): The street type of the address.
        locality (Union[None, Unset, str]): The suburb/locality of the address.
        postcode (Union[None, Unset, str]): The postcode of the address.
        state (Union[None, Unset, str]): The defined State or Territory in Australia (in abbreviated format) where the
            specific address is located.
    """

    unit_number: Union[None, Unset, str] = UNSET
    street_number: Union[None, Unset, str] = UNSET
    street_name: Union[None, Unset, str] = UNSET
    street_type: Union[None, Unset, str] = UNSET
    locality: Union[None, Unset, str] = UNSET
    postcode: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        unit_number: Union[None, Unset, str]
        if isinstance(self.unit_number, Unset):
            unit_number = UNSET
        else:
            unit_number = self.unit_number

        street_number: Union[None, Unset, str]
        if isinstance(self.street_number, Unset):
            street_number = UNSET
        else:
            street_number = self.street_number

        street_name: Union[None, Unset, str]
        if isinstance(self.street_name, Unset):
            street_name = UNSET
        else:
            street_name = self.street_name

        street_type: Union[None, Unset, str]
        if isinstance(self.street_type, Unset):
            street_type = UNSET
        else:
            street_type = self.street_type

        locality: Union[None, Unset, str]
        if isinstance(self.locality, Unset):
            locality = UNSET
        else:
            locality = self.locality

        postcode: Union[None, Unset, str]
        if isinstance(self.postcode, Unset):
            postcode = UNSET
        else:
            postcode = self.postcode

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if street_type is not UNSET:
            field_dict["streetType"] = street_type
        if locality is not UNSET:
            field_dict["locality"] = locality
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_unit_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unit_number = _parse_unit_number(d.pop("unitNumber", UNSET))

        def _parse_street_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_number = _parse_street_number(d.pop("streetNumber", UNSET))

        def _parse_street_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_name = _parse_street_name(d.pop("streetName", UNSET))

        def _parse_street_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_type = _parse_street_type(d.pop("streetType", UNSET))

        def _parse_locality(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        locality = _parse_locality(d.pop("locality", UNSET))

        def _parse_postcode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postcode = _parse_postcode(d.pop("postcode", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        domain_avm_v1_address = cls(
            unit_number=unit_number,
            street_number=street_number,
            street_name=street_name,
            street_type=street_type,
            locality=locality,
            postcode=postcode,
            state=state,
        )

        return domain_avm_v1_address
