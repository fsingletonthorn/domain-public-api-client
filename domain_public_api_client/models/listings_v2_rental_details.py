import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.listings_v2_rental_details_rental_method import ListingsV2RentalDetailsRentalMethod
from ..models.listings_v2_rental_details_source import ListingsV2RentalDetailsSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV2RentalDetails")


@_attrs_define
class ListingsV2RentalDetails:
    """The rental detail's of the listing in case of it being for rent or leased

    Attributes:
        rental_method (Union[Unset, ListingsV2RentalDetailsRentalMethod]): Gets or Sets RentalMethod
        source (Union[Unset, ListingsV2RentalDetailsSource]): Gets or Sets Source
        leased_date (Union[None, Unset, datetime.datetime]): The Date the listing was leased. DateTime is in a local
            timezone.
        leased_price (Union[None, Unset, int]): The last leased price entered by the Advertiser  This price will only be
            visible if allowed by the Advertiser  and the listing as been leased
        can_display_price (Union[None, Unset, bool]): Indicates whether this instance can display price
        leased_months (Union[None, Unset, int]): The number of months the property was last leased for  This will only
            be visible if the property has been leased
        term_of_lease_from (Union[None, Unset, int]): Lease term range from
        term_of_lease_to (Union[None, Unset, int]): Lease term range to
        lease_outgoings (Union[None, Unset, int]): Outgoing cost of current lease
    """

    rental_method: Union[Unset, ListingsV2RentalDetailsRentalMethod] = UNSET
    source: Union[Unset, ListingsV2RentalDetailsSource] = UNSET
    leased_date: Union[None, Unset, datetime.datetime] = UNSET
    leased_price: Union[None, Unset, int] = UNSET
    can_display_price: Union[None, Unset, bool] = UNSET
    leased_months: Union[None, Unset, int] = UNSET
    term_of_lease_from: Union[None, Unset, int] = UNSET
    term_of_lease_to: Union[None, Unset, int] = UNSET
    lease_outgoings: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        rental_method: Union[Unset, str] = UNSET
        if not isinstance(self.rental_method, Unset):
            rental_method = self.rental_method.value

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        leased_date: Union[None, Unset, str]
        if isinstance(self.leased_date, Unset):
            leased_date = UNSET
        elif isinstance(self.leased_date, datetime.datetime):
            leased_date = self.leased_date.isoformat()
        else:
            leased_date = self.leased_date

        leased_price: Union[None, Unset, int]
        if isinstance(self.leased_price, Unset):
            leased_price = UNSET
        else:
            leased_price = self.leased_price

        can_display_price: Union[None, Unset, bool]
        if isinstance(self.can_display_price, Unset):
            can_display_price = UNSET
        else:
            can_display_price = self.can_display_price

        leased_months: Union[None, Unset, int]
        if isinstance(self.leased_months, Unset):
            leased_months = UNSET
        else:
            leased_months = self.leased_months

        term_of_lease_from: Union[None, Unset, int]
        if isinstance(self.term_of_lease_from, Unset):
            term_of_lease_from = UNSET
        else:
            term_of_lease_from = self.term_of_lease_from

        term_of_lease_to: Union[None, Unset, int]
        if isinstance(self.term_of_lease_to, Unset):
            term_of_lease_to = UNSET
        else:
            term_of_lease_to = self.term_of_lease_to

        lease_outgoings: Union[None, Unset, int]
        if isinstance(self.lease_outgoings, Unset):
            lease_outgoings = UNSET
        else:
            lease_outgoings = self.lease_outgoings

        field_dict: Dict[str, Any] = {}
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
        rental_method: Union[Unset, ListingsV2RentalDetailsRentalMethod]
        if isinstance(_rental_method, Unset):
            rental_method = UNSET
        else:
            rental_method = ListingsV2RentalDetailsRentalMethod(_rental_method)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ListingsV2RentalDetailsSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ListingsV2RentalDetailsSource(_source)

        def _parse_leased_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                leased_date_type_0 = isoparse(data)

                return leased_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        leased_date = _parse_leased_date(d.pop("leasedDate", UNSET))

        def _parse_leased_price(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        leased_price = _parse_leased_price(d.pop("leasedPrice", UNSET))

        def _parse_can_display_price(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        can_display_price = _parse_can_display_price(d.pop("canDisplayPrice", UNSET))

        def _parse_leased_months(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        leased_months = _parse_leased_months(d.pop("leasedMonths", UNSET))

        def _parse_term_of_lease_from(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        term_of_lease_from = _parse_term_of_lease_from(d.pop("termOfLeaseFrom", UNSET))

        def _parse_term_of_lease_to(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        term_of_lease_to = _parse_term_of_lease_to(d.pop("termOfLeaseTo", UNSET))

        def _parse_lease_outgoings(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        lease_outgoings = _parse_lease_outgoings(d.pop("leaseOutgoings", UNSET))

        listings_v2_rental_details = cls(
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

        return listings_v2_rental_details
