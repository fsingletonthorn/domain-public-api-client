from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAustralianPropertyMonitorsIdentifiers",
)


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAustralianPropertyMonitorsIdentifiers:
    """
    Attributes:
        address_id (Union[Unset, int]):
        street_id (Union[Unset, int]):
        suburb_id (Union[Unset, int]):
        cadastre_id (Union[Unset, int]):
        postcode_id (Union[Unset, int]):
        state_id (Union[Unset, int]):
        state (Union[Unset, str]):
        property_type_id (Union[Unset, int]):
        property_type_category_id (Union[Unset, int]):
        flat_number (Union[Unset, str]):
        street_number (Union[Unset, str]):
    """

    address_id: Union[Unset, int] = UNSET
    street_id: Union[Unset, int] = UNSET
    suburb_id: Union[Unset, int] = UNSET
    cadastre_id: Union[Unset, int] = UNSET
    postcode_id: Union[Unset, int] = UNSET
    state_id: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    property_type_id: Union[Unset, int] = UNSET
    property_type_category_id: Union[Unset, int] = UNSET
    flat_number: Union[Unset, str] = UNSET
    street_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_id = self.address_id

        street_id = self.street_id

        suburb_id = self.suburb_id

        cadastre_id = self.cadastre_id

        postcode_id = self.postcode_id

        state_id = self.state_id

        state = self.state

        property_type_id = self.property_type_id

        property_type_category_id = self.property_type_category_id

        flat_number = self.flat_number

        street_number = self.street_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_id is not UNSET:
            field_dict["addressId"] = address_id
        if street_id is not UNSET:
            field_dict["streetId"] = street_id
        if suburb_id is not UNSET:
            field_dict["suburbId"] = suburb_id
        if cadastre_id is not UNSET:
            field_dict["cadastreId"] = cadastre_id
        if postcode_id is not UNSET:
            field_dict["postcodeId"] = postcode_id
        if state_id is not UNSET:
            field_dict["stateId"] = state_id
        if state is not UNSET:
            field_dict["state"] = state
        if property_type_id is not UNSET:
            field_dict["propertyTypeId"] = property_type_id
        if property_type_category_id is not UNSET:
            field_dict["propertyTypeCategoryId"] = property_type_category_id
        if flat_number is not UNSET:
            field_dict["flatNumber"] = flat_number
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address_id = d.pop("addressId", UNSET)

        street_id = d.pop("streetId", UNSET)

        suburb_id = d.pop("suburbId", UNSET)

        cadastre_id = d.pop("cadastreId", UNSET)

        postcode_id = d.pop("postcodeId", UNSET)

        state_id = d.pop("stateId", UNSET)

        state = d.pop("state", UNSET)

        property_type_id = d.pop("propertyTypeId", UNSET)

        property_type_category_id = d.pop("propertyTypeCategoryId", UNSET)

        flat_number = d.pop("flatNumber", UNSET)

        street_number = d.pop("streetNumber", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_australian_property_monitors_identifiers = cls(
            address_id=address_id,
            street_id=street_id,
            suburb_id=suburb_id,
            cadastre_id=cadastre_id,
            postcode_id=postcode_id,
            state_id=state_id,
            state=state,
            property_type_id=property_type_id,
            property_type_category_id=property_type_category_id,
            flat_number=flat_number,
            street_number=street_number,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_australian_property_monitors_identifiers.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_australian_property_monitors_identifiers

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
