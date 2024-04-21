import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.listings_v1_sold_details_sold_action import ListingsV1SoldDetailsSoldAction
from ..models.listings_v1_sold_details_source import ListingsV1SoldDetailsSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV1SoldDetails")


@_attrs_define
class ListingsV1SoldDetails:
    """Sold details in the case of the listing being sold.

    Attributes:
        sold_action (Union[Unset, ListingsV1SoldDetailsSoldAction]): Gets or Sets SoldAction
        source (Union[Unset, ListingsV1SoldDetailsSource]): Gets or Sets Source
        sold_price (Union[None, Unset, int]): The last sold price entered by the Advertiser.  This price will only be
            visible if allowed by the Advertiser  and the listing as been sold
        government_recorded_sold_price (Union[None, Unset, int]): The government recorded sold price sourced from APM
        sold_date (Union[None, Unset, datetime.datetime]): The Date the listing was sold. DateTime is in a local
            timezone.
        can_display_price (Union[None, Unset, bool]): Indicates whether this instance can display price
    """

    sold_action: Union[Unset, ListingsV1SoldDetailsSoldAction] = UNSET
    source: Union[Unset, ListingsV1SoldDetailsSource] = UNSET
    sold_price: Union[None, Unset, int] = UNSET
    government_recorded_sold_price: Union[None, Unset, int] = UNSET
    sold_date: Union[None, Unset, datetime.datetime] = UNSET
    can_display_price: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sold_action: Union[Unset, str] = UNSET
        if not isinstance(self.sold_action, Unset):
            sold_action = self.sold_action.value

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        sold_price: Union[None, Unset, int]
        if isinstance(self.sold_price, Unset):
            sold_price = UNSET
        else:
            sold_price = self.sold_price

        government_recorded_sold_price: Union[None, Unset, int]
        if isinstance(self.government_recorded_sold_price, Unset):
            government_recorded_sold_price = UNSET
        else:
            government_recorded_sold_price = self.government_recorded_sold_price

        sold_date: Union[None, Unset, str]
        if isinstance(self.sold_date, Unset):
            sold_date = UNSET
        elif isinstance(self.sold_date, datetime.datetime):
            sold_date = self.sold_date.isoformat()
        else:
            sold_date = self.sold_date

        can_display_price: Union[None, Unset, bool]
        if isinstance(self.can_display_price, Unset):
            can_display_price = UNSET
        else:
            can_display_price = self.can_display_price

        field_dict: Dict[str, Any] = {}
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
        sold_action: Union[Unset, ListingsV1SoldDetailsSoldAction]
        if isinstance(_sold_action, Unset):
            sold_action = UNSET
        else:
            sold_action = ListingsV1SoldDetailsSoldAction(_sold_action)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ListingsV1SoldDetailsSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ListingsV1SoldDetailsSource(_source)

        def _parse_sold_price(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sold_price = _parse_sold_price(d.pop("soldPrice", UNSET))

        def _parse_government_recorded_sold_price(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        government_recorded_sold_price = _parse_government_recorded_sold_price(
            d.pop("governmentRecordedSoldPrice", UNSET)
        )

        def _parse_sold_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sold_date_type_0 = isoparse(data)

                return sold_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        sold_date = _parse_sold_date(d.pop("soldDate", UNSET))

        def _parse_can_display_price(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        can_display_price = _parse_can_display_price(d.pop("canDisplayPrice", UNSET))

        listings_v1_sold_details = cls(
            sold_action=sold_action,
            source=source,
            sold_price=sold_price,
            government_recorded_sold_price=government_recorded_sold_price,
            sold_date=sold_date,
            can_display_price=can_display_price,
        )

        return listings_v1_sold_details
