from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationTypeaheadV1AddressComponents")


@_attrs_define
class LocationTypeaheadV1AddressComponents:
    """
    Attributes:
        unit_number (Union[None, Unset, str]):
        street_number (Union[None, Unset, str]):
        street_name (Union[None, Unset, str]):
        street_type (Union[None, Unset, str]):
        street_type_long (Union[None, Unset, str]):
        suburb (Union[None, Unset, str]):
        post_code (Union[None, Unset, str]):
        state (Union[None, Unset, str]):
    """

    unit_number: Union[None, Unset, str] = UNSET
    street_number: Union[None, Unset, str] = UNSET
    street_name: Union[None, Unset, str] = UNSET
    street_type: Union[None, Unset, str] = UNSET
    street_type_long: Union[None, Unset, str] = UNSET
    suburb: Union[None, Unset, str] = UNSET
    post_code: Union[None, Unset, str] = UNSET
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

        street_type_long: Union[None, Unset, str]
        if isinstance(self.street_type_long, Unset):
            street_type_long = UNSET
        else:
            street_type_long = self.street_type_long

        suburb: Union[None, Unset, str]
        if isinstance(self.suburb, Unset):
            suburb = UNSET
        else:
            suburb = self.suburb

        post_code: Union[None, Unset, str]
        if isinstance(self.post_code, Unset):
            post_code = UNSET
        else:
            post_code = self.post_code

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
        if street_type_long is not UNSET:
            field_dict["streetTypeLong"] = street_type_long
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if post_code is not UNSET:
            field_dict["postCode"] = post_code
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

        def _parse_street_type_long(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_type_long = _parse_street_type_long(d.pop("streetTypeLong", UNSET))

        def _parse_suburb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suburb = _parse_suburb(d.pop("suburb", UNSET))

        def _parse_post_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        post_code = _parse_post_code(d.pop("postCode", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        location_typeahead_v1_address_components = cls(
            unit_number=unit_number,
            street_number=street_number,
            street_name=street_name,
            street_type=street_type,
            street_type_long=street_type_long,
            suburb=suburb,
            post_code=post_code,
            state=state,
        )

        return location_typeahead_v1_address_components
