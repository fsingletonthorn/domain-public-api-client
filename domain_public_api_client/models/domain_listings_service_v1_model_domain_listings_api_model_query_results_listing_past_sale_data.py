from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPastSaleData")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPastSaleData:
    """
    Attributes:
        unit_number (Union[Unset, str]):
        street_number (Union[Unset, str]):
        street (Union[Unset, str]):
        suburb (Union[Unset, str]):
        postcode (Union[Unset, str]):
        state (Union[Unset, str]):
        display_address (Union[Unset, str]):
        date_of_sale (Union[Unset, str]):
        sold_price (Union[Unset, int]):
    """

    unit_number: Union[Unset, str] = UNSET
    street_number: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    suburb: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    display_address: Union[Unset, str] = UNSET
    date_of_sale: Union[Unset, str] = UNSET
    sold_price: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unit_number = self.unit_number

        street_number = self.street_number

        street = self.street

        suburb = self.suburb

        postcode = self.postcode

        state = self.state

        display_address = self.display_address

        date_of_sale = self.date_of_sale

        sold_price = self.sold_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if street is not UNSET:
            field_dict["street"] = street
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if state is not UNSET:
            field_dict["state"] = state
        if display_address is not UNSET:
            field_dict["displayAddress"] = display_address
        if date_of_sale is not UNSET:
            field_dict["dateOfSale"] = date_of_sale
        if sold_price is not UNSET:
            field_dict["soldPrice"] = sold_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unit_number = d.pop("unitNumber", UNSET)

        street_number = d.pop("streetNumber", UNSET)

        street = d.pop("street", UNSET)

        suburb = d.pop("suburb", UNSET)

        postcode = d.pop("postcode", UNSET)

        state = d.pop("state", UNSET)

        display_address = d.pop("displayAddress", UNSET)

        date_of_sale = d.pop("dateOfSale", UNSET)

        sold_price = d.pop("soldPrice", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_past_sale_data = cls(
            unit_number=unit_number,
            street_number=street_number,
            street=street,
            suburb=suburb,
            postcode=postcode,
            state=state,
            display_address=display_address,
            date_of_sale=date_of_sale,
            sold_price=sold_price,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_past_sale_data.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_past_sale_data

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
