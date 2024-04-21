from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_address_display_option import ListingAdminV2AddressDisplayOption
from ..models.listing_admin_v2_address_state import ListingAdminV2AddressState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_admin_v2_geo_location import ListingAdminV2GeoLocation


T = TypeVar("T", bound="ListingAdminV2Address")


@_attrs_define
class ListingAdminV2Address:
    """Address structure for property

    Attributes:
        street (str): Street name, maximum 100 characters
        suburb (str): Suburb name , maximum 50 characters
        postcode (str): Postcode
        state (ListingAdminV2AddressState): State
        unit_number (Union[Unset, str]): Unit number for apartments, maximum 30 characters
        display_option (Union[Unset, ListingAdminV2AddressDisplayOption]): What granularity to display the properties
            location at.
            For residential listings, the accepted displayOption values are "FullAddress", "StreetAndSuburb" or
            "SuburbOnly".
        suggested_geo_location (Union[Unset, ListingAdminV2GeoLocation]): Contains geocoding of an address
        street_number (Union[Unset, str]): Street number, maximum 20 characters
    """

    street: str
    suburb: str
    postcode: str
    state: ListingAdminV2AddressState
    unit_number: Union[Unset, str] = UNSET
    display_option: Union[Unset, ListingAdminV2AddressDisplayOption] = UNSET
    suggested_geo_location: Union[Unset, "ListingAdminV2GeoLocation"] = UNSET
    street_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        street = self.street

        suburb = self.suburb

        postcode = self.postcode

        state = self.state.value

        unit_number = self.unit_number

        display_option: Union[Unset, str] = UNSET
        if not isinstance(self.display_option, Unset):
            display_option = self.display_option.value

        suggested_geo_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.suggested_geo_location, Unset):
            suggested_geo_location = self.suggested_geo_location.to_dict()

        street_number = self.street_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "street": street,
                "suburb": suburb,
                "postcode": postcode,
                "state": state,
            }
        )
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if display_option is not UNSET:
            field_dict["displayOption"] = display_option
        if suggested_geo_location is not UNSET:
            field_dict["suggestedGeoLocation"] = suggested_geo_location
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listing_admin_v2_geo_location import ListingAdminV2GeoLocation

        d = src_dict.copy()
        street = d.pop("street")

        suburb = d.pop("suburb")

        postcode = d.pop("postcode")

        state = ListingAdminV2AddressState(d.pop("state"))

        unit_number = d.pop("unitNumber", UNSET)

        _display_option = d.pop("displayOption", UNSET)
        display_option: Union[Unset, ListingAdminV2AddressDisplayOption]
        if isinstance(_display_option, Unset):
            display_option = UNSET
        else:
            display_option = ListingAdminV2AddressDisplayOption(_display_option)

        _suggested_geo_location = d.pop("suggestedGeoLocation", UNSET)
        suggested_geo_location: Union[Unset, ListingAdminV2GeoLocation]
        if isinstance(_suggested_geo_location, Unset):
            suggested_geo_location = UNSET
        else:
            suggested_geo_location = ListingAdminV2GeoLocation.from_dict(_suggested_geo_location)

        street_number = d.pop("streetNumber", UNSET)

        listing_admin_v2_address = cls(
            street=street,
            suburb=suburb,
            postcode=postcode,
            state=state,
            unit_number=unit_number,
            display_option=display_option,
            suggested_geo_location=suggested_geo_location,
            street_number=street_number,
        )

        listing_admin_v2_address.additional_properties = d
        return listing_admin_v2_address

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
