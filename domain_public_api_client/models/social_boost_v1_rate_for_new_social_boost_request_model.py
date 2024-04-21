import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.social_boost_v1_rate_for_new_social_boost_request_model_channel import (
    SocialBoostV1RateForNewSocialBoostRequestModelChannel,
)
from ..models.social_boost_v1_rate_for_new_social_boost_request_model_listing_type import (
    SocialBoostV1RateForNewSocialBoostRequestModelListingType,
)
from ..models.social_boost_v1_rate_for_new_social_boost_request_model_property_type import (
    SocialBoostV1RateForNewSocialBoostRequestModelPropertyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialBoostV1RateForNewSocialBoostRequestModel")


@_attrs_define
class SocialBoostV1RateForNewSocialBoostRequestModel:
    """
    Attributes:
        agency_id (int): Id of the agency for whom rates are to be calculated.
        agent_first_name (str): The first name of the primary agent associated with the listing.
        agent_last_name (str): The last name of the primary agent associated with the listing
        agent_email (str): The email of the primary agent associated with the listing.
        suburb (str): Suburb for which rates are to be calculated.
        postcode (str): Postcode for which rates are to be calculated.
        state (str): State for which rates are to be calculated
        property_type (SocialBoostV1RateForNewSocialBoostRequestModelPropertyType): The property type of the listing
            e.g. House
        is_rural (bool): Whether to return the normal or rural rates
        listing_type (SocialBoostV1RateForNewSocialBoostRequestModelListingType): Type of the listing whether sale or
            rent
        price (float): The value of the listing
        channel (SocialBoostV1RateForNewSocialBoostRequestModelChannel): The intended channel of the listing.
        booking_start_date (Union[None, Unset, datetime.datetime]): Date at which the booking will start. Defaults to
            today. Allows for returning future contracts/price changes.
    """

    agency_id: int
    agent_first_name: str
    agent_last_name: str
    agent_email: str
    suburb: str
    postcode: str
    state: str
    property_type: SocialBoostV1RateForNewSocialBoostRequestModelPropertyType
    is_rural: bool
    listing_type: SocialBoostV1RateForNewSocialBoostRequestModelListingType
    price: float
    channel: SocialBoostV1RateForNewSocialBoostRequestModelChannel
    booking_start_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agency_id = self.agency_id

        agent_first_name = self.agent_first_name

        agent_last_name = self.agent_last_name

        agent_email = self.agent_email

        suburb = self.suburb

        postcode = self.postcode

        state = self.state

        property_type = self.property_type.value

        is_rural = self.is_rural

        listing_type = self.listing_type.value

        price = self.price

        channel = self.channel.value

        booking_start_date: Union[None, Unset, str]
        if isinstance(self.booking_start_date, Unset):
            booking_start_date = UNSET
        elif isinstance(self.booking_start_date, datetime.datetime):
            booking_start_date = self.booking_start_date.isoformat()
        else:
            booking_start_date = self.booking_start_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "agencyId": agency_id,
                "agentFirstName": agent_first_name,
                "agentLastName": agent_last_name,
                "agentEmail": agent_email,
                "suburb": suburb,
                "postcode": postcode,
                "state": state,
                "propertyType": property_type,
                "isRural": is_rural,
                "listingType": listing_type,
                "price": price,
                "channel": channel,
            }
        )
        if booking_start_date is not UNSET:
            field_dict["bookingStartDate"] = booking_start_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agency_id = d.pop("agencyId")

        agent_first_name = d.pop("agentFirstName")

        agent_last_name = d.pop("agentLastName")

        agent_email = d.pop("agentEmail")

        suburb = d.pop("suburb")

        postcode = d.pop("postcode")

        state = d.pop("state")

        property_type = SocialBoostV1RateForNewSocialBoostRequestModelPropertyType(d.pop("propertyType"))

        is_rural = d.pop("isRural")

        listing_type = SocialBoostV1RateForNewSocialBoostRequestModelListingType(d.pop("listingType"))

        price = d.pop("price")

        channel = SocialBoostV1RateForNewSocialBoostRequestModelChannel(d.pop("channel"))

        def _parse_booking_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                booking_start_date_type_0 = isoparse(data)

                return booking_start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        booking_start_date = _parse_booking_start_date(d.pop("bookingStartDate", UNSET))

        social_boost_v1_rate_for_new_social_boost_request_model = cls(
            agency_id=agency_id,
            agent_first_name=agent_first_name,
            agent_last_name=agent_last_name,
            agent_email=agent_email,
            suburb=suburb,
            postcode=postcode,
            state=state,
            property_type=property_type,
            is_rural=is_rural,
            listing_type=listing_type,
            price=price,
            channel=channel,
            booking_start_date=booking_start_date,
        )

        return social_boost_v1_rate_for_new_social_boost_request_model
