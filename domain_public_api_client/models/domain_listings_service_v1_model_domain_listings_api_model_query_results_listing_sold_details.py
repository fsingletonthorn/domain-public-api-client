import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sold_details_sold_action import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetailsSoldAction,
)
from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sold_details_source import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetailsSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetails:
    """
    Attributes:
        sold_action (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetailsSoldAction]):
        source (Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetailsSource]):
        sold_price (Union[Unset, int]):
        government_recorded_sold_price (Union[Unset, int]):
        sold_date (Union[Unset, datetime.datetime]):
        can_display_price (Union[Unset, bool]):
    """

    sold_action: Union[
        Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetailsSoldAction
    ] = UNSET
    source: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetailsSource] = UNSET
    sold_price: Union[Unset, int] = UNSET
    government_recorded_sold_price: Union[Unset, int] = UNSET
    sold_date: Union[Unset, datetime.datetime] = UNSET
    can_display_price: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sold_action: Union[Unset, str] = UNSET
        if not isinstance(self.sold_action, Unset):
            sold_action = self.sold_action.value

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        sold_price = self.sold_price

        government_recorded_sold_price = self.government_recorded_sold_price

        sold_date: Union[Unset, str] = UNSET
        if not isinstance(self.sold_date, Unset):
            sold_date = self.sold_date.isoformat()

        can_display_price = self.can_display_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sold_action is not UNSET:
            field_dict["soldAction"] = sold_action
        if source is not UNSET:
            field_dict["source"] = source
        if sold_price is not UNSET:
            field_dict["soldPrice"] = sold_price
        if government_recorded_sold_price is not UNSET:
            field_dict["governmentRecordedSoldPrice"] = government_recorded_sold_price
        if sold_date is not UNSET:
            field_dict["soldDate"] = sold_date
        if can_display_price is not UNSET:
            field_dict["canDisplayPrice"] = can_display_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sold_action = d.pop("soldAction", UNSET)
        sold_action: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetailsSoldAction
        ]
        if isinstance(_sold_action, Unset):
            sold_action = UNSET
        else:
            sold_action = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetailsSoldAction(
                _sold_action
            )

        _source = d.pop("source", UNSET)
        source: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetailsSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingSoldDetailsSource(_source)

        sold_price = d.pop("soldPrice", UNSET)

        government_recorded_sold_price = d.pop("governmentRecordedSoldPrice", UNSET)

        _sold_date = d.pop("soldDate", UNSET)
        sold_date: Union[Unset, datetime.datetime]
        if isinstance(_sold_date, Unset):
            sold_date = UNSET
        else:
            sold_date = isoparse(_sold_date)

        can_display_price = d.pop("canDisplayPrice", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sold_details = cls(
            sold_action=sold_action,
            source=source,
            sold_price=sold_price,
            government_recorded_sold_price=government_recorded_sold_price,
            sold_date=sold_date,
            can_display_price=can_display_price,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sold_details.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_sold_details

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
