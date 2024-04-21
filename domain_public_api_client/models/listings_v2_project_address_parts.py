from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.listings_v2_project_address_parts_display_type import ListingsV2ProjectAddressPartsDisplayType
from ..models.listings_v2_project_address_parts_state_abbreviation import ListingsV2ProjectAddressPartsStateAbbreviation
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV2ProjectAddressParts")


@_attrs_define
class ListingsV2ProjectAddressParts:
    """Project address parts

    Attributes:
        state_abbreviation (Union[Unset, ListingsV2ProjectAddressPartsStateAbbreviation]): Gets or Sets
            StateAbbreviation
        display_type (Union[Unset, ListingsV2ProjectAddressPartsDisplayType]): Gets or Sets DisplayType
        street_number (Union[None, Unset, str]): Street number
        unit_number (Union[None, Unset, str]): Unit number.
        street (Union[None, Unset, str]): Street address
        suburb (Union[None, Unset, str]): Suburb of the address
        suburb_id (Union[None, Unset, int]): Domain suburb identifier for address lookup via the domain location api
        postcode (Union[None, Unset, str]): Postcode of the address
        display_address (Union[None, Unset, str]): Advertiser's preference in displaying their listing's address
        street2 (Union[None, Unset, str]): Street 2
        latitude (Union[None, Unset, float]): Latitude
        longitude (Union[None, Unset, float]): Longitude
    """

    state_abbreviation: Union[Unset, ListingsV2ProjectAddressPartsStateAbbreviation] = UNSET
    display_type: Union[Unset, ListingsV2ProjectAddressPartsDisplayType] = UNSET
    street_number: Union[None, Unset, str] = UNSET
    unit_number: Union[None, Unset, str] = UNSET
    street: Union[None, Unset, str] = UNSET
    suburb: Union[None, Unset, str] = UNSET
    suburb_id: Union[None, Unset, int] = UNSET
    postcode: Union[None, Unset, str] = UNSET
    display_address: Union[None, Unset, str] = UNSET
    street2: Union[None, Unset, str] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET

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

        street2: Union[None, Unset, str]
        if isinstance(self.street2, Unset):
            street2 = UNSET
        else:
            street2 = self.street2

        latitude: Union[None, Unset, float]
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: Union[None, Unset, float]
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

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
        if street2 is not UNSET:
            field_dict["street2"] = street2
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state_abbreviation = d.pop("stateAbbreviation", UNSET)
        state_abbreviation: Union[Unset, ListingsV2ProjectAddressPartsStateAbbreviation]
        if isinstance(_state_abbreviation, Unset):
            state_abbreviation = UNSET
        else:
            state_abbreviation = ListingsV2ProjectAddressPartsStateAbbreviation(_state_abbreviation)

        _display_type = d.pop("displayType", UNSET)
        display_type: Union[Unset, ListingsV2ProjectAddressPartsDisplayType]
        if isinstance(_display_type, Unset):
            display_type = UNSET
        else:
            display_type = ListingsV2ProjectAddressPartsDisplayType(_display_type)

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

        def _parse_street2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street2 = _parse_street2(d.pop("street2", UNSET))

        def _parse_latitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        listings_v2_project_address_parts = cls(
            state_abbreviation=state_abbreviation,
            display_type=display_type,
            street_number=street_number,
            unit_number=unit_number,
            street=street,
            suburb=suburb,
            suburb_id=suburb_id,
            postcode=postcode,
            display_address=display_address,
            street2=street2,
            latitude=latitude,
            longitude=longitude,
        )

        return listings_v2_project_address_parts
