import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2CommercialAuction")


@_attrs_define
class ListingAdminV2CommercialAuction:
    """Commercial Auction Details

    Attributes:
        date_time (datetime.datetime): Date of the auction. format: yyyy-MM-ddTHH:mm:ss
        auction_terms (Union[Unset, str]): Terms for the auctions, up to 200 characters. Example: "10% deposit, balance
            60 days"
        location (Union[Unset, str]): Optional. Venue for the Auction. String max 100 characters. If the Location is
            omitted, or included but empty, the Venue will default to "On Site".
        url (Union[Unset, str]): Optional on-line auction URL. Must be a valid URL and maximum 255 characters. If an
            empty string is received, the property will be re-set.
    """

    date_time: datetime.datetime
    auction_terms: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_time = self.date_time.isoformat()

        auction_terms = self.auction_terms

        location = self.location

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dateTime": date_time,
            }
        )
        if auction_terms is not UNSET:
            field_dict["auctionTerms"] = auction_terms
        if location is not UNSET:
            field_dict["location"] = location
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date_time = isoparse(d.pop("dateTime"))

        auction_terms = d.pop("auctionTerms", UNSET)

        location = d.pop("location", UNSET)

        url = d.pop("url", UNSET)

        listing_admin_v2_commercial_auction = cls(
            date_time=date_time,
            auction_terms=auction_terms,
            location=location,
            url=url,
        )

        listing_admin_v2_commercial_auction.additional_properties = d
        return listing_admin_v2_commercial_auction

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
