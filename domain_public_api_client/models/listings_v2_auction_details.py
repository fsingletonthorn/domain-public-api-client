import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listings_v2_auction_schedule import ListingsV2AuctionSchedule


T = TypeVar("T", bound="ListingsV2AuctionDetails")


@_attrs_define
class ListingsV2AuctionDetails:
    """The detail's of the auction in case of a listing for sale being auctioned or sold by auction

    Attributes:
        auction_schedule (Union[Unset, ListingsV2AuctionSchedule]): Encapsulates the details of a Property being
            Auctioned.
        auctioned_price (Union[None, Unset, int]): The auctioned price entered by the Advertiser.  This price will only
            be visible if allowed by the Advertiser  and the listing as been auctioned
        auctioned_date (Union[None, Unset, datetime.datetime]): The listing's last auctioned date and time specified by
            the Advertiser.  This will only be visible if the listing has been auctioned.  DateTime is in a local timezone.
    """

    auction_schedule: Union[Unset, "ListingsV2AuctionSchedule"] = UNSET
    auctioned_price: Union[None, Unset, int] = UNSET
    auctioned_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        auction_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auction_schedule, Unset):
            auction_schedule = self.auction_schedule.to_dict()

        auctioned_price: Union[None, Unset, int]
        if isinstance(self.auctioned_price, Unset):
            auctioned_price = UNSET
        else:
            auctioned_price = self.auctioned_price

        auctioned_date: Union[None, Unset, str]
        if isinstance(self.auctioned_date, Unset):
            auctioned_date = UNSET
        elif isinstance(self.auctioned_date, datetime.datetime):
            auctioned_date = self.auctioned_date.isoformat()
        else:
            auctioned_date = self.auctioned_date

        field_dict: Dict[str, Any] = {}
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
        from ..models.listings_v2_auction_schedule import ListingsV2AuctionSchedule

        d = src_dict.copy()
        _auction_schedule = d.pop("auctionSchedule", UNSET)
        auction_schedule: Union[Unset, ListingsV2AuctionSchedule]
        if isinstance(_auction_schedule, Unset):
            auction_schedule = UNSET
        else:
            auction_schedule = ListingsV2AuctionSchedule.from_dict(_auction_schedule)

        def _parse_auctioned_price(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        auctioned_price = _parse_auctioned_price(d.pop("auctionedPrice", UNSET))

        def _parse_auctioned_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auctioned_date_type_0 = isoparse(data)

                return auctioned_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        auctioned_date = _parse_auctioned_date(d.pop("auctionedDate", UNSET))

        listings_v2_auction_details = cls(
            auction_schedule=auction_schedule,
            auctioned_price=auctioned_price,
            auctioned_date=auctioned_date,
        )

        return listings_v2_auction_details
