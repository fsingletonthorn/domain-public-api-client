from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listing_admin_service_v1_model_address_display_option import (
    DomainListingAdminServiceV1ModelAddressDisplayOption,
)
from ..models.domain_listing_admin_service_v1_model_address_state import DomainListingAdminServiceV1ModelAddressState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listing_admin_service_v1_model_geo_location import DomainListingAdminServiceV1ModelGeoLocation


T = TypeVar("T", bound="DomainListingAdminServiceV1ModelAddress")


@_attrs_define
class DomainListingAdminServiceV1ModelAddress:
    """Address structure for property

    Attributes:
        display_option (Union[Unset, DomainListingAdminServiceV1ModelAddressDisplayOption]): What granularity to display
            the properties location at. For residential listings, the accepted displayOption values are `FullAddress`,
            `StreetAndSuburb` or `SuburbOnly`.
        state (Union[Unset, DomainListingAdminServiceV1ModelAddressState]): State
        unit_number (Union[Unset, str]): Unit number for apartments, maximum 30 characters
        street (Union[Unset, str]): Street name, maximum 100 characters
        suggested_geo_location (Union[Unset, DomainListingAdminServiceV1ModelGeoLocation]): Contains geocoding of an
            address
        street_number (Union[Unset, str]): Street number, maximum 20 characters
        suburb (Union[Unset, str]): Suburb name , maximum 50 characters
        postcode (Union[Unset, str]): Postcode
    """

    display_option: Union[Unset, DomainListingAdminServiceV1ModelAddressDisplayOption] = UNSET
    state: Union[Unset, DomainListingAdminServiceV1ModelAddressState] = UNSET
    unit_number: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    suggested_geo_location: Union[Unset, "DomainListingAdminServiceV1ModelGeoLocation"] = UNSET
    street_number: Union[Unset, str] = UNSET
    suburb: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_option: Union[Unset, str] = UNSET
        if not isinstance(self.display_option, Unset):
            display_option = self.display_option.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        unit_number = self.unit_number

        street = self.street

        suggested_geo_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.suggested_geo_location, Unset):
            suggested_geo_location = self.suggested_geo_location.to_dict()

        street_number = self.street_number

        suburb = self.suburb

        postcode = self.postcode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_option is not UNSET:
            field_dict["displayOption"] = display_option
        if state is not UNSET:
            field_dict["state"] = state
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if street is not UNSET:
            field_dict["street"] = street
        if suggested_geo_location is not UNSET:
            field_dict["suggestedGeoLocation"] = suggested_geo_location
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if postcode is not UNSET:
            field_dict["postcode"] = postcode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_listing_admin_service_v1_model_geo_location import (
            DomainListingAdminServiceV1ModelGeoLocation,
        )

        d = src_dict.copy()
        _display_option = d.pop("displayOption", UNSET)
        display_option: Union[Unset, DomainListingAdminServiceV1ModelAddressDisplayOption]
        if isinstance(_display_option, Unset):
            display_option = UNSET
        else:
            display_option = DomainListingAdminServiceV1ModelAddressDisplayOption(_display_option)

        _state = d.pop("state", UNSET)
        state: Union[Unset, DomainListingAdminServiceV1ModelAddressState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DomainListingAdminServiceV1ModelAddressState(_state)

        unit_number = d.pop("unitNumber", UNSET)

        street = d.pop("street", UNSET)

        _suggested_geo_location = d.pop("suggestedGeoLocation", UNSET)
        suggested_geo_location: Union[Unset, DomainListingAdminServiceV1ModelGeoLocation]
        if isinstance(_suggested_geo_location, Unset):
            suggested_geo_location = UNSET
        else:
            suggested_geo_location = DomainListingAdminServiceV1ModelGeoLocation.from_dict(_suggested_geo_location)

        street_number = d.pop("streetNumber", UNSET)

        suburb = d.pop("suburb", UNSET)

        postcode = d.pop("postcode", UNSET)

        domain_listing_admin_service_v1_model_address = cls(
            display_option=display_option,
            state=state,
            unit_number=unit_number,
            street=street,
            suggested_geo_location=suggested_geo_location,
            street_number=street_number,
            suburb=suburb,
            postcode=postcode,
        )

        domain_listing_admin_service_v1_model_address.additional_properties = d
        return domain_listing_admin_service_v1_model_address

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
