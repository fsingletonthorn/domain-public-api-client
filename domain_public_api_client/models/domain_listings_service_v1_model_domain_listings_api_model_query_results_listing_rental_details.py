import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_rental_details_rental_method import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetailsRentalMethod,
)
from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_rental_details_source import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetailsSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetails")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetails:
    """
    Attributes:
        rental_method (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetailsRentalMethod]):
        source (Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetailsSource]):
        leased_date (Union[Unset, datetime.datetime]):
        leased_price (Union[Unset, int]):
        can_display_price (Union[Unset, bool]):
        leased_months (Union[Unset, int]):
        term_of_lease_from (Union[Unset, int]):
        term_of_lease_to (Union[Unset, int]):
        lease_outgoings (Union[Unset, int]):
    """

    rental_method: Union[
        Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetailsRentalMethod
    ] = UNSET
    source: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetailsSource] = (
        UNSET
    )
    leased_date: Union[Unset, datetime.datetime] = UNSET
    leased_price: Union[Unset, int] = UNSET
    can_display_price: Union[Unset, bool] = UNSET
    leased_months: Union[Unset, int] = UNSET
    term_of_lease_from: Union[Unset, int] = UNSET
    term_of_lease_to: Union[Unset, int] = UNSET
    lease_outgoings: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rental_method: Union[Unset, str] = UNSET
        if not isinstance(self.rental_method, Unset):
            rental_method = self.rental_method.value

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        leased_date: Union[Unset, str] = UNSET
        if not isinstance(self.leased_date, Unset):
            leased_date = self.leased_date.isoformat()

        leased_price = self.leased_price

        can_display_price = self.can_display_price

        leased_months = self.leased_months

        term_of_lease_from = self.term_of_lease_from

        term_of_lease_to = self.term_of_lease_to

        lease_outgoings = self.lease_outgoings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rental_method is not UNSET:
            field_dict["rentalMethod"] = rental_method
        if source is not UNSET:
            field_dict["source"] = source
        if leased_date is not UNSET:
            field_dict["leasedDate"] = leased_date
        if leased_price is not UNSET:
            field_dict["leasedPrice"] = leased_price
        if can_display_price is not UNSET:
            field_dict["canDisplayPrice"] = can_display_price
        if leased_months is not UNSET:
            field_dict["leasedMonths"] = leased_months
        if term_of_lease_from is not UNSET:
            field_dict["termOfLeaseFrom"] = term_of_lease_from
        if term_of_lease_to is not UNSET:
            field_dict["termOfLeaseTo"] = term_of_lease_to
        if lease_outgoings is not UNSET:
            field_dict["leaseOutgoings"] = lease_outgoings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _rental_method = d.pop("rentalMethod", UNSET)
        rental_method: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetailsRentalMethod
        ]
        if isinstance(_rental_method, Unset):
            rental_method = UNSET
        else:
            rental_method = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetailsRentalMethod(
                    _rental_method
                )
            )

        _source = d.pop("source", UNSET)
        source: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetailsSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingRentalDetailsSource(_source)

        _leased_date = d.pop("leasedDate", UNSET)
        leased_date: Union[Unset, datetime.datetime]
        if isinstance(_leased_date, Unset):
            leased_date = UNSET
        else:
            leased_date = isoparse(_leased_date)

        leased_price = d.pop("leasedPrice", UNSET)

        can_display_price = d.pop("canDisplayPrice", UNSET)

        leased_months = d.pop("leasedMonths", UNSET)

        term_of_lease_from = d.pop("termOfLeaseFrom", UNSET)

        term_of_lease_to = d.pop("termOfLeaseTo", UNSET)

        lease_outgoings = d.pop("leaseOutgoings", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_rental_details = cls(
            rental_method=rental_method,
            source=source,
            leased_date=leased_date,
            leased_price=leased_price,
            can_display_price=can_display_price,
            leased_months=leased_months,
            term_of_lease_from=term_of_lease_from,
            term_of_lease_to=term_of_lease_to,
            lease_outgoings=lease_outgoings,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_rental_details.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_rental_details

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
