from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyEnrichmentV2AddressBasic")


@_attrs_define
class PropertyEnrichmentV2AddressBasic:
    """Address of property

    Attributes:
        flat_number (Union[None, Unset, str]):
        street_number (Union[Unset, str]):
        street_name (Union[Unset, str]):
        street_type (Union[None, Unset, str]):
        street_type_long (Union[None, Unset, str]):
        suburb (Union[Unset, str]):
        postcode (Union[Unset, str]):
        state (Union[Unset, str]):
    """

    flat_number: Union[None, Unset, str] = UNSET
    street_number: Union[Unset, str] = UNSET
    street_name: Union[Unset, str] = UNSET
    street_type: Union[None, Unset, str] = UNSET
    street_type_long: Union[None, Unset, str] = UNSET
    suburb: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        flat_number: Union[None, Unset, str]
        if isinstance(self.flat_number, Unset):
            flat_number = UNSET
        else:
            flat_number = self.flat_number

        street_number = self.street_number

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

        suburb = self.suburb

        postcode = self.postcode

        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if flat_number is not UNSET:
            field_dict["flatNumber"] = flat_number
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
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_flat_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        flat_number = _parse_flat_number(d.pop("flatNumber", UNSET))

        street_number = d.pop("streetNumber", UNSET)

        street_name = d.pop("streetName", UNSET)

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

        suburb = d.pop("suburb", UNSET)

        postcode = d.pop("postcode", UNSET)

        state = d.pop("state", UNSET)

        property_enrichment_v2_address_basic = cls(
            flat_number=flat_number,
            street_number=street_number,
            street_name=street_name,
            street_type=street_type,
            street_type_long=street_type_long,
            suburb=suburb,
            postcode=postcode,
            state=state,
        )

        return property_enrichment_v2_address_basic
