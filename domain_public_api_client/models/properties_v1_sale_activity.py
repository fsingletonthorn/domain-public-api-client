import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.properties_v1_activity_boundary import PropertiesV1ActivityBoundary


T = TypeVar("T", bound="PropertiesV1SaleActivity")


@_attrs_define
class PropertiesV1SaleActivity:
    """
    Attributes:
        agency (Union[None, Unset, str]): Gets or Sets Agency
        agency_colour (Union[None, Unset, str]): Gets or Sets AgencyColour
        agency_id (Union[None, Unset, int]): Gets or Sets AgencyId
        agency_logo (Union[None, Unset, str]): Gets or Sets AgencyLogo
        agency_url (Union[None, Unset, str]): Gets or Sets AgencyUrl
        apm_agency_id (Union[None, Unset, int]): Gets or Sets ApmAgencyId
        date (Union[None, Unset, datetime.datetime]): Gets or Sets Date
        days_on_market (Union[None, Unset, float]): Gets or Sets DaysOnMarket
        documented_as_sold (Union[None, Unset, bool]): Gets or Sets DocumentedAsSold
        price (Union[None, Unset, int]): Gets or Sets Price
        reported_as_sold (Union[None, Unset, bool]): Gets or Sets ReportedAsSold
        suppress_details (Union[None, Unset, bool]): Gets or Sets SuppressDetails
        suppress_price (Union[None, Unset, bool]): Gets or Sets SuppressPrice
        type (Union[None, Unset, str]): Gets or Sets Type
        url (Union[None, Unset, str]): Gets or Sets Url
        first (Union[Unset, PropertiesV1ActivityBoundary]):
        id (Union[None, Unset, int]): Gets or Sets Id
        last (Union[Unset, PropertiesV1ActivityBoundary]):
        property_type (Union[None, Unset, str]): Gets or Sets PropertyType
        listing_id (Union[None, Unset, int]):
    """

    agency: Union[None, Unset, str] = UNSET
    agency_colour: Union[None, Unset, str] = UNSET
    agency_id: Union[None, Unset, int] = UNSET
    agency_logo: Union[None, Unset, str] = UNSET
    agency_url: Union[None, Unset, str] = UNSET
    apm_agency_id: Union[None, Unset, int] = UNSET
    date: Union[None, Unset, datetime.datetime] = UNSET
    days_on_market: Union[None, Unset, float] = UNSET
    documented_as_sold: Union[None, Unset, bool] = UNSET
    price: Union[None, Unset, int] = UNSET
    reported_as_sold: Union[None, Unset, bool] = UNSET
    suppress_details: Union[None, Unset, bool] = UNSET
    suppress_price: Union[None, Unset, bool] = UNSET
    type: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    first: Union[Unset, "PropertiesV1ActivityBoundary"] = UNSET
    id: Union[None, Unset, int] = UNSET
    last: Union[Unset, "PropertiesV1ActivityBoundary"] = UNSET
    property_type: Union[None, Unset, str] = UNSET
    listing_id: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
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

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        days_on_market: Union[None, Unset, float]
        if isinstance(self.days_on_market, Unset):
            days_on_market = UNSET
        else:
            days_on_market = self.days_on_market

        documented_as_sold: Union[None, Unset, bool]
        if isinstance(self.documented_as_sold, Unset):
            documented_as_sold = UNSET
        else:
            documented_as_sold = self.documented_as_sold

        price: Union[None, Unset, int]
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        reported_as_sold: Union[None, Unset, bool]
        if isinstance(self.reported_as_sold, Unset):
            reported_as_sold = UNSET
        else:
            reported_as_sold = self.reported_as_sold

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

        first: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.first, Unset):
            first = self.first.to_dict()

        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        last: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last, Unset):
            last = self.last.to_dict()

        property_type: Union[None, Unset, str]
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

        listing_id: Union[None, Unset, int]
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
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
        if date is not UNSET:
            field_dict["date"] = date
        if days_on_market is not UNSET:
            field_dict["daysOnMarket"] = days_on_market
        if documented_as_sold is not UNSET:
            field_dict["documentedAsSold"] = documented_as_sold
        if price is not UNSET:
            field_dict["price"] = price
        if reported_as_sold is not UNSET:
            field_dict["reportedAsSold"] = reported_as_sold
        if suppress_details is not UNSET:
            field_dict["suppressDetails"] = suppress_details
        if suppress_price is not UNSET:
            field_dict["suppressPrice"] = suppress_price
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url
        if first is not UNSET:
            field_dict["first"] = first
        if id is not UNSET:
            field_dict["id"] = id
        if last is not UNSET:
            field_dict["last"] = last
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.properties_v1_activity_boundary import PropertiesV1ActivityBoundary

        d = src_dict.copy()

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

        def _parse_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_days_on_market(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        days_on_market = _parse_days_on_market(d.pop("daysOnMarket", UNSET))

        def _parse_documented_as_sold(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        documented_as_sold = _parse_documented_as_sold(d.pop("documentedAsSold", UNSET))

        def _parse_price(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_reported_as_sold(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        reported_as_sold = _parse_reported_as_sold(d.pop("reportedAsSold", UNSET))

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

        _first = d.pop("first", UNSET)
        first: Union[Unset, PropertiesV1ActivityBoundary]
        if isinstance(_first, Unset):
            first = UNSET
        else:
            first = PropertiesV1ActivityBoundary.from_dict(_first)

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        _last = d.pop("last", UNSET)
        last: Union[Unset, PropertiesV1ActivityBoundary]
        if isinstance(_last, Unset):
            last = UNSET
        else:
            last = PropertiesV1ActivityBoundary.from_dict(_last)

        def _parse_property_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_type = _parse_property_type(d.pop("propertyType", UNSET))

        def _parse_listing_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))

        properties_v1_sale_activity = cls(
            agency=agency,
            agency_colour=agency_colour,
            agency_id=agency_id,
            agency_logo=agency_logo,
            agency_url=agency_url,
            apm_agency_id=apm_agency_id,
            date=date,
            days_on_market=days_on_market,
            documented_as_sold=documented_as_sold,
            price=price,
            reported_as_sold=reported_as_sold,
            suppress_details=suppress_details,
            suppress_price=suppress_price,
            type=type,
            url=url,
            first=first,
            id=id,
            last=last,
            property_type=property_type,
            listing_id=listing_id,
        )

        return properties_v1_sale_activity
