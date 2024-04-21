from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.social_boost_v1_listing_rate_info_product_listing_level import (
    SocialBoostV1ListingRateInfoProductListingLevel,
)
from ..models.social_boost_v1_listing_rate_info_product_listing_rule import (
    SocialBoostV1ListingRateInfoProductListingRule,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialBoostV1ListingRateInfo")


@_attrs_define
class SocialBoostV1ListingRateInfo:
    """ListingRateInfo

    Attributes:
        product_listing_level (Union[Unset, SocialBoostV1ListingRateInfoProductListingLevel]): Gets or Sets
            ProductListingLevel
        product_listing_rule (Union[Unset, SocialBoostV1ListingRateInfoProductListingRule]): Gets or Sets
            ProductListingRule
        booking_product_id (Union[None, Unset, int]): Gets or Sets BookingProductId
        booking_product_rate_id (Union[None, Unset, int]): Gets or Sets BookingProductRateId
        booking_product_name (Union[None, Unset, str]): Gets or Sets BookingProductName
        duration_in_days (Union[None, Unset, int]): Gets or Sets DurationInDays
        cost_ex_gst (Union[None, Unset, float]): Gets or Sets CostExGst
        cost_inc_gst (Union[None, Unset, float]): Gets or Sets CostIncGst
        zone_id (Union[None, Unset, int]): Gets or Sets ZoneId
        product_attributes (Union[None, Unset, str]): Gets or Sets ProductAttributes
        rate_attributes (Union[None, Unset, str]): Gets or Sets RateAttributes
        booking_method (Union[None, Unset, str]): Gets or Sets BookingMethod
        product_for_rural (Union[None, Unset, bool]): Gets or Sets ProductForRural
    """

    product_listing_level: Union[Unset, SocialBoostV1ListingRateInfoProductListingLevel] = UNSET
    product_listing_rule: Union[Unset, SocialBoostV1ListingRateInfoProductListingRule] = UNSET
    booking_product_id: Union[None, Unset, int] = UNSET
    booking_product_rate_id: Union[None, Unset, int] = UNSET
    booking_product_name: Union[None, Unset, str] = UNSET
    duration_in_days: Union[None, Unset, int] = UNSET
    cost_ex_gst: Union[None, Unset, float] = UNSET
    cost_inc_gst: Union[None, Unset, float] = UNSET
    zone_id: Union[None, Unset, int] = UNSET
    product_attributes: Union[None, Unset, str] = UNSET
    rate_attributes: Union[None, Unset, str] = UNSET
    booking_method: Union[None, Unset, str] = UNSET
    product_for_rural: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        product_listing_level: Union[Unset, str] = UNSET
        if not isinstance(self.product_listing_level, Unset):
            product_listing_level = self.product_listing_level.value

        product_listing_rule: Union[Unset, str] = UNSET
        if not isinstance(self.product_listing_rule, Unset):
            product_listing_rule = self.product_listing_rule.value

        booking_product_id: Union[None, Unset, int]
        if isinstance(self.booking_product_id, Unset):
            booking_product_id = UNSET
        else:
            booking_product_id = self.booking_product_id

        booking_product_rate_id: Union[None, Unset, int]
        if isinstance(self.booking_product_rate_id, Unset):
            booking_product_rate_id = UNSET
        else:
            booking_product_rate_id = self.booking_product_rate_id

        booking_product_name: Union[None, Unset, str]
        if isinstance(self.booking_product_name, Unset):
            booking_product_name = UNSET
        else:
            booking_product_name = self.booking_product_name

        duration_in_days: Union[None, Unset, int]
        if isinstance(self.duration_in_days, Unset):
            duration_in_days = UNSET
        else:
            duration_in_days = self.duration_in_days

        cost_ex_gst: Union[None, Unset, float]
        if isinstance(self.cost_ex_gst, Unset):
            cost_ex_gst = UNSET
        else:
            cost_ex_gst = self.cost_ex_gst

        cost_inc_gst: Union[None, Unset, float]
        if isinstance(self.cost_inc_gst, Unset):
            cost_inc_gst = UNSET
        else:
            cost_inc_gst = self.cost_inc_gst

        zone_id: Union[None, Unset, int]
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        else:
            zone_id = self.zone_id

        product_attributes: Union[None, Unset, str]
        if isinstance(self.product_attributes, Unset):
            product_attributes = UNSET
        else:
            product_attributes = self.product_attributes

        rate_attributes: Union[None, Unset, str]
        if isinstance(self.rate_attributes, Unset):
            rate_attributes = UNSET
        else:
            rate_attributes = self.rate_attributes

        booking_method: Union[None, Unset, str]
        if isinstance(self.booking_method, Unset):
            booking_method = UNSET
        else:
            booking_method = self.booking_method

        product_for_rural: Union[None, Unset, bool]
        if isinstance(self.product_for_rural, Unset):
            product_for_rural = UNSET
        else:
            product_for_rural = self.product_for_rural

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if product_listing_level is not UNSET:
            field_dict["productListingLevel"] = product_listing_level
        if product_listing_rule is not UNSET:
            field_dict["productListingRule"] = product_listing_rule
        if booking_product_id is not UNSET:
            field_dict["bookingProductId"] = booking_product_id
        if booking_product_rate_id is not UNSET:
            field_dict["bookingProductRateId"] = booking_product_rate_id
        if booking_product_name is not UNSET:
            field_dict["bookingProductName"] = booking_product_name
        if duration_in_days is not UNSET:
            field_dict["durationInDays"] = duration_in_days
        if cost_ex_gst is not UNSET:
            field_dict["costExGst"] = cost_ex_gst
        if cost_inc_gst is not UNSET:
            field_dict["costIncGst"] = cost_inc_gst
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if product_attributes is not UNSET:
            field_dict["productAttributes"] = product_attributes
        if rate_attributes is not UNSET:
            field_dict["rateAttributes"] = rate_attributes
        if booking_method is not UNSET:
            field_dict["bookingMethod"] = booking_method
        if product_for_rural is not UNSET:
            field_dict["productForRural"] = product_for_rural

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _product_listing_level = d.pop("productListingLevel", UNSET)
        product_listing_level: Union[Unset, SocialBoostV1ListingRateInfoProductListingLevel]
        if isinstance(_product_listing_level, Unset):
            product_listing_level = UNSET
        else:
            product_listing_level = SocialBoostV1ListingRateInfoProductListingLevel(_product_listing_level)

        _product_listing_rule = d.pop("productListingRule", UNSET)
        product_listing_rule: Union[Unset, SocialBoostV1ListingRateInfoProductListingRule]
        if isinstance(_product_listing_rule, Unset):
            product_listing_rule = UNSET
        else:
            product_listing_rule = SocialBoostV1ListingRateInfoProductListingRule(_product_listing_rule)

        def _parse_booking_product_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        booking_product_id = _parse_booking_product_id(d.pop("bookingProductId", UNSET))

        def _parse_booking_product_rate_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        booking_product_rate_id = _parse_booking_product_rate_id(d.pop("bookingProductRateId", UNSET))

        def _parse_booking_product_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        booking_product_name = _parse_booking_product_name(d.pop("bookingProductName", UNSET))

        def _parse_duration_in_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        duration_in_days = _parse_duration_in_days(d.pop("durationInDays", UNSET))

        def _parse_cost_ex_gst(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost_ex_gst = _parse_cost_ex_gst(d.pop("costExGst", UNSET))

        def _parse_cost_inc_gst(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost_inc_gst = _parse_cost_inc_gst(d.pop("costIncGst", UNSET))

        def _parse_zone_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        zone_id = _parse_zone_id(d.pop("zoneId", UNSET))

        def _parse_product_attributes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        product_attributes = _parse_product_attributes(d.pop("productAttributes", UNSET))

        def _parse_rate_attributes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rate_attributes = _parse_rate_attributes(d.pop("rateAttributes", UNSET))

        def _parse_booking_method(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        booking_method = _parse_booking_method(d.pop("bookingMethod", UNSET))

        def _parse_product_for_rural(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        product_for_rural = _parse_product_for_rural(d.pop("productForRural", UNSET))

        social_boost_v1_listing_rate_info = cls(
            product_listing_level=product_listing_level,
            product_listing_rule=product_listing_rule,
            booking_product_id=booking_product_id,
            booking_product_rate_id=booking_product_rate_id,
            booking_product_name=booking_product_name,
            duration_in_days=duration_in_days,
            cost_ex_gst=cost_ex_gst,
            cost_inc_gst=cost_inc_gst,
            zone_id=zone_id,
            product_attributes=product_attributes,
            rate_attributes=rate_attributes,
            booking_method=booking_method,
            product_for_rural=product_for_rural,
        )

        return social_boost_v1_listing_rate_info
