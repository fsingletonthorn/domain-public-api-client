from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.listings_v1_address_parts_display_type import ListingsV1AddressPartsDisplayType
from ..models.listings_v1_address_parts_state_abbreviation import ListingsV1AddressPartsStateAbbreviation
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV1AddressParts")


@_attrs_define
class ListingsV1AddressParts:
    """Encapsulates the parts that make up an Address

    Attributes:
        state_abbreviation (Union[Unset, ListingsV1AddressPartsStateAbbreviation]): Gets or Sets StateAbbreviation
        display_type (Union[Unset, ListingsV1AddressPartsDisplayType]): Gets or Sets DisplayType
        street_number (Union[None, Unset, str]): Street number
        unit_number (Union[None, Unset, str]): Unit number.
        street (Union[None, Unset, str]): Street address
        suburb (Union[None, Unset, str]): Suburb of the address
        suburb_id (Union[None, Unset, int]): Domain suburb identifier for address lookup via the domain location api
        postcode (Union[None, Unset, str]): Postcode of the address
        display_address (Union[None, Unset, str]): Advertiser's preference in displaying their listing's address
    """

    state_abbreviation: Union[Unset, ListingsV1AddressPartsStateAbbreviation] = UNSET
    display_type: Union[Unset, ListingsV1AddressPartsDisplayType] = UNSET
    street_number: Union[None, Unset, str] = UNSET
    unit_number: Union[None, Unset, str] = UNSET
    street: Union[None, Unset, str] = UNSET
    suburb: Union[None, Unset, str] = UNSET
    suburb_id: Union[None, Unset, int] = UNSET
    postcode: Union[None, Unset, str] = UNSET
    display_address: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        state_abbreviation: Union[Unset, str] = UNSET
        if not isinstance(self.state_abbreviation, Unset):
            state_abbreviation = self.state_abbreviation.value

        display_type: Union[Unset, str] = UNSET
        if not isinstance(self.display_type, Unset):
            display_type = self.display_type.value

        street_number: Union[None, Unset, str]
        if isinstance(self.street_number, Unset):
            street_number = UNSET
        else:
            street_number = self.street_number

        unit_number: Union[None, Unset, str]
        if isinstance(self.unit_number, Unset):
            unit_number = UNSET
        else:
            unit_number = self.unit_number

        street: Union[None, Unset, str]
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        suburb: Union[None, Unset, str]
        if isinstance(self.suburb, Unset):
            suburb = UNSET
        else:
            suburb = self.suburb

        suburb_id: Union[None, Unset, int]
        if isinstance(self.suburb_id, Unset):
            suburb_id = UNSET
        else:
            suburb_id = self.suburb_id

        postcode: Union[None, Unset, str]
        if isinstance(self.postcode, Unset):
            postcode = UNSET
        else:
            postcode = self.postcode

        display_address: Union[None, Unset, str]
        if isinstance(self.display_address, Unset):
            display_address = UNSET
        else:
            display_address = self.display_address

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if state_abbreviation is not UNSET:
            field_dict["stateAbbreviation"] = state_abbreviation
        if display_type is not UNSET:
            field_dict["displayType"] = display_type
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if street is not UNSET:
            field_dict["street"] = street
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if suburb_id is not UNSET:
            field_dict["suburbId"] = suburb_id
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if display_address is not UNSET:
            field_dict["displayAddress"] = display_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state_abbreviation = d.pop("stateAbbreviation", UNSET)
        state_abbreviation: Union[Unset, ListingsV1AddressPartsStateAbbreviation]
        if isinstance(_state_abbreviation, Unset):
            state_abbreviation = UNSET
        else:
            state_abbreviation = ListingsV1AddressPartsStateAbbreviation(_state_abbreviation)

        _display_type = d.pop("displayType", UNSET)
        display_type: Union[Unset, ListingsV1AddressPartsDisplayType]
        if isinstance(_display_type, Unset):
            display_type = UNSET
        else:
            display_type = ListingsV1AddressPartsDisplayType(_display_type)

        def _parse_street_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_number = _parse_street_number(d.pop("streetNumber", UNSET))

        def _parse_unit_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unit_number = _parse_unit_number(d.pop("unitNumber", UNSET))

        def _parse_street(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street = _parse_street(d.pop("street", UNSET))

        def _parse_suburb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suburb = _parse_suburb(d.pop("suburb", UNSET))

        def _parse_suburb_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        suburb_id = _parse_suburb_id(d.pop("suburbId", UNSET))

        def _parse_postcode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postcode = _parse_postcode(d.pop("postcode", UNSET))

        def _parse_display_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_address = _parse_display_address(d.pop("displayAddress", UNSET))

        listings_v1_address_parts = cls(
            state_abbreviation=state_abbreviation,
            display_type=display_type,
            street_number=street_number,
            unit_number=unit_number,
            street=street,
            suburb=suburb,
            suburb_id=suburb_id,
            postcode=postcode,
            display_address=display_address,
        )

        return listings_v1_address_parts
