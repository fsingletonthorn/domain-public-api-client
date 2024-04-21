import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionSchedule")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionSchedule:
    """
    Attributes:
        location_description (Union[Unset, str]):
        opening_date_time (Union[Unset, datetime.datetime]):
        terms (Union[Unset, str]):
    """

    location_description: Union[Unset, str] = UNSET
    opening_date_time: Union[Unset, datetime.datetime] = UNSET
    terms: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location_description = self.location_description

        opening_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.opening_date_time, Unset):
            opening_date_time = self.opening_date_time.isoformat()

        terms = self.terms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location_description is not UNSET:
            field_dict["locationDescription"] = location_description
        if opening_date_time is not UNSET:
            field_dict["openingDateTime"] = opening_date_time
        if terms is not UNSET:
            field_dict["terms"] = terms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        location_description = d.pop("locationDescription", UNSET)

        _opening_date_time = d.pop("openingDateTime", UNSET)
        opening_date_time: Union[Unset, datetime.datetime]
        if isinstance(_opening_date_time, Unset):
            opening_date_time = UNSET
        else:
            opening_date_time = isoparse(_opening_date_time)

        terms = d.pop("terms", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_auction_schedule = cls(
            location_description=location_description,
            opening_date_time=opening_date_time,
            terms=terms,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_auction_schedule.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_auction_schedule

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
