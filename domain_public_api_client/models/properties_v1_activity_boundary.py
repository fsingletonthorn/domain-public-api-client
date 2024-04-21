import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropertiesV1ActivityBoundary")


@_attrs_define
class PropertiesV1ActivityBoundary:
    """
    Attributes:
        advertised_date (Union[None, Unset, datetime.datetime]): Gets or Sets AdvertisedDate
        advertised_price (Union[None, Unset, int]): Gets or Sets AdvertisedPrice
        agency (Union[None, Unset, str]): Gets or Sets Agency
        agency_colour (Union[None, Unset, str]): Gets or Sets AgencyColour
        agency_id (Union[None, Unset, int]): Gets or Sets AgencyId
        agency_logo (Union[None, Unset, str]): Gets or Sets AgencyLogo
        agency_url (Union[None, Unset, str]): Gets or Sets AgencyUrl
        apm_agency_id (Union[None, Unset, int]): Gets or Sets ApmAgencyId
        source (Union[None, Unset, str]): Gets or Sets Source
        suppress_details (Union[None, Unset, bool]): Gets or Sets SuppressDetails
        suppress_price (Union[None, Unset, bool]): Gets or Sets SuppressPrice
        type (Union[None, Unset, str]): Gets or Sets Type
        url (Union[None, Unset, str]): Gets or Sets Url
        listing_id (Union[None, Unset, int]):
    """

    advertised_date: Union[None, Unset, datetime.datetime] = UNSET
    advertised_price: Union[None, Unset, int] = UNSET
    agency: Union[None, Unset, str] = UNSET
    agency_colour: Union[None, Unset, str] = UNSET
    agency_id: Union[None, Unset, int] = UNSET
    agency_logo: Union[None, Unset, str] = UNSET
    agency_url: Union[None, Unset, str] = UNSET
    apm_agency_id: Union[None, Unset, int] = UNSET
    source: Union[None, Unset, str] = UNSET
    suppress_details: Union[None, Unset, bool] = UNSET
    suppress_price: Union[None, Unset, bool] = UNSET
    type: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    listing_id: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        advertised_date: Union[None, Unset, str]
        if isinstance(self.advertised_date, Unset):
            advertised_date = UNSET
        elif isinstance(self.advertised_date, datetime.datetime):
            advertised_date = self.advertised_date.isoformat()
        else:
            advertised_date = self.advertised_date

        advertised_price: Union[None, Unset, int]
        if isinstance(self.advertised_price, Unset):
            advertised_price = UNSET
        else:
            advertised_price = self.advertised_price

        agency: Union[None, Unset, str]
        if isinstance(self.agency, Unset):
            agency = UNSET
        else:
            agency = self.agency

        agency_colour: Union[None, Unset, str]
        if isinstance(self.agency_colour, Unset):
            agency_colour = UNSET
        else:
            agency_colour = self.agency_colour

        agency_id: Union[None, Unset, int]
        if isinstance(self.agency_id, Unset):
            agency_id = UNSET
        else:
            agency_id = self.agency_id

        agency_logo: Union[None, Unset, str]
        if isinstance(self.agency_logo, Unset):
            agency_logo = UNSET
        else:
            agency_logo = self.agency_logo

        agency_url: Union[None, Unset, str]
        if isinstance(self.agency_url, Unset):
            agency_url = UNSET
        else:
            agency_url = self.agency_url

        apm_agency_id: Union[None, Unset, int]
        if isinstance(self.apm_agency_id, Unset):
            apm_agency_id = UNSET
        else:
            apm_agency_id = self.apm_agency_id

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        suppress_details: Union[None, Unset, bool]
        if isinstance(self.suppress_details, Unset):
            suppress_details = UNSET
        else:
            suppress_details = self.suppress_details

        suppress_price: Union[None, Unset, bool]
        if isinstance(self.suppress_price, Unset):
            suppress_price = UNSET
        else:
            suppress_price = self.suppress_price

        type: Union[None, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        else:
            type = self.type

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        listing_id: Union[None, Unset, int]
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if advertised_date is not UNSET:
            field_dict["advertisedDate"] = advertised_date
        if advertised_price is not UNSET:
            field_dict["advertisedPrice"] = advertised_price
        if agency is not UNSET:
            field_dict["agency"] = agency
        if agency_colour is not UNSET:
            field_dict["agencyColour"] = agency_colour
        if agency_id is not UNSET:
            field_dict["agencyId"] = agency_id
        if agency_logo is not UNSET:
            field_dict["agencyLogo"] = agency_logo
        if agency_url is not UNSET:
            field_dict["agencyUrl"] = agency_url
        if apm_agency_id is not UNSET:
            field_dict["apmAgencyId"] = apm_agency_id
        if source is not UNSET:
            field_dict["source"] = source
        if suppress_details is not UNSET:
            field_dict["suppressDetails"] = suppress_details
        if suppress_price is not UNSET:
            field_dict["suppressPrice"] = suppress_price
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_advertised_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                advertised_date_type_0 = isoparse(data)

                return advertised_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        advertised_date = _parse_advertised_date(d.pop("advertisedDate", UNSET))

        def _parse_advertised_price(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        advertised_price = _parse_advertised_price(d.pop("advertisedPrice", UNSET))

        def _parse_agency(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency = _parse_agency(d.pop("agency", UNSET))

        def _parse_agency_colour(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_colour = _parse_agency_colour(d.pop("agencyColour", UNSET))

        def _parse_agency_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        agency_id = _parse_agency_id(d.pop("agencyId", UNSET))

        def _parse_agency_logo(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_logo = _parse_agency_logo(d.pop("agencyLogo", UNSET))

        def _parse_agency_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_url = _parse_agency_url(d.pop("agencyUrl", UNSET))

        def _parse_apm_agency_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        apm_agency_id = _parse_apm_agency_id(d.pop("apmAgencyId", UNSET))

        def _parse_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_suppress_details(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        suppress_details = _parse_suppress_details(d.pop("suppressDetails", UNSET))

        def _parse_suppress_price(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        suppress_price = _parse_suppress_price(d.pop("suppressPrice", UNSET))

        def _parse_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type = _parse_type(d.pop("type", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_listing_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))

        properties_v1_activity_boundary = cls(
            advertised_date=advertised_date,
            advertised_price=advertised_price,
            agency=agency,
            agency_colour=agency_colour,
            agency_id=agency_id,
            agency_logo=agency_logo,
            agency_url=agency_url,
            apm_agency_id=apm_agency_id,
            source=source,
            suppress_details=suppress_details,
            suppress_price=suppress_price,
            type=type,
            url=url,
            listing_id=listing_id,
        )

        return properties_v1_activity_boundary
