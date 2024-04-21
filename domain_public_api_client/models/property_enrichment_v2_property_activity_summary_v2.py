from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.property_enrichment_v2_property_activity_summary_v2_market_status import (
    PropertyEnrichmentV2PropertyActivitySummaryV2MarketStatus,
)
from ..models.property_enrichment_v2_property_activity_summary_v2_owner_renter import (
    PropertyEnrichmentV2PropertyActivitySummaryV2OwnerRenter,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertyEnrichmentV2PropertyActivitySummaryV2")


@_attrs_define
class PropertyEnrichmentV2PropertyActivitySummaryV2:
    """Property activity summary derived from property activity events (not currently in EVENT-SCHEMAS project)

    Attributes:
        last_listed_date (Union[None, Unset, str]):
        last_sold_date (Union[None, Unset, str]):
        last_rented_date (Union[None, Unset, str]):
        last_listed_price (Union[None, Unset, float]):
        last_sold_price (Union[None, Unset, float]):
        last_rented_price (Union[None, Unset, float]):
        owner_renter (Union[Unset, PropertyEnrichmentV2PropertyActivitySummaryV2OwnerRenter]): Whether the most recent
            known activity indicates that the current resident is the owner or renter
        market_status (Union[Unset, PropertyEnrichmentV2PropertyActivitySummaryV2MarketStatus]): Whether or not the
            property is currently on the market
    """

    last_listed_date: Union[None, Unset, str] = UNSET
    last_sold_date: Union[None, Unset, str] = UNSET
    last_rented_date: Union[None, Unset, str] = UNSET
    last_listed_price: Union[None, Unset, float] = UNSET
    last_sold_price: Union[None, Unset, float] = UNSET
    last_rented_price: Union[None, Unset, float] = UNSET
    owner_renter: Union[Unset, PropertyEnrichmentV2PropertyActivitySummaryV2OwnerRenter] = UNSET
    market_status: Union[Unset, PropertyEnrichmentV2PropertyActivitySummaryV2MarketStatus] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        last_listed_date: Union[None, Unset, str]
        if isinstance(self.last_listed_date, Unset):
            last_listed_date = UNSET
        else:
            last_listed_date = self.last_listed_date

        last_sold_date: Union[None, Unset, str]
        if isinstance(self.last_sold_date, Unset):
            last_sold_date = UNSET
        else:
            last_sold_date = self.last_sold_date

        last_rented_date: Union[None, Unset, str]
        if isinstance(self.last_rented_date, Unset):
            last_rented_date = UNSET
        else:
            last_rented_date = self.last_rented_date

        last_listed_price: Union[None, Unset, float]
        if isinstance(self.last_listed_price, Unset):
            last_listed_price = UNSET
        else:
            last_listed_price = self.last_listed_price

        last_sold_price: Union[None, Unset, float]
        if isinstance(self.last_sold_price, Unset):
            last_sold_price = UNSET
        else:
            last_sold_price = self.last_sold_price

        last_rented_price: Union[None, Unset, float]
        if isinstance(self.last_rented_price, Unset):
            last_rented_price = UNSET
        else:
            last_rented_price = self.last_rented_price

        owner_renter: Union[Unset, str] = UNSET
        if not isinstance(self.owner_renter, Unset):
            owner_renter = self.owner_renter.value

        market_status: Union[Unset, str] = UNSET
        if not isinstance(self.market_status, Unset):
            market_status = self.market_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if last_listed_date is not UNSET:
            field_dict["lastListedDate"] = last_listed_date
        if last_sold_date is not UNSET:
            field_dict["lastSoldDate"] = last_sold_date
        if last_rented_date is not UNSET:
            field_dict["lastRentedDate"] = last_rented_date
        if last_listed_price is not UNSET:
            field_dict["lastListedPrice"] = last_listed_price
        if last_sold_price is not UNSET:
            field_dict["lastSoldPrice"] = last_sold_price
        if last_rented_price is not UNSET:
            field_dict["lastRentedPrice"] = last_rented_price
        if owner_renter is not UNSET:
            field_dict["ownerRenter"] = owner_renter
        if market_status is not UNSET:
            field_dict["marketStatus"] = market_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_last_listed_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_listed_date = _parse_last_listed_date(d.pop("lastListedDate", UNSET))

        def _parse_last_sold_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_sold_date = _parse_last_sold_date(d.pop("lastSoldDate", UNSET))

        def _parse_last_rented_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_rented_date = _parse_last_rented_date(d.pop("lastRentedDate", UNSET))

        def _parse_last_listed_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        last_listed_price = _parse_last_listed_price(d.pop("lastListedPrice", UNSET))

        def _parse_last_sold_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        last_sold_price = _parse_last_sold_price(d.pop("lastSoldPrice", UNSET))

        def _parse_last_rented_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        last_rented_price = _parse_last_rented_price(d.pop("lastRentedPrice", UNSET))

        _owner_renter = d.pop("ownerRenter", UNSET)
        owner_renter: Union[Unset, PropertyEnrichmentV2PropertyActivitySummaryV2OwnerRenter]
        if isinstance(_owner_renter, Unset):
            owner_renter = UNSET
        else:
            owner_renter = PropertyEnrichmentV2PropertyActivitySummaryV2OwnerRenter(_owner_renter)

        _market_status = d.pop("marketStatus", UNSET)
        market_status: Union[Unset, PropertyEnrichmentV2PropertyActivitySummaryV2MarketStatus]
        if isinstance(_market_status, Unset):
            market_status = UNSET
        else:
            market_status = PropertyEnrichmentV2PropertyActivitySummaryV2MarketStatus(_market_status)

        property_enrichment_v2_property_activity_summary_v2 = cls(
            last_listed_date=last_listed_date,
            last_sold_date=last_sold_date,
            last_rented_date=last_rented_date,
            last_listed_price=last_listed_price,
            last_sold_price=last_sold_price,
            last_rented_price=last_rented_price,
            owner_renter=owner_renter,
            market_status=market_status,
        )

        return property_enrichment_v2_property_activity_summary_v2
