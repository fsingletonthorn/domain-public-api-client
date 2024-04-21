import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_auction_schedule import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionSchedule,
    )


T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionDetails")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionDetails:
    """
    Attributes:
        auction_schedule (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionSchedule]):
        auctioned_price (Union[Unset, int]):
        auctioned_date (Union[Unset, datetime.datetime]):
    """

    auction_schedule: Union[
        Unset, "DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionSchedule"
    ] = UNSET
    auctioned_price: Union[Unset, int] = UNSET
    auctioned_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auction_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auction_schedule, Unset):
            auction_schedule = self.auction_schedule.to_dict()

        auctioned_price = self.auctioned_price

        auctioned_date: Union[Unset, str] = UNSET
        if not isinstance(self.auctioned_date, Unset):
            auctioned_date = self.auctioned_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auction_schedule is not UNSET:
            field_dict["auctionSchedule"] = auction_schedule
        if auctioned_price is not UNSET:
            field_dict["auctionedPrice"] = auctioned_price
        if auctioned_date is not UNSET:
            field_dict["auctionedDate"] = auctioned_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_auction_schedule import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionSchedule,
        )

        d = src_dict.copy()
        _auction_schedule = d.pop("auctionSchedule", UNSET)
        auction_schedule: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionSchedule
        ]
        if isinstance(_auction_schedule, Unset):
            auction_schedule = UNSET
        else:
            auction_schedule = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAuctionSchedule.from_dict(
                    _auction_schedule
                )
            )

        auctioned_price = d.pop("auctionedPrice", UNSET)

        _auctioned_date = d.pop("auctionedDate", UNSET)
        auctioned_date: Union[Unset, datetime.datetime]
        if isinstance(_auctioned_date, Unset):
            auctioned_date = UNSET
        else:
            auctioned_date = isoparse(_auctioned_date)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_auction_details = cls(
            auction_schedule=auction_schedule,
            auctioned_price=auctioned_price,
            auctioned_date=auctioned_date,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_auction_details.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_auction_details

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
