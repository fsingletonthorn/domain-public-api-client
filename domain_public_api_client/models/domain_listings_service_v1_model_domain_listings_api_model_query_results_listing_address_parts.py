from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_address_parts_display_type import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressPartsDisplayType,
)
from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_address_parts_state_abbreviation import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressPartsStateAbbreviation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressParts")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressParts:
    """
    Attributes:
        state_abbreviation (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressPartsStateAbbreviation]):
        display_type (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressPartsDisplayType]):
        street_number (Union[Unset, str]):
        unit_number (Union[Unset, str]):
        street (Union[Unset, str]):
        suburb (Union[Unset, str]):
        suburb_id (Union[Unset, int]):
        postcode (Union[Unset, str]):
        display_address (Union[Unset, str]):
    """

    state_abbreviation: Union[
        Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressPartsStateAbbreviation
    ] = UNSET
    display_type: Union[
        Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressPartsDisplayType
    ] = UNSET
    street_number: Union[Unset, str] = UNSET
    unit_number: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    suburb: Union[Unset, str] = UNSET
    suburb_id: Union[Unset, int] = UNSET
    postcode: Union[Unset, str] = UNSET
    display_address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state_abbreviation: Union[Unset, str] = UNSET
        if not isinstance(self.state_abbreviation, Unset):
            state_abbreviation = self.state_abbreviation.value

        display_type: Union[Unset, str] = UNSET
        if not isinstance(self.display_type, Unset):
            display_type = self.display_type.value

        street_number = self.street_number

        unit_number = self.unit_number

        street = self.street

        suburb = self.suburb

        suburb_id = self.suburb_id

        postcode = self.postcode

        display_address = self.display_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        state_abbreviation: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressPartsStateAbbreviation
        ]
        if isinstance(_state_abbreviation, Unset):
            state_abbreviation = UNSET
        else:
            state_abbreviation = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressPartsStateAbbreviation(
                    _state_abbreviation
                )
            )

        _display_type = d.pop("displayType", UNSET)
        display_type: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressPartsDisplayType
        ]
        if isinstance(_display_type, Unset):
            display_type = UNSET
        else:
            display_type = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAddressPartsDisplayType(
                _display_type
            )

        street_number = d.pop("streetNumber", UNSET)

        unit_number = d.pop("unitNumber", UNSET)

        street = d.pop("street", UNSET)

        suburb = d.pop("suburb", UNSET)

        suburb_id = d.pop("suburbId", UNSET)

        postcode = d.pop("postcode", UNSET)

        display_address = d.pop("displayAddress", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_address_parts = cls(
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

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_address_parts.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_address_parts

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
