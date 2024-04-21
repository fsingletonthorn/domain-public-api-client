import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.pre_market_v1_authority_type import PreMarketV1AuthorityType
from ..models.pre_market_v1_pre_portal_listing_status import PreMarketV1PrePortalListingStatus
from ..models.pre_market_v1_property_type import PreMarketV1PropertyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pre_market_v1_address_response import PreMarketV1AddressResponse
    from ..models.pre_market_v1_advertiser_identifiers import PreMarketV1AdvertiserIdentifiers
    from ..models.pre_market_v1_geo_location import PreMarketV1GeoLocation
    from ..models.pre_market_v1_listing_response_metadata_type_0 import PreMarketV1ListingResponseMetadataType0
    from ..models.pre_market_v1_price import PreMarketV1Price
    from ..models.pre_market_v1_property_media import PreMarketV1PropertyMedia
    from ..models.pre_market_v1_provider_details import PreMarketV1ProviderDetails
    from ..models.pre_market_v1_sold_details import PreMarketV1SoldDetails
    from ..models.pre_market_v1_statement_of_information import PreMarketV1StatementOfInformation


T = TypeVar("T", bound="PreMarketV1ListingResponse")


@_attrs_define
class PreMarketV1ListingResponse:
    """Pre-portal listing response.

    Attributes:
        id (str): Pre-portal listing ID.
        listing_status (PreMarketV1PrePortalListingStatus):
        address (PreMarketV1AddressResponse):
        bedrooms (float): Total number of bedrooms in the property.
        bathrooms (float): Total number of bathrooms in the property.
        carspaces (float): Total number of car spaces in the property.
        estimated_sale_price (PreMarketV1Price):
        related_ad_id (Union[None, Unset, int]): The Domain Ad Id of the related listing.
        provider_details (Union[Unset, PreMarketV1ProviderDetails]): Information for the listing provider
        advertiser_identifiers (Union[Unset, PreMarketV1AdvertiserIdentifiers]):
        headline (Union[None, Unset, str]): The short description of the property provided by the advertiser.
        description (Union[None, Unset, str]): The long description of the property provided by the advertiser.
        authority_executed_date (Union[None, Unset, datetime.datetime]): The date on which the authority contract was
            executed.
            The date is compliant with the ISO 8601 and is in the UTC format, e.g. 2009-06-15T13:45:30.0000000Z.
        reserve_price (Union[None, Unset, float]): Vendor reserve price.
        property_types (Union[List[PreMarketV1PropertyType], None, Unset]): The property types (e.g. house,
            apartment/unit/flat, etc.).
        authority_type (Union[Unset, PreMarketV1AuthorityType]):
        exclusive_period_days (Union[None, Unset, int]): The time (in days) that the agent has exclusive authority to
            sell the property.
        exclusive_continuing_period_days (Union[None, Unset, int]): The time (in days) that exclusive authority has been
            extended.
        exclusive_period_start_date (Union[None, Unset, datetime.datetime]): Start date of the exclusivity period.
            The date is compliant with the ISO 8601 and is in the UTC format, e.g. 2009-06-15T13:45:30.0000000Z.
        geo_location (Union[Unset, PreMarketV1GeoLocation]): Encapsulates the details of a geo location.
        map_certainty (Union[Unset, int]): Map certainty of the property location.
        media (Union[List['PreMarketV1PropertyMedia'], None, Unset]): The media associated with the property provided by
            the advertiser.
        property_id (Union[None, Unset, str]): The identifier which uniquely identifies the property being advertised.
            This may be empty if the Address of property is poorly described.
        statement_of_information (Union[Unset, PreMarketV1StatementOfInformation]):
        date_created (Union[Unset, datetime.datetime]): The date/time the listing was created.
            The date is compliant with the ISO 8601 and is in the UTC format, e.g. 2009-06-15T13:45:30.0000000Z.
        date_updated (Union[Unset, datetime.datetime]): The date/time the listing was last updated.
            The date is compliant with the ISO 8601 and is in the UTC format, e.g. 2009-06-15T13:45:30.0000000Z.
        date_pre_market (Union[None, Unset, datetime.datetime]): The date/time the listing went pre-market.
            The date is compliant with the ISO 8601 and is in the UTC format, e.g. 2009-06-15T13:45:30.0000000Z.
        date_listed (Union[None, Unset, datetime.datetime]): The date/time the listing was listed.
            The date is compliant with the ISO 8601 and is in the UTC format, e.g. 2009-06-15T13:45:30.0000000Z.
        date_sold (Union[None, Unset, datetime.datetime]): The date/time when the listing status was changed to sold (it
            is NOT the date/time when the property was sold).
            The date is compliant with the ISO 8601 and is in the UTC format, e.g. 2009-06-15T13:45:30.0000000Z.
        date_withdrawn (Union[None, Unset, datetime.datetime]): The date/time the listing was withdrawn.
            The date is compliant with the ISO 8601 and is in the UTC format, e.g. 2009-06-15T13:45:30.0000000Z.
        date_drafted (Union[None, Unset, datetime.datetime]): The date/time the listing was drafted.
            The date is compliant with the ISO 8601 and is in the UTC format, e.g. 2009-06-15T13:45:30.0000000Z.
        metadata (Union['PreMarketV1ListingResponseMetadataType0', None, Unset]): Optional listing metadata.
        comment (Union[None, Unset, str]): Optional listing comment.
        sold_details (Union[Unset, PreMarketV1SoldDetails]):
    """

    id: str
    listing_status: PreMarketV1PrePortalListingStatus
    address: "PreMarketV1AddressResponse"
    bedrooms: float
    bathrooms: float
    carspaces: float
    estimated_sale_price: "PreMarketV1Price"
    related_ad_id: Union[None, Unset, int] = UNSET
    provider_details: Union[Unset, "PreMarketV1ProviderDetails"] = UNSET
    advertiser_identifiers: Union[Unset, "PreMarketV1AdvertiserIdentifiers"] = UNSET
    headline: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    authority_executed_date: Union[None, Unset, datetime.datetime] = UNSET
    reserve_price: Union[None, Unset, float] = UNSET
    property_types: Union[List[PreMarketV1PropertyType], None, Unset] = UNSET
    authority_type: Union[Unset, PreMarketV1AuthorityType] = UNSET
    exclusive_period_days: Union[None, Unset, int] = UNSET
    exclusive_continuing_period_days: Union[None, Unset, int] = UNSET
    exclusive_period_start_date: Union[None, Unset, datetime.datetime] = UNSET
    geo_location: Union[Unset, "PreMarketV1GeoLocation"] = UNSET
    map_certainty: Union[Unset, int] = UNSET
    media: Union[List["PreMarketV1PropertyMedia"], None, Unset] = UNSET
    property_id: Union[None, Unset, str] = UNSET
    statement_of_information: Union[Unset, "PreMarketV1StatementOfInformation"] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    date_updated: Union[Unset, datetime.datetime] = UNSET
    date_pre_market: Union[None, Unset, datetime.datetime] = UNSET
    date_listed: Union[None, Unset, datetime.datetime] = UNSET
    date_sold: Union[None, Unset, datetime.datetime] = UNSET
    date_withdrawn: Union[None, Unset, datetime.datetime] = UNSET
    date_drafted: Union[None, Unset, datetime.datetime] = UNSET
    metadata: Union["PreMarketV1ListingResponseMetadataType0", None, Unset] = UNSET
    comment: Union[None, Unset, str] = UNSET
    sold_details: Union[Unset, "PreMarketV1SoldDetails"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.pre_market_v1_listing_response_metadata_type_0 import PreMarketV1ListingResponseMetadataType0

        id = self.id

        listing_status = self.listing_status.value

        address = self.address.to_dict()

        bedrooms = self.bedrooms

        bathrooms = self.bathrooms

        carspaces = self.carspaces

        estimated_sale_price = self.estimated_sale_price.to_dict()

        related_ad_id: Union[None, Unset, int]
        if isinstance(self.related_ad_id, Unset):
            related_ad_id = UNSET
        else:
            related_ad_id = self.related_ad_id

        provider_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider_details, Unset):
            provider_details = self.provider_details.to_dict()

        advertiser_identifiers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.advertiser_identifiers, Unset):
            advertiser_identifiers = self.advertiser_identifiers.to_dict()

        headline: Union[None, Unset, str]
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        authority_executed_date: Union[None, Unset, str]
        if isinstance(self.authority_executed_date, Unset):
            authority_executed_date = UNSET
        elif isinstance(self.authority_executed_date, datetime.datetime):
            authority_executed_date = self.authority_executed_date.isoformat()
        else:
            authority_executed_date = self.authority_executed_date

        reserve_price: Union[None, Unset, float]
        if isinstance(self.reserve_price, Unset):
            reserve_price = UNSET
        else:
            reserve_price = self.reserve_price

        property_types: Union[List[str], None, Unset]
        if isinstance(self.property_types, Unset):
            property_types = UNSET
        elif isinstance(self.property_types, list):
            property_types = []
            for property_types_type_0_item_data in self.property_types:
                property_types_type_0_item = property_types_type_0_item_data.value
                property_types.append(property_types_type_0_item)

        else:
            property_types = self.property_types

        authority_type: Union[Unset, str] = UNSET
        if not isinstance(self.authority_type, Unset):
            authority_type = self.authority_type.value

        exclusive_period_days: Union[None, Unset, int]
        if isinstance(self.exclusive_period_days, Unset):
            exclusive_period_days = UNSET
        else:
            exclusive_period_days = self.exclusive_period_days

        exclusive_continuing_period_days: Union[None, Unset, int]
        if isinstance(self.exclusive_continuing_period_days, Unset):
            exclusive_continuing_period_days = UNSET
        else:
            exclusive_continuing_period_days = self.exclusive_continuing_period_days

        exclusive_period_start_date: Union[None, Unset, str]
        if isinstance(self.exclusive_period_start_date, Unset):
            exclusive_period_start_date = UNSET
        elif isinstance(self.exclusive_period_start_date, datetime.datetime):
            exclusive_period_start_date = self.exclusive_period_start_date.isoformat()
        else:
            exclusive_period_start_date = self.exclusive_period_start_date

        geo_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geo_location, Unset):
            geo_location = self.geo_location.to_dict()

        map_certainty = self.map_certainty

        media: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.media, Unset):
            media = UNSET
        elif isinstance(self.media, list):
            media = []
            for media_type_0_item_data in self.media:
                media_type_0_item = media_type_0_item_data.to_dict()
                media.append(media_type_0_item)

        else:
            media = self.media

        property_id: Union[None, Unset, str]
        if isinstance(self.property_id, Unset):
            property_id = UNSET
        else:
            property_id = self.property_id

        statement_of_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.statement_of_information, Unset):
            statement_of_information = self.statement_of_information.to_dict()

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_updated: Union[Unset, str] = UNSET
        if not isinstance(self.date_updated, Unset):
            date_updated = self.date_updated.isoformat()

        date_pre_market: Union[None, Unset, str]
        if isinstance(self.date_pre_market, Unset):
            date_pre_market = UNSET
        elif isinstance(self.date_pre_market, datetime.datetime):
            date_pre_market = self.date_pre_market.isoformat()
        else:
            date_pre_market = self.date_pre_market

        date_listed: Union[None, Unset, str]
        if isinstance(self.date_listed, Unset):
            date_listed = UNSET
        elif isinstance(self.date_listed, datetime.datetime):
            date_listed = self.date_listed.isoformat()
        else:
            date_listed = self.date_listed

        date_sold: Union[None, Unset, str]
        if isinstance(self.date_sold, Unset):
            date_sold = UNSET
        elif isinstance(self.date_sold, datetime.datetime):
            date_sold = self.date_sold.isoformat()
        else:
            date_sold = self.date_sold

        date_withdrawn: Union[None, Unset, str]
        if isinstance(self.date_withdrawn, Unset):
            date_withdrawn = UNSET
        elif isinstance(self.date_withdrawn, datetime.datetime):
            date_withdrawn = self.date_withdrawn.isoformat()
        else:
            date_withdrawn = self.date_withdrawn

        date_drafted: Union[None, Unset, str]
        if isinstance(self.date_drafted, Unset):
            date_drafted = UNSET
        elif isinstance(self.date_drafted, datetime.datetime):
            date_drafted = self.date_drafted.isoformat()
        else:
            date_drafted = self.date_drafted

        metadata: Union[Dict[str, Any], None, Unset]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PreMarketV1ListingResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        sold_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sold_details, Unset):
            sold_details = self.sold_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "listingStatus": listing_status,
                "address": address,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "carspaces": carspaces,
                "estimatedSalePrice": estimated_sale_price,
            }
        )
        if related_ad_id is not UNSET:
            field_dict["relatedAdId"] = related_ad_id
        if provider_details is not UNSET:
            field_dict["providerDetails"] = provider_details
        if advertiser_identifiers is not UNSET:
            field_dict["advertiserIdentifiers"] = advertiser_identifiers
        if headline is not UNSET:
            field_dict["headline"] = headline
        if description is not UNSET:
            field_dict["description"] = description
        if authority_executed_date is not UNSET:
            field_dict["authorityExecutedDate"] = authority_executed_date
        if reserve_price is not UNSET:
            field_dict["reservePrice"] = reserve_price
        if property_types is not UNSET:
            field_dict["propertyTypes"] = property_types
        if authority_type is not UNSET:
            field_dict["authorityType"] = authority_type
        if exclusive_period_days is not UNSET:
            field_dict["exclusivePeriodDays"] = exclusive_period_days
        if exclusive_continuing_period_days is not UNSET:
            field_dict["exclusiveContinuingPeriodDays"] = exclusive_continuing_period_days
        if exclusive_period_start_date is not UNSET:
            field_dict["exclusivePeriodStartDate"] = exclusive_period_start_date
        if geo_location is not UNSET:
            field_dict["geoLocation"] = geo_location
        if map_certainty is not UNSET:
            field_dict["mapCertainty"] = map_certainty
        if media is not UNSET:
            field_dict["media"] = media
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if statement_of_information is not UNSET:
            field_dict["statementOfInformation"] = statement_of_information
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_updated is not UNSET:
            field_dict["dateUpdated"] = date_updated
        if date_pre_market is not UNSET:
            field_dict["datePreMarket"] = date_pre_market
        if date_listed is not UNSET:
            field_dict["dateListed"] = date_listed
        if date_sold is not UNSET:
            field_dict["dateSold"] = date_sold
        if date_withdrawn is not UNSET:
            field_dict["dateWithdrawn"] = date_withdrawn
        if date_drafted is not UNSET:
            field_dict["dateDrafted"] = date_drafted
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if comment is not UNSET:
            field_dict["comment"] = comment
        if sold_details is not UNSET:
            field_dict["soldDetails"] = sold_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pre_market_v1_address_response import PreMarketV1AddressResponse
        from ..models.pre_market_v1_advertiser_identifiers import PreMarketV1AdvertiserIdentifiers
        from ..models.pre_market_v1_geo_location import PreMarketV1GeoLocation
        from ..models.pre_market_v1_listing_response_metadata_type_0 import PreMarketV1ListingResponseMetadataType0
        from ..models.pre_market_v1_price import PreMarketV1Price
        from ..models.pre_market_v1_property_media import PreMarketV1PropertyMedia
        from ..models.pre_market_v1_provider_details import PreMarketV1ProviderDetails
        from ..models.pre_market_v1_sold_details import PreMarketV1SoldDetails
        from ..models.pre_market_v1_statement_of_information import PreMarketV1StatementOfInformation

        d = src_dict.copy()
        id = d.pop("id")

        listing_status = PreMarketV1PrePortalListingStatus(d.pop("listingStatus"))

        address = PreMarketV1AddressResponse.from_dict(d.pop("address"))

        bedrooms = d.pop("bedrooms")

        bathrooms = d.pop("bathrooms")

        carspaces = d.pop("carspaces")

        estimated_sale_price = PreMarketV1Price.from_dict(d.pop("estimatedSalePrice"))

        def _parse_related_ad_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        related_ad_id = _parse_related_ad_id(d.pop("relatedAdId", UNSET))

        _provider_details = d.pop("providerDetails", UNSET)
        provider_details: Union[Unset, PreMarketV1ProviderDetails]
        if isinstance(_provider_details, Unset):
            provider_details = UNSET
        else:
            provider_details = PreMarketV1ProviderDetails.from_dict(_provider_details)

        _advertiser_identifiers = d.pop("advertiserIdentifiers", UNSET)
        advertiser_identifiers: Union[Unset, PreMarketV1AdvertiserIdentifiers]
        if isinstance(_advertiser_identifiers, Unset):
            advertiser_identifiers = UNSET
        else:
            advertiser_identifiers = PreMarketV1AdvertiserIdentifiers.from_dict(_advertiser_identifiers)

        def _parse_headline(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        headline = _parse_headline(d.pop("headline", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_authority_executed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authority_executed_date_type_0 = isoparse(data)

                return authority_executed_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        authority_executed_date = _parse_authority_executed_date(d.pop("authorityExecutedDate", UNSET))

        def _parse_reserve_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        reserve_price = _parse_reserve_price(d.pop("reservePrice", UNSET))

        def _parse_property_types(data: object) -> Union[List[PreMarketV1PropertyType], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                property_types_type_0 = []
                _property_types_type_0 = data
                for property_types_type_0_item_data in _property_types_type_0:
                    property_types_type_0_item = PreMarketV1PropertyType(property_types_type_0_item_data)

                    property_types_type_0.append(property_types_type_0_item)

                return property_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[PreMarketV1PropertyType], None, Unset], data)

        property_types = _parse_property_types(d.pop("propertyTypes", UNSET))

        _authority_type = d.pop("authorityType", UNSET)
        authority_type: Union[Unset, PreMarketV1AuthorityType]
        if isinstance(_authority_type, Unset):
            authority_type = UNSET
        else:
            authority_type = PreMarketV1AuthorityType(_authority_type)

        def _parse_exclusive_period_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        exclusive_period_days = _parse_exclusive_period_days(d.pop("exclusivePeriodDays", UNSET))

        def _parse_exclusive_continuing_period_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        exclusive_continuing_period_days = _parse_exclusive_continuing_period_days(
            d.pop("exclusiveContinuingPeriodDays", UNSET)
        )

        def _parse_exclusive_period_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exclusive_period_start_date_type_0 = isoparse(data)

                return exclusive_period_start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        exclusive_period_start_date = _parse_exclusive_period_start_date(d.pop("exclusivePeriodStartDate", UNSET))

        _geo_location = d.pop("geoLocation", UNSET)
        geo_location: Union[Unset, PreMarketV1GeoLocation]
        if isinstance(_geo_location, Unset):
            geo_location = UNSET
        else:
            geo_location = PreMarketV1GeoLocation.from_dict(_geo_location)

        map_certainty = d.pop("mapCertainty", UNSET)

        def _parse_media(data: object) -> Union[List["PreMarketV1PropertyMedia"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_type_0 = []
                _media_type_0 = data
                for media_type_0_item_data in _media_type_0:
                    media_type_0_item = PreMarketV1PropertyMedia.from_dict(media_type_0_item_data)

                    media_type_0.append(media_type_0_item)

                return media_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PreMarketV1PropertyMedia"], None, Unset], data)

        media = _parse_media(d.pop("media", UNSET))

        def _parse_property_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_id = _parse_property_id(d.pop("propertyId", UNSET))

        _statement_of_information = d.pop("statementOfInformation", UNSET)
        statement_of_information: Union[Unset, PreMarketV1StatementOfInformation]
        if isinstance(_statement_of_information, Unset):
            statement_of_information = UNSET
        else:
            statement_of_information = PreMarketV1StatementOfInformation.from_dict(_statement_of_information)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _date_updated = d.pop("dateUpdated", UNSET)
        date_updated: Union[Unset, datetime.datetime]
        if isinstance(_date_updated, Unset):
            date_updated = UNSET
        else:
            date_updated = isoparse(_date_updated)

        def _parse_date_pre_market(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_pre_market_type_0 = isoparse(data)

                return date_pre_market_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_pre_market = _parse_date_pre_market(d.pop("datePreMarket", UNSET))

        def _parse_date_listed(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_listed_type_0 = isoparse(data)

                return date_listed_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_listed = _parse_date_listed(d.pop("dateListed", UNSET))

        def _parse_date_sold(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_sold_type_0 = isoparse(data)

                return date_sold_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_sold = _parse_date_sold(d.pop("dateSold", UNSET))

        def _parse_date_withdrawn(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_withdrawn_type_0 = isoparse(data)

                return date_withdrawn_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_withdrawn = _parse_date_withdrawn(d.pop("dateWithdrawn", UNSET))

        def _parse_date_drafted(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_drafted_type_0 = isoparse(data)

                return date_drafted_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_drafted = _parse_date_drafted(d.pop("dateDrafted", UNSET))

        def _parse_metadata(data: object) -> Union["PreMarketV1ListingResponseMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = PreMarketV1ListingResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PreMarketV1ListingResponseMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        _sold_details = d.pop("soldDetails", UNSET)
        sold_details: Union[Unset, PreMarketV1SoldDetails]
        if isinstance(_sold_details, Unset):
            sold_details = UNSET
        else:
            sold_details = PreMarketV1SoldDetails.from_dict(_sold_details)

        pre_market_v1_listing_response = cls(
            id=id,
            listing_status=listing_status,
            address=address,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            carspaces=carspaces,
            estimated_sale_price=estimated_sale_price,
            related_ad_id=related_ad_id,
            provider_details=provider_details,
            advertiser_identifiers=advertiser_identifiers,
            headline=headline,
            description=description,
            authority_executed_date=authority_executed_date,
            reserve_price=reserve_price,
            property_types=property_types,
            authority_type=authority_type,
            exclusive_period_days=exclusive_period_days,
            exclusive_continuing_period_days=exclusive_continuing_period_days,
            exclusive_period_start_date=exclusive_period_start_date,
            geo_location=geo_location,
            map_certainty=map_certainty,
            media=media,
            property_id=property_id,
            statement_of_information=statement_of_information,
            date_created=date_created,
            date_updated=date_updated,
            date_pre_market=date_pre_market,
            date_listed=date_listed,
            date_sold=date_sold,
            date_withdrawn=date_withdrawn,
            date_drafted=date_drafted,
            metadata=metadata,
            comment=comment,
            sold_details=sold_details,
        )

        return pre_market_v1_listing_response
